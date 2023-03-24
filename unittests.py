import unittest
from CCTMK import *

class TestXMLRender(unittest.TestCase):
    def testScopes(self):
        self.maxDiff = None
        self.assertEqual(GetScopesResponse(), '<?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope" xmlns:SOAP-ENC="http://www.w3.org/2003/05/soap-encoding" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:chan="http://schemas.microsoft.com/ws/2005/02/duplex" xmlns:wsa5="http://www.w3.org/2005/08/addressing" xmlns:wsrfbf="http://docs.oasis-open.org/wsrf/bf-2" xmlns:xmime="http://www.w3.org/2005/05/xmlmime" xmlns:ns2="http://www.w3.org/2004/08/xop/include" xmlns:tt="http://www.onvif.org/ver10/schema" xmlns:wstop="http://docs.oasis-open.org/wsn/t-1" xmlns:wsrfr="http://docs.oasis-open.org/wsrf/r-2" xmlns:tds="http://www.onvif.org/ver10/device/wsdl" xmlns:tev="http://www.onvif.org/ver10/events/wsdl" xmlns:wsnt="http://docs.oasis-open.org/wsn/b-2" xmlns:c14n="http://www.w3.org/2001/10/xml-exc-c14n#" xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:saml1="urn:oasis:names:tc:SAML:1.0:assertion" xmlns:saml2="urn:oasis:names:tc:SAML:2.0:assertion" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" xmlns:xenc="http://www.w3.org/2001/04/xmlenc#" xmlns:wsc="http://docs.oasis-open.org/ws-sx/ws-secureconversation/200512" xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"><SOAP-ENV:Header></SOAP-ENV:Header><SOAP-ENV:Body><tds:GetScopesResponse><tds:Scopes><tt:ScopeDef>Fixed</tt:ScopeDef><tt:ScopeItem>onvif://www.onvif.org/manufacturer/SmithDetection</tt:ScopeItem></tds:Scopes><tds:Scopes><tt:ScopeDef>Fixed</tt:ScopeDef><tt:ScopeItem>onvif://www.onvif.org/location/Russia</tt:ScopeItem></tds:Scopes></tds:GetScopesResponse></SOAP-ENV:Body></SOAP-ENV:Envelope>')
    
    def testCapabilities(self):
        self.assertEqual(GetCapabilitiesResponse(), '<?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope" xmlns:SOAP-ENC="http://www.w3.org/2003/05/soap-encoding" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:chan="http://schemas.microsoft.com/ws/2005/02/duplex" xmlns:wsa5="http://www.w3.org/2005/08/addressing" xmlns:wsrfbf="http://docs.oasis-open.org/wsrf/bf-2" xmlns:xmime="http://www.w3.org/2005/05/xmlmime" xmlns:ns2="http://www.w3.org/2004/08/xop/include" xmlns:tt="http://www.onvif.org/ver10/schema" xmlns:wstop="http://docs.oasis-open.org/wsn/t-1" xmlns:wsrfr="http://docs.oasis-open.org/wsrf/r-2" xmlns:tds="http://www.onvif.org/ver10/device/wsdl" xmlns:tev="http://www.onvif.org/ver10/events/wsdl" xmlns:wsnt="http://docs.oasis-open.org/wsn/b-2" xmlns:c14n="http://www.w3.org/2001/10/xml-exc-c14n#" xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:saml1="urn:oasis:names:tc:SAML:1.0:assertion" xmlns:saml2="urn:oasis:names:tc:SAML:2.0:assertion" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" xmlns:xenc="http://www.w3.org/2001/04/xmlenc#" xmlns:wsc="http://docs.oasis-open.org/ws-sx/ws-secureconversation/200512" xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"><SOAP-ENV:Header></SOAP-ENV:Header><SOAP-ENV:Body><tds:GetCapabilitiesResponse><tds:Capabilities><tt:Device><tt:XAddr>http://192.168.10.23:10000/onvif/device_service</tt:XAddr><tt:Network></tt:Network><tt:System><tt:DiscoveryResolve>false</tt:DiscoveryResolve><tt:DiscoveryBye>false</tt:DiscoveryBye><tt:RemoteDiscovery>false</tt:RemoteDiscovery><tt:SystemBackup>false</tt:SystemBackup><tt:SystemLogging>false</tt:SystemLogging><tt:FirmwareUpgrade>false</tt:FirmwareUpgrade><tt:SupportedVersions><tt:Major>2</tt:Major><tt:Minor>0</tt:Minor></tt:SupportedVersions></tt:System><tt:IO></tt:IO><tt:Security><tt:TLS1.1>false</tt:TLS1.1><tt:TLS1.2>false</tt:TLS1.2><tt:OnboardKeyGeneration>false</tt:OnboardKeyGeneration><tt:AccessPolicyConfig>false</tt:AccessPolicyConfig><tt:X.509Token>false</tt:X.509Token><tt:SAMLToken>false</tt:SAMLToken><tt:KerberosToken>false</tt:KerberosToken><tt:RELToken>false</tt:RELToken></tt:Security></tt:Device><tt:Events><tt:XAddr>http://192.168.10.23:10000/onvif/device_service</tt:XAddr><tt:WSSubscriptionPolicySupport>false</tt:WSSubscriptionPolicySupport><tt:WSPullPointSupport>true</tt:WSPullPointSupport><tt:WSPausableSubscriptionManagerInterfaceSupport>false</tt:WSPausableSubscriptionManagerInterfaceSupport></tt:Events></tds:Capabilities></tds:GetCapabilitiesResponse></SOAP-ENV:Body></SOAP-ENV:Envelope>')

    def testDeviceInformation(self):
        self.assertEqual(GetDeviceInformationResponse(),'<?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope" xmlns:SOAP-ENC="http://www.w3.org/2003/05/soap-encoding" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:chan="http://schemas.microsoft.com/ws/2005/02/duplex" xmlns:wsa5="http://www.w3.org/2005/08/addressing" xmlns:wsrfbf="http://docs.oasis-open.org/wsrf/bf-2" xmlns:xmime="http://www.w3.org/2005/05/xmlmime" xmlns:ns2="http://www.w3.org/2004/08/xop/include" xmlns:tt="http://www.onvif.org/ver10/schema" xmlns:wstop="http://docs.oasis-open.org/wsn/t-1" xmlns:wsrfr="http://docs.oasis-open.org/wsrf/r-2" xmlns:tds="http://www.onvif.org/ver10/device/wsdl" xmlns:tev="http://www.onvif.org/ver10/events/wsdl" xmlns:wsnt="http://docs.oasis-open.org/wsn/b-2" xmlns:c14n="http://www.w3.org/2001/10/xml-exc-c14n#" xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:saml1="urn:oasis:names:tc:SAML:1.0:assertion" xmlns:saml2="urn:oasis:names:tc:SAML:2.0:assertion" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" xmlns:xenc="http://www.w3.org/2001/04/xmlenc#" xmlns:wsc="http://docs.oasis-open.org/ws-sx/ws-secureconversation/200512" xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"><SOAP-ENV:Header></SOAP-ENV:Header><SOAP-ENV:Body><tds:GetDeviceInformationResponse><tds:Manufacturer>Smiths Detection</tds:Manufacturer><tds:Model>HS6040i&#xD;</tds:Model><tds:FirmwareVersion>HX-03</tds:FirmwareVersion><tds:SerialNumber>150453&#xD;</tds:SerialNumber><tds:HardwareId>HiTrax</tds:HardwareId></tds:GetDeviceInformationResponse></SOAP-ENV:Body></SOAP-ENV:Envelope>')


    def testServiceCapabilities(self):
        self.assertEqual(GetServiceCapabilitiesResponse(),'<?xml version="1.0" encoding="utf-8"?><env:Envelope xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:env="http://www.w3.org/2003/05/soap-envelope" xmlns:tev="http://www.onvif.org/ver10/events/wsdl" xmlns:tt="http://www.onvif.org/ver10/schema"><env:Header><wsa:Action>http://www.onvif.org/ver10/events/wsdl/EventPortType/GetServiceCapabilitiesResponse</wsa:Action></env:Header><env:Body><tev:GetServiceCapabilitiesResponse><tev:Capabilities WSSubscriptionPolicySupport="true" WSPullPointSupport="true" WSPausableSubscriptionManagerInterfaceSupport="false" PersistentNotificationStorage="true" MaxNotificationProducers="30" MaxPullPoints="30"/></tev:GetServiceCapabilitiesResponse></env:Body></env:Envelope>')

if __name__ == '__main__':
    unittest.main()