# Description: This file contains the state machine for the vision module.
import random
import STT
import BardController

#state machine to handle transitions

class States:
    Search = "search"
    Found = "found"
    Phone = "phone"
    Lost = "lost"

class VisionState:
    def __init__(self, _voice):
        self.voice = _voice
        self.current_state = States.Search
        self.transition_request = []
        self.speach_to_text = STT()
        self.bard = BardController()
        
        self.voicelines = {
            "search": [],
            "found": ["Hello Joe", "Yee haw", "I found you", "I see you", "I found you Joe", "I see you Joe"],
            "phone": ["Get off your phone!", "Put your phone away!", "Stop using your phone!", "Stop using your phone Joe!"],
            "lost": ["Goodbye Joe", "Goodbye", "Bye Joe", "Bye", "Goodbye Joe"]

        }

    def request_transition(self, new_state, type = ""):
        print(self.transition_request)
        if self.transition_request == []:
            self.transition_request.append(new_state)
        else:
            # if meets the required amount of requests, transition
            if len(self.transition_request) == 7: #7 consecutive requests required to change state
                # Voiceline or not
                if type == "sound":
                    # if needs voiceline and voiceline exists, add to queue
                    if self.voicelines[new_state] != []:
                        self.voice.put(random.choice(self.voicelines[new_state]))
                
                #transition to new state
                self.current_state = new_state
                self.transition_request = []

            #else, add to the request
            else:
                #if the same as end of list, add
                if new_state == self.transition_request[-1]:
                    self.transition_request.append(new_state)
                    #else, create new list
                else:
                    self.transition_request = []
                    self.transition_request.append(new_state)


    def execute(self, valid_detections):
        if self.current_state == States.Search:
            # Only transition when a person is present.
            if "person" in valid_detections:
                self.request_transition(States.Found, "sound")

        elif self.current_state == States.Found:
            # If a person is holding a cell phone, transition to Phone.
            if "cell phone" in valid_detections :
                self.request_transition(States.Phone, "sound")
            # If no person is detected, transition to Lost.
            elif "person" not in valid_detections:
                self.request_transition(States.Lost, "sound")

        elif self.current_state == States.Phone:
            # If no cell phone is present, check for a person.
            if "cell phone" not in valid_detections:
                # If a person is detected, transition to Found.
                #no sound needed as person is already found
                if "person" in valid_detections:
                    self.request_transition(States.Found)
                else:
                    self.request_transition(States.Lost, "sound")
                

        elif self.current_state == States.Lost:
            self.request_transition(States.Search, "sound")
            