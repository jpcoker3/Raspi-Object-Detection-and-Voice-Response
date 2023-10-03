"""
    
    Chatterbot is a free, opensource chat bot
    Needs to be trained on a dataset to be useful
"""
from chatterbot import ChatBot
import google_search
from chatterbot.trainers import ChatterBotCorpusTrainer
import sys



class ChatController:
    def __init__(self):
        #set bot with name of clark
        self.chatbot = ChatBot("Clark")
        
        #train the bot
        self.trainer = ChatterBotCorpusTrainer(self.chatbot)
        self.trainer.train(
            "chatterbot.corpus.english"
        )
        

    def prompt(self, prompt:str):
        
        #exit does not work
        if prompt == "quit":
            sys.exit()

        """
        #Not working as expected. leaving out for now.
        question_words = ['what', "why"]
        for word in question_words:
            if word in prompt:
                #this does not return the intended result unfornately. researching other solutions ...
                response = google_search.top_description(prompt)
                return response
        """
        #else, get response from bot
        response = self.chatbot.get_response(prompt)
        
        return response
    


