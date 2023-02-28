from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import math

class ActionPerformOperation(Action):

    def name(self) -> Text:
        return "action_perform_operation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        operation = tracker.get_slot("operation")
        number1 = tracker.get_slot("number1")
        number2 = tracker.get_slot("number2")

        if operation == "add":
            result = float(number1) + float(number2)
        elif operation == "subtract":
            result = float(number1) - float(number2)
        elif operation == "multiply":
            result = float(number1) * float(number2)
        elif operation == "divide":
            result = float(number1) / float(number2)
        elif operation == "power":
            result = float(number1) ** float(number2)
        elif operation == "square_root":
            result = math.sqrt(float(number1))

        dispatcher.utter_message(text=f"The result is {result}")

        return []
