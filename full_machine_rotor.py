
"""
The below Rotor class implements the forward and backward functionality in the form of a signal(index number of the corresponding
str character), rotate method(to rotate n number of times), rotate_to_letter(to rotate to a given str character) and
a set_ring method (to set the position of the rings to a given int value).
"""

### The Rtor class takes the rotor wiring and a notch (or no notch), instantiates four dictionaries, to map each letter to it's index and the other one to map each index to it's corresponding letter {key:value pairs}. This is done both for the original ordered letters and the letters ordered according to the rotor chronology ###

###Please do not modify the below code###

class Rotor:
    def __init__(self, wiring, notch):
        self.label = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.rotor = wiring
        self.notch = notch
        self.original_label = {}
        self.rotor_label = {}
        self.original_index = {}
        self.rotor_index = {}
        self.letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    #splits the letters into their own dictionaries
    def label_split(self):
        for i, j in enumerate(self.label):
            self.original_label.update([(i, j)])
            self.original_index.update([(j, i)])

        for i, j in enumerate(self.rotor):
            self.rotor_label.update([(i, j)])
            self.rotor_index.update([(j, i)])
        return
    
    #method to encrypt a letter going right side to left side (rotor towards reflector)
    def right_to_left(self, pulse):
        return self.original_index[self.rotor_label[pulse]]
    
    ##method to encrypt a letter going left side to right side (rotor to back towards keyboard)
    def left_to_right(self, pulse):
        return self.rotor_index[self.original_label[pulse]]
    
    #method to rotate (or not to rotate) a rotor letter to it's corresponding pair value
    def rotate(self, letter = None):
        if letter == None:
            self.label = self.label[1:] + self.label[0]
            self.rotor = self.rotor[1:] + self.rotor[0]
        else:
            n = self.letter.find(letter)
            self.label = self.label[n:] + self.label[:n]
            self.rotor = self.rotor[n:] + self.rotor[:n]
        
        self.label_split()
    
    #method to rotate a letter a rotor letter to it's corresponding ring number
    def ring(self, q):
        n = 26-(q-1)
        self.label = self.label[n:] + self.label[:n]
        self.rotor = self.rotor[n:] + self.rotor[:n]

        if self.notch != None:
            new_notch = self.letter.find(self.notch)
            self.notch = self.letter[((new_notch - q) + 1) % 26]

###Please do not modify the above code###