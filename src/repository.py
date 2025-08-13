import json

def saveItem(items):
    with open("/home/luiz/itens.json", "w") as file:
        file.writelines(json.dumps(items))

def loadItems():
    with open("/home/luiz/itens.json", "r") as file:
        return json.loads(file.read())       