from __future__ import absolute_import,division,unicode_literals

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

from config import getData

if __name__ == '__main__':
    utils.configure_colored_logging(loglevel='INFO')

    domain = getData()["domain"]
    stories = getData()["stories"]
    dialogue=getData()["dialogue"]

    agent = Agent(domain,policies=[MemoizationPolicy(max_history=2)
    ,KerasPolicy()])

    training_data = agent.load_data(stories)
    agent.train(training_data,
            epochs=400,
            batch_size=100,
            validation_split=0.2
    )
    agent.persist(dialogue)
