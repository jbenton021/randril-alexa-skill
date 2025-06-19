from ask_adk_core.skill_builder import SkillBuilder

import os
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard

from atproto import Client
from atproto.exceptions import AtProtocolError
from dotenv import load_dotenv

from dril_search import search_dril_posts

from ask_sdk_core.dispatch_components import AbstractExceptionHandler



class LaunchRequestHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        return is_request_type("LaunchRequest")(handler_input)
    
    def handle(self, handler_input):
        load_dotenv()

        speech_text = "Welcome to the Alexa Skills Kit, you can say hello!"
        
        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Dril Search", speech_text)).set_should_end_session(end_session)
        
        return handler_input.response_builder.response

class DrilSearchIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        return is_intent_name("HelloWorldIntent")(handler_input)
    
    def handle(self, handler_input):
        speech_text = "Hello World"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Dril Search", speech_text)).set_should_end_session(
                True
            )
        
        return handler_input.response_builder.response
    
class HelpIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        speech_text = "You can say hello to me!"

        handler_input.response_builder.speak(speech_text).ask(speech_text).set_card(
            SimpleCard("Dril Search", speech_text))
        return handler_input.response_builder.response
    
class CancelAndStopIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.CancelIntent")(handler_input) or is_intent_name("AMAZON.StopIntent")(handler_input)
    
    def handle(self, handler_input):
        speech_text = "Goodbye!"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Dril Search", speech_text)).set_should_end_session(True)
        
        return handler_input.response_builder

class SessionEndedRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        return handler_input.response_builder.response

class AllExceptionHandler(AbstractExceptionHandler):

    def can_handle(self, handler_input, exception):
        return True
    
    def handle(self, handler_input, exception):
        print(exception)

        speech = "Sorry, I didn't get it. Can you please say it again!!"
        handler_input.response_builder.speak(speech).ask(speech)
        return handler_input.response_builder.response

sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(DrilSearchIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelAndStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

sb.add_exception_handler(AllExceptionHandler())

handler = sb.lambda_handler()