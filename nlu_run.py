
from rasa_nlu import config
from rasa_nlu.model import Interpreter
import json
import sys
from config import getData

def run_nlu(model,spacy_config):
    interpreter= Interpreter.load(model) #, config.load(spacy_config))
    result = interpreter.parse(sys.argv[1])
    print(json.dumps(result,indent=4,sort_keys=True))

if __name__== '__main__':
    #train_nlu('./data/data.json','./config_spacy.json','./models/nlu')
    run_nlu(getData()["model_directory"]+ '/default/' + getData()["model_name"],getData()["config_spacy"])