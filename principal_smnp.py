from configparser import ConfigParser
from sys import argv
from traceback import format_exc
from controller.controle_log import ControleLog
from os.path import join, dirname
from scripts import snmpget, snmpset, volume_particao

aplicacao, comando = argv[0], argv[1]
log = ControleLog(join(dirname(aplicacao), 'log'), True)
cfg = ConfigParser()


def group_mib(opcao):
    group_mib_get = {
        'System': {
            'sysContact': {'oid': '.1.3.6.1.2.1.1.4.0', 'descricao': 'Contato'},
            'sysName': {'oid': '.1.3.6.1.2.1.1.5.0', 'descricao': 'Nome do Host'},
            'sysLocation': {'oid': '.1.3.6.1.2.1.1.6.0', 'descricao': 'Localizacao do Host'}
        },
        'Interface': {
            'ifDescr':
                {'oid': '.1.3.6.1.2.1.2.2.1.2.2', 'descricao': 'Nome da interface'},
            'ifType':
                {'oid': '.1.3.6.1.2.1.2.2.1.3.2', 'descricao': 'Tipo da interface'},
            'ifSpeed':
                {'oid': '.1.3.6.1.2.1.2.2.1.4.2', 'descricao': 'Medidor da velocidade da interface em bits por segundo'}
        },
        'Hardware': {
            '': {'oid': '', 'descricao': ''},
            '': {'oid': '', 'descricao': ''},
            '': {'oid': '', 'descricao': ''}
        },
        'Software': {
            'hrSystemUptime':
                {'oid': '.1.3.6.1.2.1.25.1.1.0', 'descricao': 'Tempo desde a ultima vez que este host foi inicializado'},
            'hrSystemDate':
                {'oid': '.1.3.6.1.2.1.25.1.2.0', 'descricao': 'A noção do HOST da data e hora locais do dia'},
            'hrMemorySize':
                {'oid': '.1.3.6.1.2.1.25.2.2.0', 'descricao': 'Quantidade de memoria RAM'},
        },
    }
    group_mib_set = {
        'System': {
            'sysContact': {'oid': '.1.3.6.1.2.1.1.4.0', 'descricao': 'Contato'},
            'sysName': {'oid': '.1.3.6.1.2.1.1.5.0', 'descricao': 'Nome do Host'},
            'sysLocation': {'oid': '.1.3.6.1.2.1.1.6.0', 'descricao': 'Localizacao do Host'}
        }
    }
    if opcao == 'get':
        for grupo, objeto in group_mib_get.items():
            log.info(f'{grupo:-^81}')
            for key, value in objeto.items():
                log.info(f'Objeto: {key}')
                log.info(f'OID: {objeto[key]["oid"]}')
                log.info(f'Descricao: {objeto[key]["descricao"]}')
                log.info(f'{"":~^81}')
    elif opcao == 'set':
        for grupo, objeto in group_mib_set.items():
            log.info(f'{grupo:-^81}')
            for key, value in objeto.items():
                log.info(f'Objeto: {key}')
                log.info(f'OID: {objeto[key]["oid"]}')
                log.info(f'Descricao: {objeto[key]["descricao"]}')
                log.info(f'{"":~^81}')


try:
    log.cabecalho()

    if len(argv) == 2 and aplicacao == 'principal_smnp.py' and comando == 'get':
        group_mib(comando)
        community = input("Informe a community: ")
        user = input("Informe o USER: ")
        md5 = input("Informe a MD5: ")
        des = input("Informe a DES: ")
        host = input("Informe o IP do Host: ")
        oid = input("Informe o OID que deseja consultar: ")
        # community = 'plutao'
        # user = 'daniloa'
        # md5 = 'dean2020'
        # des = 'sistemas'
        # host = '192.168.0.7'
        # oid = '.1.3.6.1.2.1.1.4.0'

        snmpget.main(user, md5, des, host, oid)

    elif len(argv) == 2 and aplicacao == 'principal_smnp.py' and comando == 'set':
        group_mib(comando)
        # community = input("Informe a community: ")
        user = input("Informe o USER: ")
        md5 = input("Informe a MD5: ")
        des = input("Informe a DES: ")
        host = input("Informe o IP do Host: ")
        oid = input("Informe o OID que deseja consultar: ")
        valor = input("Insira o novo valor: ")
        # community = 'plutao'
        # user = 'daniloa'
        # md5 = 'dean2020'
        # des = 'sistemas'
        # host = '192.168.0.7'
        # oid = '.1.3.6.1.2.1.1.4.0'
        snmpset.main(user, md5, des, host, oid, valor)

    elif len(argv) == 2 and aplicacao == 'principal_smnp.py' and comando == 'av1-rec':
        community = input("Informe a community: ")
        host = input("Informe o IP do Host: ")
        # community = 'plutao'
        # host = '192.168.0.7'
        volume_particao.main(community, host)

    else:
        cfg.read(join(dirname(aplicacao), 'cfg', 'ajuda.cfg'))
        log.info(cfg.get('Ajuda', 'uso'))

except BaseException:
    mensagem = format_exc()
    log.error(mensagem)

finally:
    log.rodape()
