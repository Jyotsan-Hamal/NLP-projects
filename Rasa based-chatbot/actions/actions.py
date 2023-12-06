
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List

class ExtractFoodEntity(Action):

    def name(self) -> Text:
        return "action_extract_food_entity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        food_entity = next(tracker.get_latest_entity_values('food'),None)
        if food_entity:
            dispatcher.utter_message(text= f"You have selected {food_entity} as food choice.")
        else:
            dispatcher.utter_message(text="Sorry i couldn't detect the food choice")
        return []


