import json

def saveItem(items):
    with open("/app/data/Itens.json", "w") as file:
        file.writelines(json.dumps(items))

def loadItems():
    with open("/app/data/Itens.json", "r") as file:
        return json.loads(file.read())       
