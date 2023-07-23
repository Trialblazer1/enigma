
"""
The below Reflector class implements the reflect functionality in the form of a signal(index number of the corresponding str character).
"""

### The Reflector class takes the reflector wiring, instantiates four dictionaries, to map each letter to it's index and the other one to map each index to it's corresponding letter {key:value pairs}. This is done both for the original ordered letters and the letters ordered according to the reflector chronology ###

###Please do not modify the below code###

class Reflector:
    def __init__(self, wiring):
        self.label = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.reflector = wiring
        self.original_label = {}
        self.reflector_label = {}
        self.original_index = {}
        self.reflector_index = {}

        for i, j in enumerate(self.label):
            self.original_label.update([(i, j)])
            self.original_index.update([(j, i)])

        for i, j in enumerate(self.reflector):
            self.reflector_label.update([(i, j)])
            self.reflector_index.update([(j, i)])
    
    #method to reflect a letter received onto the reflector and send it's corresponding value back to the leftmost rotor
    def reflect(self, pulse):
        return self.original_index[self.reflector_label[pulse]]

###Please do not modify the above code###

