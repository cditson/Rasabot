## Sample Stories
* greet
    - utter_greet
* reset
    - reset_account
* bye
    - utter_bye

## Generated Story 5417482134897117873
* greet
    - utter_greet
* reset{"application": "jabber", "username": "jk1234"}
    - slot{"application": "jabber"}
    - slot{"username": "jk1234"}
    - reset_account
    - slot{"application": "jabber"}
    - slot{"username": "jk1234"}
* greet
    - utter_bye

## Generated Story -8492819318233501221
* greet
    - utter_greet
* reset{"application": "servicenow"}
    - slot{"application": "servicenow"}
    - utter_ask_username
* reset{"username": "jana1234"}
    - slot{"username": "jana1234"}
    - reset_account
    - slot{"application": "servicenow"}
    - slot{"username": "jana1234"}
* greet
    - utter_greet

## Generated Story 6057254937780284082
* greet
    - utter_greet
* reset{"application": "sametime"}
    - slot{"application": "sametime"}
    - utter_ask_username
* reset{"username": "jana1234"}
    - slot{"username": "jana1234"}
    - reset_account
    - slot{"application": "sametime"}
    - slot{"username": "jana1234"}
* bye
    - utter_bye


