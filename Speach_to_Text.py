"""
    sudo apt-get install python3-pyaudio
"""
import speech_recognition as sr

class STT:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        
    def listen(self):
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
                
                print("Listening ...")
                audio = self.recognizer.listen(source, timeout=8, phrase_time_limit=8)
                print("Recognizing ...")
                text = self.recognizer.recognize_google(audio)
                text = text.lower()
                print("Recognized: ", text)
                if "clark" in text:
                    return True
                
                return text
            
            
        except Exception as e:
            return f'Error: {e}'

    
    def take_request(self):
        try:   
            with sr.Microphone() as source:
                
                audio = self.recognizer.listen(source)
                
                text = self.recognizer.recognize_google(audio)
                text = text.lower()
                
                return text
            
            
        except Exception as e:
            return f'Error: {str(e)}'

  

if __name__ == "__main__":
    stt = STT()
    
    while True:        
        if stt.listen() == True:
            print(stt.take_request())