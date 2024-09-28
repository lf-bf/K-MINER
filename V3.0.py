import PySimpleGUI as sg
import subprocess
import json
import sys
from funcer import err
miner = None
valores2 = None
flag = True


# Comando da taskbar
if sys.platform.startswith('win'):
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u'CompanyName.ProductName.SubProduct.VersionInformati'
                                                                  u'on')

# carregando dados


def js():
    data2 = open("data.json", "r")
    output = data2.read()
    dic = json.loads(output)
    data2.close()

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


# função de salvamento de dados json
def save():
    data = open("data.json", "w+")
    json.dump(valores, data)
    data.close()


# geranado a interface
sg.theme("DarkAmber")

layout = [
    [],
    [sg.Text('Selecione o minerador desejado:', size=(20, 2), font='Lucida', justification='left')],
    [sg.Combo(['T-Rex', 'LolMiner'], key='c1')],
    [sg.Text('Selecione o algoritmo desejado desejado:', size=(20, 2), font='Lucida', justification='left')],
    [sg.Combo(['Ethash', 'Kawpow', 'Etchash', 'Firopow', 'Octopus', 'Autolykos2', 'Cuckoo',
               'Beamhash'], key='c2')],
    [sg.Text('Selecione uma moeda:', size=(20, 1), font='Lucida', justification='left')],
    [sg.Combo(['Ethereum', 'Ethereum Classic', 'Bitcoin', 'Ravencoin', 'Dogecoin',
               'Ergo', 'Cortex', 'Zcoin', 'Beam', 'Callisto', 'Expanse'], key='c3')],
    [sg.Text('Insira o servidor desejado:', size=(20, 2), font='Lucida', justification='left')],
    [sg.Input(key='server')],
    [sg.Text('Insira a sua carteira:', size=(20, 1), font='Lucida', justification='left')],
    [sg.Input(key='wallet')],
    [sg.Text('Insira o nome do seu minerador:', size=(20, 2), font='Lucida', justification='left')],
    [sg.Input(key='miner')],
    [sg.Button('Salvar', font=('Lucida', 12), key='botao'), sg.Text('*TODOS OS CAMPOS DEVEM SER PREECHIDOS!',
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

#  editando o arquivo bat
if valores['c1'] == 'T-Rex':

    valores['c2'].lower()
    with open('trex.bat', 'w+') as myBat:
        myBat.write(r'''C:\Users\lffon\Desktop\Trex\t-rex.exe -a {0} -o {1} -u {2}.{3} -p x
     pause '''.format(valores['c2'], valores['server'], valores['wallet'], valores['miner']))

    miner = 'trex.bat'

elif valores['c1'] == 'LolMiner':
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
    with open('lolminer.bat', 'w+') as myBat:
        myBat.write(r'''C:\Users\lffon\Desktop\1.42\lolMiner.exe --algo {0} --pool {1} --user {2}.{3} --tls 0'''.format
                    (valores2, valores['server'], valores['wallet'], valores['miner']))

    miner = 'lolminer.bat'

# abertura do minerador
subprocess.Popen("start {}".format(miner), shell=True)





