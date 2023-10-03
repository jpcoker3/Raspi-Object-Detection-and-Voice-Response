"""
    sudo apt-get install python3-pyaudio
"""
import speech_recognition as sr
import sounddevice

class STT:
    def __init__(self, _display):
        #initialize recognizer
        self.recognizer = sr.Recognizer()
        #set display
        self.display = _display
        
    def listen(self):
        try:
            #try to listen for 8 seconds
            with sr.Microphone() as source:
                #adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
                #print current state
                self.display.write_to_second_line("Listening ...")
                print("Listening ...")
                #listen for audio
                audio = self.recognizer.listen(source, timeout=8, phrase_time_limit=8)
                
                #print current state
                self.display.write_to_second_line("Recognizing ...")
                print("Recognizing ...")
                
                #voice to text
                text = self.recognizer.recognize_google(audio)
                text = text.lower() #for normalization
                
                #display current state
                self.display.write_to_second_line("Recognized ...")
                print("Recognized: ", text)
                
                #return text
                return text
            
        #grab all exceptions as error
        except Exception as e:
            return f'Error: could not hear'

    
    def take_request(self):
        try:
            with sr.Microphone() as source:
                #same as above, adjust for noise
                self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
                
                #print current state
                print("Listening for request...")
                self.display.write_to_second_line("Listening ...")
                
                #listen for audio
                audio = self.recognizer.listen(source, timeout=8, phrase_time_limit=8)
                #recognize request
                print("Recognizing request ...")
                self.display.write_to_second_line("Recognizing ...")
                #voice to text
                text = self.recognizer.recognize_google(audio)
                text = text.lower() # normalize
                #print current state
                self.display.write_to_second_line("Recognized ...")
                print("Recognized: ", text)
                
                
                return text
            
            
        except Exception as e:
            return f'Error: could not hear'

  

if __name__ == "__main__":
    #testing. listen and output result
    stt = STT()
    
    while True:
        print(stt.listen())        
        if stt.listen() == True:
            print(stt.take_request())