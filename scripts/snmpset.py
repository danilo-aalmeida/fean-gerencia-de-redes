from pysnmp.hlapi.asyncore import *


def cbFun(snmpEngine, sendRequestHandle, errorIndication, errorStatus, errorIndex, varBinds, cbCtx):
     print(errorIndication, errorStatus, errorIndex, varBinds)

def main(community, host, oid, valor):
    snmpEngine = SnmpEngine()
    setCmd(snmpEngine, CommunityData(community), UdpTransportTarget((host, 161)), ContextData(),
           ObjectType(ObjectIdentity(oid), valor), cbFun=cbFun)
    snmpEngine.transportDispatcher.runDispatcher()
# (None, 0, 0, [ObjectType(ObjectIdentity(ObjectName('1.3.6.1.2.1.1.4.0')), DisplayString('info@snmplabs.com'))])
