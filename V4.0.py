import PySimpleGUI as sg
import subprocess
import json
import sys
import os
from funcer import err
miner = None
flag = True

# Comando da taskbar
if sys.platform.startswith('win'):
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u'CompanyName.ProductName.SubProduct.VersionInformati'
                                                                  u'on')


def trex():
    user = os.getlogin()
    valores['c2'].lower()
    with open(f'trex.bat', 'w+') as myBat:
        myBat.write(fr'''C:\Users\{user}\Desktop\Trex\t-rex.exe -a {valores['c2']} -o {valores['server']} -u {valores['wallet']}.{valores['miner']} -p x
        pause ''')
    return subprocess.Popen("start {}".format('trex.bat'), shell=True)


def lol_miner():
    valores2 = None
    user = os.getlogin()
    if valores['c2'] == 'Ethash':
        valores2 = 'ETHASH'
    elif valores['c2'] == 'Etchash':
        valores2 = 'ETCHASH'
    elif valores['c2'] == 'Beamhash':
        valores2 = 'BEAM-I'
    elif valores['c2'] == 'Autolykos2':
        valores2 = 'AUTOLYKOS2'
    elif valores['c2'] == 'Cuckoo':
        valores2 = 'C29AE'
    with open(f'lolminer.bat', 'w+') as myBat:
        myBat.write(fr'''C:\Users\{user}\Desktop\1.42\lolMiner.exe -a {valores2} -o {valores['server']} -u {valores['wallet']}.{valores['miner']} -p x
        pause ''')
    return subprocess.Popen("start {}".format('lolminer.bat'), shell=True)

# carregando dados


def js():
    with open("data.json", "r") as jsn1:
        output = jsn1.read()
        dic = json.loads(output)
    if dic['checkbox'] is True:

        try:
            janela['c1'].update(dic['c1'])
            janela['c2'].update(dic['c2'])
            janela['c3'].update(dic['c3'])
            janela['server'].update(dic['server'])
            janela['wallet'].update(dic['wallet'])
            janela['miner'].update(dic['miner'])
        except TypeError:
            err()
        else:
            janela['c1'].update(dic['c1'])
            janela['c2'].update(dic['c2'])
            janela['c3'].update(dic['c3'])
            janela['server'].update(dic['server'])
            janela['wallet'].update(dic['wallet'])
            janela['miner'].update(dic['miner'])
    else:
        pass

# função de salvamento de dados json


def save():
    data = open("data.json", "w+")
    json.dump(valores, data)
    data.close()

# funcao de escolha


def choice():
    item = valores[acoes]
    title_list = [i["name"] for i in dic2[item]]
    janela['c2'].update(value=title_list[0], values=title_list)


with open('config.json', 'r') as jsn:
    output2 = jsn.read()
    dic2 = json.loads(output2)


# geranado a interface
sg.theme("DarkAmber")

layout = [
    [],
    [sg.Text('Selecione o minerador desejado:', size=(20, 2), font='Lucida', justification='left')],
    [sg.Combo(list(dic2.keys()), enable_events=True, key='c1')],
    [sg.Text('Selecione o algoritmo desejado desejado:', size=(20, 2), font='Lucida', justification='left')],
    [sg.Combo([], size=(15, 0), key='c2')],
    [sg.Text('Selecione uma moeda:', size=(20, 1), font='Lucida', justification='left')],
    [sg.Combo(['Ethereum', 'Ethereum Classic', 'Bitcoin', 'Ravencoin', 'Dogecoin',
               'Ergo', 'Cortex', 'Zcoin', 'Beam', 'Callisto', 'Expanse'], size=(15,0), key='c3')],
    [sg.Text('Insira o servidor desejado:', size=(20, 1), font='Lucida', justification='left')],
    [sg.Input(key='server')],
    [sg.Text('Insira a sua carteira:', size=(20, 1), font='Lucida', justification='left')],
    [sg.Input(key='wallet')],
    [sg.Text('Insira o nome do seu minerador:', size=(30, 1), font='Lucida', justification='left')],
    [sg.Input(key='miner')],
    [sg.Button('Rodar', font=('Lucida', 12), key='botao'), sg.Checkbox('Deseja salvar todas as configurações?', font= 'Lucida, 10', key= 'checkbox')],
    [sg.Text('*TODOS OS CAMPOS DEVEM SER PREECHIDOS!',
             size=(40, 1), font='Lucida, 8', text_color='Red', key='text', visible=False)]
]
janela = sg.Window('K-Miner', layout, icon=r'K4.ico', finalize=True)

# carregando dados fase 2
js()

# verificaçao de valores e inserção do programa no loop
while flag is True:
    acoes, valores = janela.read(timeout=10)
    if acoes == sg.WINDOW_CLOSED:
        exit()
    elif acoes == 'c1':
        choice()
    elif acoes == 'botao':
        flag = False
    elif valores['miner'] == '':
        janela['botao'].update(disabled=True)
        janela['text'].update(visible=True)
    elif valores['miner'] != '':
        janela['botao'].update(disabled=False)
        janela['text'].update(visible=False)
janela.close()

# salvando dados
save()

# execuçao
if valores['c1'] == 'T-Rex':
    trex()
elif valores['c1'] == 'Lolminer':
    lol_miner()

