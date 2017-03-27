# redes2
#Devido a formatação do GIT, recomento leitura no DOC entregue via UNIFOR ONLINE#
Universidade de Fortaleza - UNIFOR
Trabalho referente a cadeira de redes II
Professor: Bruno Lopes
Aluno: Rafael Carvalho - 1410801
Linguagem de programação: Python 3.4
Instruções de compilação: (Ter python3.4 instalado na máquina)
  1-Baixar ou clonar repositorio em uma mesmo diretorio
  2-Em 'App': 
            2.1-Rodar ServerApp.py
            2.2-Rodar clients(Rafa.py, Jorge.py, Amanda.py)
            2.3-Se desejar mais clients, basta criar uma nova classe .py em 'App' e copiar o codigo de
                qualquer um dos outros clients, alterando apenas o parametro nick para um novo nick.
  
  P.S: Funcionalidade de mensagem privada:
        -Para enviar mensagem privada de Rafa para Amanda, digitar no client de Rafa /d/Amanda&tilde;MENSAGEM AQUI
        -Ou seja, /d/ é o comando de mensagem privada, seguido do nick do destinatario e um '&tilde;'

Funcionalidades opcionais:
  -GUI Servidor, classe ServerTCP.py
  -GUI Cliente, classe ClientTCP.py
  -Envio de bytes no protocolo de comunicação, classe ProtocolPacker.py
