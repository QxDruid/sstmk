import requests 
from jinja2 import Template, FileSystemLoader, Environment
import time
from threading import Thread
import re
import cv2
import base64 
import OPi.GPIO as GPIO

class CCTMK():
    def __init__(self, config) -> None:
        pass

        self.configuration = config
        self.file_loader = FileSystemLoader('templates')
        self.env = Environment(loader=self.file_loader)

        # GPIO INIT BLOCK
        GPIO.cleanup()

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(26, GPIO.OUT)
        self.led_status = False

    def buttonWait(self):
        res  = GPIO.wait_for_edge(22, GPIO.FALLING, 600000)
        if res:
            return True
        else:
            return False

    def getScreenCapture(self):
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

    def NotifyRequest(self, NotifyRequestData):
        res = self.buttonWait()
        GPIO.output(26, True)
        print(f"buttomwait = {res}")
        if res == None:
            return False
        NotifyRequestData['image'] = self.getScreenCapture().decode()
        NotifyRequestData['time'] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        template = self.env.get_template('NotifyRequest.xml')
        request = template.render(data = NotifyRequestData)

        requests.post(NotifyRequestData['notify_addr'], data=request)

        GPIO.output(26, False)

        return True

    def GetCapabilitiesResponse(self):
        template = self.env.get_template('GetCapabilitiesResponse.xml')
        return template.render(data = self.configuration.Capabilities)

    def GetScopesResponse(self):
        template = self.env.get_template('GetScopesResponse.xml')
        return template.render(data = self.configuration.Scopes)

    def GetDeviceInformationResponse(self):
        template = self.env.get_template('GetDeviceInformationResponse.xml')
        return template.render(data = self.configuration.DeviceInformation)

    def GetServiceCapabilitiesResponse(self):
        template = self.env.get_template('GetServiceCapabilitiesResponse.xml')
        return template.render()

    def SubscribeResponse(self, data):
        template = self.env.get_template('SubscribeResponse.xml')
        return template.render(data = data)

    def Run(self, soap_action, request_data):
        if soap_action == "GetCapabilities":
            resp = self.GetCapabilitiesResponse()
        elif soap_action == "GetScopes":
            resp = self.GetScopesResponse()
        elif soap_action == "GetDeviceInformation":
            resp = self.GetDeviceInformationResponse()
        elif soap_action == "GetServiceCapabilitiesRequest":
            resp = self.GetServiceCapabilitiesResponse()
        else:
            #response.set_header("SOAPAction","http://www.onvif.org/ver10/device/wsdl/SubscribeResponse")
            #response.content_type = 'application/soap+xml;  charset=utf-8; action="http://www.onvif.org/ver10/device/wsdl/SubscribeResponse"'

            sec_utc = time.time()
            subscribe_data = {
                "self_addr": f'{self.configuration.ip_addr}:{self.configuration.port}',
                "current_time": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),
                "terminate_time": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(sec_utc + 60*60))
            }
            resp = self.SubscribeResponse(subscribe_data)
            resp_addr = re.search(r'<Address>.*</Address>', request_data)[0][9:-10]
            print(resp_addr)

            NotifyRequestData = {
                "notify_addr": resp_addr,
                "self_addr": f'{self.configuration.ip_addr}:{self.configuration.port}',
                "image": '',
                "id": self.configuration.DeviceInformation["SerialNumber"],
                "time": "",
            }
            
            th = Thread(target=self.NotifyRequest, daemon=True ,args=(NotifyRequestData, ))
            th.start()
        return resp


