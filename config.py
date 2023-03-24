
class Config():
    def __init__(self):
        self.ip_addr = "192.168.10.23"
        self.port = "10000"

        self.Capabilities = {
            "ip_addr":f'{self.ip_addr}:{self.port}'
        }

        self.DeviceInformation = {
            'Manufacturer':"Smiths Detection",
            'Model':"HS6040i",
            'FirmwareVersion':"HX-03",
            'SerialNumber':"150453",
            'HardwareId':"HiTrax"
        }

        self.Scopes = [
            {'ScopeDef':"Fixed",
            'ScopeItem':"onvif://www.onvif.org/manufacturer/SmithDetection"},
            {'ScopeDef':"Fixed",
            'ScopeItem':"onvif://www.onvif.org/location/Russia"},
            ]
