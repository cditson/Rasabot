from __future__ import absolute_import,division,print_function,unicode_literals

from rasa_core import utils

from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter

from config import getData

def run_weather_online(input_channel,interpreter,
            domain_file,training_data_file):
    agent = Agent(domain_file,policies=[MemoizationPolicy(max_history=3),KerasPolicy()],
                interpreter=interpreter)

    training_data = agent.load_data(training_data_file)

    agent.train_online(training_data
            ,input_channel=input_channel,
            epochs=400,
            batch_size=100,
            validation_split=0.2)

if __name__ == '__main__':
    utils.configure_colored_logging(loglevel='INFO')
    nlu_interpretter = RasaNLUInterpreter(getData()["model_directory"] + '/default/' + getData()["model_name"] )

    run_weather_online(ConsoleInputChannel(),nlu_interpretter,
            getData()["domain"],getData()["stories"])