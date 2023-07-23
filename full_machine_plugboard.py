
"""
The below Plugboard class implements the functionality of adding plug leads to the plugboard and swapping each character
of the str pair to it's corresponding partner character. It also implements the forward functionality in the form of a
signal(index number of the corresponding str character) and the backward pass as a return int character of the corresponding
signal(index number of the corresponding str character).
"""

### The PlugBoard class takes in a pair of str letters, instantiates four dictionaries, to map each letter to it's index and the other one to map each index to it's corresponding letter {key:value pairs}. This is done both for the original ordered letters and the letters swapped according to the pluglead pairs ###

###Please do not modify the below code###

from full_machine_pluglead import Pluglead

class PlugBoard:
    #@staticmethod
    def __init__(self):
        self.leads= []
        self.label = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.swapped_label = ""
        self.original_label = {}
        self.swapped_label = {}
        self.original_index = {}
        self.swapped_index = {}

        for i, j in enumerate(self.label):
            self.original_label.update([(i, j)])
            self.original_index.update([(j, i)])
            self.swapped_label.update([(i, j)])
            self.swapped_index.update([(j, i)])
    
    #method to add pluglead pairs to the plugboard
    def add(self, pairs):
        for pair in pairs:
            self.leads.append(Pluglead(pair))
            pos_A = self.original_index[pair[0]]
            pos_B = self.original_index[pair[1]]
            self.swapped_label[pos_A] = pair[1]
            self.swapped_label[pos_B] = pair[0]
            self.swapped_index[pair[0]] = pos_B
            self.swapped_index[pair[1]] = pos_A

    #@staticmethod
    #method to encode the pluglead pairs
    def encode(self, char):
        res = ''
        for lead in self.leads:
            res = lead.encode(char)
            if res != char:
                print(res)
                break
        return res
    
    #method to encrypt a letter going right side to left side (keyboard to rotor)
    def right_to_left(self, letter):
        return self.swapped_index[letter]
    
    #method to encrypt a letter going left side to right side (rotor to back to keyboard)
    def left_to_right(self, pulse):
        return self.swapped_label[pulse]

###Please do not modify the above code###