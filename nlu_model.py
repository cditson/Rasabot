from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer,Interpreter,Metadata
from config import getData
import json

def train_nlu(data,spacy_config,model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load(spacy_config))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir,fixed_model_name=getData()["model_name"])

    
if __name__== '__main__':
    train_nlu(getData()["data"],getData()["config_spacy"],getData()["model_directory"])