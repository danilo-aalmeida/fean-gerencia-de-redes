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
            json.dumps(resultados)
            # for resultado in resultados.items():
                # print(resultado)
            # print(varBind)
            print(' = '.join([x.prettyPrint() for x in varBind]))


def _buscar_particao(community, host):
    snmpEngine = SnmpEngine()
    nextCmd(snmpEngine, CommunityData(community), UdpTransportTarget((host, 161)), ContextData(),
            ObjectType(ObjectIdentity('.1.3.6.1.4.1.2021.13.15.1.1.2')), cbFun=cbFun)
    snmpEngine.transportDispatcher.runDispatcher()
    particao = input('Informe numericamente a particao que deseja visualizar: ')
    return particao


def cbFun2(snmpEngine, sendRequestHandle, errorIndication, errorStatus, errorIndex, varBinds, cbCtx):
    if errorIndication:
        print(errorIndication)
        return
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBindTable[-1][int(errorIndex) - 1][0] or '?'))
        return
    else:
        for varBind in varBinds:
            valor = varBind.__getitem__(1).prettyPrint()
            tamanho = int(valor) * 1024
            print(f'{tamanho}GB')


def _calcular_tamanho(community, host, particao):
    snmpEngine = SnmpEngine()
    getCmd(snmpEngine, CommunityData(community), UdpTransportTarget((host, 161)), ContextData(),
           ObjectType(ObjectIdentity(f'.1.3.6.1.4.1.2021.13.15.1.1.2.{particao}')), cbFun=cbFun2)
    snmpEngine.transportDispatcher.runDispatcher()


def main(community, host):
    particao = _buscar_particao(community, host)
    _calcular_tamanho(community, host, particao)
