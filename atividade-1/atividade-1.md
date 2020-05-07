# **Atividade - Slide 3**

## CentOs - Agente
- [x] Virtualizar CentOs

### Instalação do Agente 

    dnf install net-snmp net-snmp-utils 
    
    ou 
    
    yum install net-snmp net-snmp-utils
    
- [x] Instalar Agente - SNMP

### Configuração do Agente

Arquivo de configuração

    vi /etc/snmp/snmpd.conf

Localizar sessão System Contact Information dentro do arquivo de configuração.

Inserir no arquivo através do VI algumas informações:

> sysdescr Atividade SNMP - Danilo

> syscontact Danilo Almeida <danilo.a.almeida@live.jp>

> sysname Danilo Augusto de Almeida

> syslocation Florianopolis - SC

Comando para reiniciar e verificar status

    systemctl restart snmpd
    systemctl status snmpd

Consultar MIB (Deverá retornar os dados inseridos no arquivo de configuração)
    
    snmpwalk -c public -v 2c localhost
    
Verificar status do Firewalld

    systemctl status firewalld
  
Caso ele esteja rodando, pare ele

    systemctl stop firewalld
    
Para deixar o firewalld sempre desligado e o SNMPD sempre ligado
    
    chkconfig firewalld off
    chkconfig snmpd on
    
Retorne para a configuração do agente

    vi /etc/snmp/snmpd.conf
    
Configure uma community particular
Na sessão **Controle de Acesso** *primeiro passo*

> com2sec   local   localhost   public

> com2sec   minharede   <seu_ip>192.168.122.0/24    plutao

Obs.: Descubra seu IP através do comando abaixo no terminal. Antes do '/24' fixe o valor 0 (Ex.: 192.999.999.*0*/24)
    
    ip a

No *segundo passo*

> group MyROGroup   v2c minharede

No *terceiro passo* (Permissão para ver a arvore inteira)

> view  all included    .1

No *último passo* (Aplicando o permissionamento para o nosso grupo)

> acess MyROGroup   ""  any noauth  exact   all all none

Reinicie o Agente

- [x] Configuração do Agente

## Exercicios

1. Instalar agente e utilitário:
    
    ![](../../gerencia-de-redes-atividades/atividade-1/img/001.1.png)

2. Configurar e iniciar o serviço:

    ![](../../gerencia-de-redes-atividades/atividade-1/img/002.1.png)
    
    ![](../../gerencia-de-redes-atividades/atividade-1/img/002.2.png)
    
3. Configurar community particular:

    ![](../../gerencia-de-redes-atividades/atividade-1/img/003.1.png)

4. Configurar acesso aos objetos da MIB no nível superior da árvore:

    ![](../../gerencia-de-redes-atividades/atividade-1/img/004.1.png)

5. Utilizar o comando *snmpwalk* para listar as inferfaces de rede do dispositivo:

    ![](../../gerencia-de-redes-atividades/atividade-1/img/005.1.png)
    
6. Qual o objeto da MIB representa o OID **.1.3.6.1.2.1.4.34.1.3.1.4** ?

    ![](../../gerencia-de-redes-atividades/atividade-1/img/006.1.png)

7. Verificar as MIBs disponíveis no dispositivo (/usr/share/snmp/mibs/):

    ![](../../gerencia-de-redes-atividades/atividade-1/img/007.1.png)

8. Verificar a MIB *HOST-RESOURCES-MIB*:

    ![](../../gerencia-de-redes-atividades/atividade-1/img/008.1.png)

9. Fazer consultas em objetos desta MIB:

    ![](../../gerencia-de-redes-atividades/atividade-1/img/009.1.png)

10. Buscar nas MIBs um objeto que forneça informações dobre IO (Input/Output) de disco. Você deve ter condições de a partir do *snmpget* opter o IO de Leitura e o IO de Escrita no seu disco.

    ![](../../gerencia-de-redes-atividades/atividade-1/img/010.1.png)
    
    ![](../../gerencia-de-redes-atividades/atividade-1/img/010.2.png)
    
    ![](../../gerencia-de-redes-atividades/atividade-1/img/010.3.png)
    
    ![](../../gerencia-de-redes-atividades/atividade-1/img/010.4.png)
    
    

