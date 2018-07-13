from __future__ import absolute_import,division,print_function,unicode_literals

from rasa_core import utils

from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter

from config import getData


def train_dialogue(): #domain_file,model_path,training_data_file):
    utils.configure_colored_logging(loglevel='INFO')
 
    agent = Agent(getData()["domain"],policies=[MemoizationPolicy(max_history=2)
    ,KerasPolicy()])

    training_data = agent.load_data(getData()["stories"])
    agent.train(training_data,
            epochs=400,
            batch_size=100,
            validation_split=0.2
    )
    agent.persist(getData()["dialogue"])
    return agent

def run_weather_bot(serve_forever=True):
    interpreter = RasaNLUInterpreter(getData()["model_directory"] + '/default/' + getData()["model_name"])
    agent = Agent.load(getData()["dialogue"],interpreter=interpreter)

    if serve_forever==True:
        agent.handle_channel(ConsoleInputChannel())

    return agent

if __name__ == '__main__':
    train_dialogue()
    run_weather_bot()