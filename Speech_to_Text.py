"""
    sudo apt-get install python3-pyaudio
"""
import speech_recognition as sr
import sounddevice

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
                
                
                return text
            
            
        except Exception as e:
            return f'Error: {e}'

    
    def take_request(self):
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
                
                print("Listening for request...")
                audio = self.recognizer.listen(source, timeout=8, phrase_time_limit=8)
                print("Recognizing request ...")
                text = self.recognizer.recognize_google(audio)
                text = text.lower()
                print("Recognized: ", text)
                
                return text
            
            
        except Exception as e:
            return f'Error: {e}'

  

if __name__ == "__main__":
    stt = STT()
    
    while True:
        print(stt.listen())        
        if stt.listen() == True:
            print(stt.take_request())