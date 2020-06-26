import json

from pysnmp.hlapi.asyncore import *
from pysnmp.hlapi import *

def cbFun(errorIndication,errorStatus, errorIndex, varBinds):
    if errorIndication:
        print(errorIndication)
        return
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[-1][int(errorIndex) - 1][0] or '?'))
        return
    else:
        result = []
        for varBind in varBinds:
            result.append({'oid': varBind.__getitem__(0).prettyPrint(), 'value': varBind.__getitem__(1).prettyPrint()})

        print(json.dumps(result))


def main(user, md5, des, host, oid, valor):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        setCmd(
            SnmpEngine(),
            UsmUserData(user, md5, des),
            UdpTransportTarget((host, 161)),
            ContextData(),
            ObjectType(ObjectIdentity(oid), valor))
    )
    cbFun(errorIndication, errorStatus, errorIndex, varBinds)
