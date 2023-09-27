"""
    
    Chatterbot is a free, opensource chat bot
    Needs to be trained on a dataset to be useful
"""
from chatterbot import ChatBot

class ChatController:
    def __init__(self):
        self.chatbot = ChatBot("Clark")

    def prompt(self, prompt:str):
        response = self.chatbot.get_response(prompt)
        
        return response
    


