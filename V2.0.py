from PySimpleGUI import PySimpleGUI as sg
import subprocess
import json

miner = None
valores2 = None

# carregando dados
data2 = open("data.json", "r")

if data2 != 'Null':
    output = data2.read()
    print(output)
    dic = json.loads(output)
    print(dic)
    data2.close()
# geranado a interface
sg.theme("DarkAmber")

layout = [
    [],
    [sg.Text('Selecione o minerador desejado:', size=(20, 2), font='Lucida', justification='left')],
    [sg.Combo(['T-Rex', 'LolMiner'], key='c1')],
    [sg.Text('Selecione o algoritmo desejado desejado:', size=(20, 2), font='Lucida', justification='left')],
    [sg.Combo(['Ethash', 'Kawpow', 'Ecthash', 'Firopow', 'Octopus', 'Autolykos2', 'Cuckoo',
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
    [sg.Button('Salvar', font=('Lucida', 12), key='botao'), sg.Text('*TODOS OS CAMPOS DEVEM SER PREECHIDOS!', size=(40, 1),
                                                       font='Lucida, 8', text_color='Red', key='text')]
]

janela = sg.Window('K-Miner', layout, finalize=True)

# substituiçao de valores
janela['c1'].update(dic['c1'])
janela['c2'].update(dic['c2'])
janela['c3'].update(dic['c3'])
janela['server'].update(dic['server'])
janela['wallet'].update(dic['wallet'])
janela['miner'].update(dic['miner'])
acoes, valores = janela.read()

janela.close()

# salvando dados
if valores['c1'] and valores['c2'] and valores['server'] and valores['wallet'] and valores['miner'] != '':

    data = open("data.json", "w+")
    json.dump(valores, data)
    data.close()

# editando o arquivo bat
if valores['c1'] == 'T-Rex':

    valores['c2'].lower()

    myBat = open('trex.bat', 'w+')
    myBat.write(r'''C:\Users\lffon\Desktop\Trex\t-rex.exe -a {0} -o {1} -u {2}.{3} -p x
     pause '''.format(valores['c2'], valores['server'], valores['wallet'], valores['miner']))
    myBat.close()
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

    myBat = open('lolminer.bat', 'w+')
    myBat.write(r'''C:\Users\lffon\Desktop\1.42\lolMiner.exe --algo {0} --pool {1} --user {2}.{3} --tls 0'''.format(valores2, valores['server'], valores['wallet'], valores['miner']))
    myBat.close()

    miner = 'lolminer.bat'
# abertura do minerador

subprocess.Popen("start {}".format(miner), shell=True)




