from bottle import Bottle, request, run, response
import requests 
from jinja2 import Template, FileSystemLoader, Environment
import time
from threading import Thread
import re
import cv2
import base64 
import OPi.GPIO as GPIO
from config import Config



configuration = Config()
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

# GPIO INIT BLOCK
GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.OUT)
led_status = False

def buttonWait():
    res  = GPIO.wait_for_edge(22, GPIO.FALLING, 600000)
    if res:
        return True
    else:
        return False

def getScreenCapture():
    # define a video capture object
    Camera = cv2.VideoCapture(0, cv2.CAP_V4L2)
    time.sleep(0.5)
    return_value, image = Camera.read()
    print(f"videocap: {return_value}")
    cv2.imwrite("test.png", image)
    with open("test.png", "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    
    Camera.release()
    return my_string

def NotifyRequest(NotifyRequestData):
    res = buttonWait()
    GPIO.output(26, True)
    print(f"buttomwait = {res}")
    if res == None:
        return False
    NotifyRequestData['image'] = getScreenCapture().decode()
    NotifyRequestData['time'] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    template = env.get_template('NotifyRequest.xml')
    request = template.render(data = NotifyRequestData)

    requests.post(NotifyRequestData['notify_addr'], data=request)

    GPIO.output(26, False)

    return True

def GetCapabilitiesResponse():
    template = env.get_template('GetCapabilitiesResponse.xml')
    return template.render(data = configuration.Capabilities)

def GetScopesResponse():
    template = env.get_template('GetScopesResponse.xml')
    return template.render(data = configuration.Scopes)

def GetDeviceInformationResponse():
    template = env.get_template('GetDeviceInformationResponse.xml')
    return template.render(data = configuration.DeviceInformation)

def GetServiceCapabilitiesResponse():
    template = env.get_template('GetServiceCapabilitiesResponse.xml')
    return template.render()

def SubscribeResponse(data):
    template = env.get_template('SubscribeResponse.xml')
    return template.render(data = data)




app = Bottle()

@app.route('/onvif/device_service', method="POST")
def connect():
    soap_action = request.get_header('SOAPAction')
    if soap_action:
        soap_action = soap_action.split('/')[-1]
    request_data = request.body.getvalue().decode('utf-8')

    response.set_header("SOAPAction",f"http://www.onvif.org/ver10/device/wsdl/{soap_action}")
    response.content_type = f'application/soap+xml;  charset=utf-8; action="http://www.onvif.org/ver10/device/wsdl/{soap_action}"'
    

    if soap_action == "GetCapabilities":
        resp = GetCapabilitiesResponse()
    elif soap_action == "GetScopes":
        resp = GetScopesResponse()
    elif soap_action == "GetDeviceInformation":
        resp = GetDeviceInformationResponse()
    elif soap_action == "GetServiceCapabilitiesRequest":
        resp = GetServiceCapabilitiesResponse()
    else:
        response.set_header("SOAPAction","http://www.onvif.org/ver10/device/wsdl/SubscribeResponse")
        response.content_type = 'application/soap+xml;  charset=utf-8; action="http://www.onvif.org/ver10/device/wsdl/SubscribeResponse"'

        sec_utc = time.time()
        subscribe_data = {
            "self_addr": f'{configuration.ip_addr}:{configuration.port}',
            "current_time": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),
            "terminate_time": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(sec_utc + 60*60))
        }
        resp = SubscribeResponse(subscribe_data)
        resp_addr = re.search(r'<Address>.*</Address>', request_data)[0][9:-10]
        print(resp_addr)

        NotifyRequestData = {
            "notify_addr": resp_addr,
            "self_addr": f'{configuration.ip_addr}:{configuration.port}',
            "image": '',
            "id": configuration.DeviceInformation["SerialNumber"],
            "time": "",
        }
        
        th = Thread(target=NotifyRequest, daemon=True ,args=(NotifyRequestData, ))
        th.start()
        
    return resp


if __name__ == "__main__":
    run(app, host=configuration.ip_addr, port=configuration.port, debug=True)
