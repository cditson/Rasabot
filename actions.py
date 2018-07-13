from __future__ import absolute_import, division, unicode_literals
from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

class ResetAccount(Action):
    def name(self):
        return 'reset_account'
    
    def run(self,dispatcher,tracker,domain):
        application = tracker.get_slot('application')
        username = tracker.get_slot('username')

        ## Invoke API to reset based on the application.
        password  = "abc123"

        response = """ Your password has been reset. New password is {}. 
                Please change password once you login """.format(password)
        dispatcher.utter_message(response)

        return [SlotSet('application',application),SlotSet('username',username)]