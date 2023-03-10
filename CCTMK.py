from bottle import Bottle, request, run, response
import requests 
import time
from pic import pic
from Responses import *
from jinja2 import Template, FileSystemLoader, Environment

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('dinfo.xml')
GetDeviceInformationData = {
    'Manufacturer':"M_1",
    'Model':"M_2",
    'FirmwareVersion':"F_1",
    'SerialNumber':"S_1",
    'HardwareId':"H_1"
}

output = template.render(data = GetDeviceInformationData)




app = Bottle()

HOST = "192.168.10.23"  # Standard loopback interface address (localhost)
PORT = 10000  # Port to listen on (non-privileged ports are > 1023)



@app.route('/onvif/device_service', method="POST")
def connect():
    soap_action = request.get_header('SOAPAction')
    #print(request.body.readlines()[0].decode('utf-8'))
    print(soap_action)
    
    if soap_action == "http://www.onvif.org/ver10/device/wsdl/GetCapabilities":
        response.set_header("SOAPAction","http://www.onvif.org/ver10/device/wsdl/GetCapabilities")
        response.content_type = 'application/soap+xml;  charset=utf-8; action="http://www.onvif.org/ver10/device/wsdl/GetCapabilities"'
        resp = GetCapabilitiesResponse
    elif soap_action == "http://www.onvif.org/ver10/device/wsdl/GetScopes":
        response.set_header("SOAPAction","http://www.onvif.org/ver10/device/wsdl/GetScopes")
        response.content_type = 'application/soap+xml;  charset=utf-8; action="http://www.onvif.org/ver10/device/wsdl/GetScopes"'
        resp = GetScopesResponse
    elif soap_action == "http://www.onvif.org/ver10/device/wsdl/GetDeviceInformation":
        response.set_header("SOAPAction","http://www.onvif.org/ver10/device/wsdl/GetDeviceInformation")
        response.content_type = 'application/soap+xml;  charset=utf-8; action="http://www.onvif.org/ver10/device/wsdl/GetDeviceInformation"'
        resp = GetDeviceInformationResponse
    elif soap_action == "http://www.onvif.org/ver10/events/wsdl/EventPortType/GetServiceCapabilitiesRequest":
        response.set_header("SOAPAction","http://www.onvif.org/ver10/device/wsdl/GetServiceCapabilitiesRequest")
        response.content_type = 'application/soap+xml;  charset=utf-8; action="http://www.onvif.org/ver10/device/wsdl/GetServiceCapabilitiesRequest"'
        resp = GetServiceCapabilitiesResponse
    else:
        response.set_header("SOAPAction","http://www.onvif.org/ver10/device/wsdl/SubscribeResponse")
        response.content_type = 'application/soap+xml;  charset=utf-8; action="http://www.onvif.org/ver10/device/wsdl/SubscribeResponse"'
        resp = SubscribeResponse
        time.sleep(1)
        requests.post('http://192.168.10.192:18888/xci5ozc3pirck3dmbg78', data=NotifyRequest)
        
    return resp


if __name__ == "__main__":
    run(app, host='192.168.10.23', port=10000, debug=True)



