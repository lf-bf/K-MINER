import json

dic = {"c1": "", "c2": "", "c3": "", "server": "", "wallet": "", "miner": "", "checkbox": ""}

# sobreescreve o arquivo json


def err():

    erro = open("data.json", "w+")
    json.dump(dic, erro)
    erro.close()
