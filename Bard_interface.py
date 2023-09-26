"""
    
    pip install bardapi
    
    
    Bard was chosen over an OpenAi model because it is free and has a higher character limit.
    
"""
from bardapi import Bard
import os
from config import bard_api_key, second_bard_api_key
import requests

class BardController:
    def __init__(self):
        os.environ["_BARD_API_KEY"] = bard_api_key
        
        self.session = requests.Session()
        self.session.headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
        }
        
        #these keys are retrieved from "inspect element" on bard.google.com
        self.session.cookies.set("__Secure-1PSID", bard_api_key) 
        self.session.cookies.set("__Secure-1PSIDTS",second_bard_api_key )
        
        self.bard = Bard(session=self.session, timeout=30)
        
    def prompt(self, prompt:str):
        response = self.bard.get_answer(prompt)['content']
        
        return response
    


#test GPT

if __name__ == "__main__":
    bard = BardController()
    print(bard.prompt("Hello, how are you?"))