# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []
class ActionConfirmOrder(Action):
    def name(self):
        return "action_confirm_order"

    def run(self, dispatcher, tracker, domain):
        # Extract the slot values
        meat_type = tracker.get_slot('meat_type')
        quantity = tracker.get_slot('quantity')
        location = tracker.get_slot('location')

        # Generate the confirmation message
        confirmation_message = f"You asked for {quantity} of {meat_type} which is to be delivered at {location}. Am I right?"

        # Send the confirmation message
        dispatcher.utter_message(confirmation_message)

        # Return a FollowupAction to ask the user to confirm the order
        return [FollowupAction("action_ask_confirm")]
    
    
    
class ActionAskConfirm(Action):
    def name(self):
        return "action_ask_confirm"

    def run(self, dispatcher, tracker, domain):
        # Get the latest message from the user
        latest_message = tracker.latest_message.get('text')

        # Check if the user confirmed the order
        if 'yes' in latest_message.lower():
            # The user confirmed the order, so you can proceed with placing the order
            return [FollowupAction("action_place_order")]
        else:
            # The user didn't confirm the order, so you need to ask for the order details again
            return [FollowupAction("action_ask_order_details")]