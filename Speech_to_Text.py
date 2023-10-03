"""
    sudo apt-get install python3-pyaudio
"""
import speech_recognition as sr
import sounddevice

class STT:
    def __init__(self, _display):
        self.recognizer = sr.Recognizer()
        self.display = _display
        
    def listen(self):
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
                self.display.write_to_second_line("Listening ...")
                print("Listening ...")
                audio = self.recognizer.listen(source, timeout=8, phrase_time_limit=8)
                
                self.display.write_to_second_line("Recognizing ...")

                print("Recognizing ...")
                text = self.recognizer.recognize_google(audio)
                text = text.lower()
                
                self.display.write_to_second_line("Recognized ...")

                print("Recognized: ", text)
                
                
                return text
            
            
        except Exception as e:
            return f'Error: {e}'

    
    def take_request(self):
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
                
                print("Listening for request...")
                self.display.write_to_second_line("Listening ...")
                audio = self.recognizer.listen(source, timeout=8, phrase_time_limit=8)
                print("Recognizing request ...")
                self.display.write_to_second_line("Recognizing ...")
                text = self.recognizer.recognize_google(audio)
                text = text.lower()
                self.display.write_to_second_line("Recognized ...")
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