from sys import argv
from traceback import format_exc
from controller.controle_log import ControleLog
from os.path import join, dirname
from scripts import snmpget, snmpset

aplicacao, comando = argv[0], argv[1]
log = ControleLog(join(dirname(aplicacao), 'log'), True)
group_mib = {
    'Grupo System': {
        'sysDescr':  '1.3.6.1.2.1.1.1',
        'sysUpTime': '1.3.6.1.2.1.1.3',
        'sysContact': '1.3.6.1.2.1.1.4'
    },
    'Grupo Interface': {
        'ifNumber': '1.3.6.1.2.1.2.1',
        'ifOperStatus': '1.3.6.1.2.1.2.2.1.8',
        'ifInOctets': '1.3.6.1.2.1.2.2.1.10'
    }
}
try:
    log.cabecalho()
    for grupo, valor in group_mib.items():
        log.info(grupo)
        log.info(f'Objeto -> ID')
        for objeto, oid in valor.items():
            log.info(f'{objeto} -> {oid}')

    if len(argv) == 2 and aplicacao == 'principal_smnp.py' and comando == 'get':
        community = input("Informe a community: ")
        host = input("Informe o IP do Host: ")
        oid = input("Informe o OID que deseja consultar: ")
        snmpget.main(community, host, oid)

    if len(argv) == 2 and aplicacao == 'principal_smnp.py' and comando == 'set':
        community = input("Informe a community: ")
        host = input("Informe o IP do Host: ")
        oid = input("Informe o OID que deseja consultar: ")
        valor = input("Informe o novo valor que deseja atribuir: ")
        snmpset.main(community, host, oid, valor)

except BaseException:
    mensagem = format_exc()
    log.error(mensagem)

finally:
    log.rodape()
