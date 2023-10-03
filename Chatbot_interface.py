"""
    
    Chatterbot is a free, opensource chat bot
    Needs to be trained on a dataset to be useful
"""
from chatterbot import ChatBot
import google_search
from chatterbot.trainers import ChatterBotCorpusTrainer



class ChatController:
    def __init__(self):
        self.chatbot = ChatBot("Clark")
        
        self.trainer = ChatterBotCorpusTrainer(self.chatbot)

        self.trainer.train(
            "chatterbot.corpus.english"
        )
        

    def prompt(self, prompt:str):
        if prompt == "quit":
            exit()

        question_words = ['what', "why"]
        for word in question_words:
            if word in prompt:
                response = google_search.top_description(prompt)
                return response
        response = self.chatbot.get_response(prompt)
                

            
        
        return response
    


