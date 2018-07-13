from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput

from config import getData

nlu_interpreter = RasaNLUInterpreter(getData()["model_directory"] +   '/default/' + getData()["model_name"])
agent = Agent.load(getData()["dialogue"],interpreter= nlu_interpreter)
input_channel = SlackInput(getData()["slack"]["oauth_access_token"],
    getData()["slack"]["user_oauth_access_token"],
    getData()["slack"]["verification_token"],True)

agent.handle_channel(HttpInputChannel(5004,'/',input_channel))