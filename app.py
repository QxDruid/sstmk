#!/usr/bin/python3
from bottle import Bottle, request, run, response


from config import Config
from cctmk import CCTMK


conf = Config()
cctmk = CCTMK(conf)
app = Bottle()

@app.route('/onvif/device_service', method="POST")
def connect():
    soap_action = request.get_header('SOAPAction')
    if soap_action:
        soap_action = soap_action.split('/')[-1]
    request_data = request.body.getvalue().decode('utf-8')
    
    response.set_header("SOAPAction",f"http://www.onvif.org/ver10/device/wsdl/{soap_action}")
    response.content_type = f'application/soap+xml;  charset=utf-8; action="http://www.onvif.org/ver10/device/wsdl/{soap_action}"'
    resp = cctmk.Run(soap_action, request_data)

    return resp


if __name__ == "__main__":
    run(app, host=conf.ip_addr, port=conf.port, debug=True)