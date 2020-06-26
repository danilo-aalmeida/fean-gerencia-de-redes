import json
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
        resultados = []
        for varBind in varBinds:
            resultados.append(
                {'oid': varBind.__getitem__(0).prettyPrint(), 'value': varBind.__getitem__(1).prettyPrint()})
        print(json.dumps(resultados))


def main(user, md5, des, host, oid):
    snmpEngine = SnmpEngine()
    getCmd(snmpEngine,
           UsmUserData(user, md5, des),
           UdpTransportTarget((host, 161)),
           ContextData(),
           ObjectType(ObjectIdentity(oid)),
           cbFun=cbFun)
    snmpEngine.transportDispatcher.runDispatcher()
