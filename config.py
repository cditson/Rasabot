import json

def getData():
    with open('./config.json',encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    
    return data