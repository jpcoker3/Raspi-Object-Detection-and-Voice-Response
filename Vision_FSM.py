import random
from Speech_to_Text import STT
from Chatbot_interface import ChatController
import threading

class States:
    Search = "search"
    Found = "found"
    Phone = "phone"
    Lost = "lost"

class VisionState:
    def __init__(self, _voice, _display):
        self.voice = _voice
        self.current_state = States.Search
        self.transition_request = []
        self.speech_to_text = STT(_display)
        self.bot = ChatController()
        self.listen_thread = None
        self.stop_listen_thread = threading.Event()  # Event to signal the listen_thread to stop
        self.display = _display

        self.voicelines = {
            "search": [],
            "found": [],
            "phone": ["Get off your phone!", "Put your phone away!", "Stop using your phone!", "Stop using your phone Joe!"],
            "lost": []
        }

    def request_transition(self, new_state, type=""):
        print(self.transition_request)
        if self.transition_request == []:
            self.transition_request.append(new_state)
        else:
            if len(self.transition_request) == 7:
                if type == "sound":
                    if self.voicelines[new_state]:
                        self.voice.put(random.choice(self.voicelines[new_state]))
                self.current_state = new_state
                self.transition_request = []
            else:
                if new_state == self.transition_request[-1]:
                    self.transition_request.append(new_state)
                else:
                    self.transition_request = []
                    self.transition_request.append(new_state)

    def execute(self, valid_detections):
        #step through the states, reqesting transitions as needed
        if self.current_state == States.Search:
            #if a person is found, request transition to found state
            if "person" in valid_detections:
                self.request_transition(States.Found, "sound")
                
            return None

        elif self.current_state == States.Found:
            answer = None
            # Start the listen thread if it is not already running
            if self.listen_thread is None or not self.listen_thread.is_alive():
                self.stop_listen_thread.clear()  # Clear the event flag
                self.listen_thread = threading.Thread(target=self.listen_loop)
                self.listen_thread.start()

            #if a phone is found, request transition to phone state
            if "cell phone" in valid_detections:
                self.request_transition(States.Phone, "sound")
            
            #if a person is not found, request transition to lost state
            elif "person" not in valid_detections:
                self.request_transition(States.Lost, "sound")

            return answer

        elif self.current_state == States.Phone:
            #if a cellphone is not present, transition
            if "cell phone" not in valid_detections:
                #if a person is present, go to found state, else go to lost. 
                if "person" in valid_detections:
                    self.request_transition(States.Found)
                else:
                    self.request_transition(States.Lost, "sound")

            return None

        elif self.current_state == States.Lost:
            # Signal the listen_thread to stop
            self.stop_listen_thread.set()
            
            #transition to search state
            self.request_transition(States.Search, "sound")
            return None

    def listen_loop(self):
        # while in a valid listen state
        while not self.stop_listen_thread.is_set():
            #listen and grab the voice input
            result = self.speech_to_text.listen()
            #output to terminal
            print(result)
            
            #assumming not error, print to display.
            if not "Error" in result:
                self.display.write_to_third_line(result)

            #three options: clark prompt, prompt with question, non prompt. 
            #split input into list of words
            last_word = list(result.split(" "))
            #clark prompt
            if last_word[-1] == "clark":
                
                self.voice.put("Hello Joe, what can i help you with?")
                #grab request
                request = self.speech_to_text.take_request()
                #if error, keep listening
                while "Error" in request:
                    self.voice.put("I'm sorry, I didn't catch that. Please repeat your request.")
                    request = self.speech_to_text.take_request()

                #Write to display
                self.display.write_to_third_line(request)
                
                #print to terminal
                print(f"User: {request}")
                
                #get the response from the bot
                response = self.bot.prompt(request)
                
                #print the response to the terminal
                print(f"Bot: {response}")
                
                #put the response into the voice queue
                self.voice.put(response)
            
            #clark with prompt
            elif (last_word[-1] != "clark") and ("clark" in result):
                keyword_index = last_word.index("clark")
                request = " ".join(last_word[keyword_index+1:])
                # write to display
                self.display.write_to_third_line(request)
                print(f"User: {request}")
                response = self.bot.prompt(request)
                print(f"Bot: {response}")
                self.voice.put(response)

            #irrelevant info
            else:
                pass


