from pysnmp.hlapi.asyncore import *


def cbFun(snmpEngine, sendRequestHandle, errorIndication, errorStatus, errorIndex, varBinds, cbCtx):
    if errorIndication:
        print(errorIndication)
        return
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBindTable[-1][int(errorIndex) - 1][0] or '?'))
        return
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))


def main(community, host, oid):
    snmpEngine = SnmpEngine()
    getCmd(snmpEngine, CommunityData(community), UdpTransportTarget((host, 161)), ContextData(),
           ObjectType(ObjectIdentity(oid)), cbFun=cbFun)
    snmpEngine.transportDispatcher.runDispatcher()