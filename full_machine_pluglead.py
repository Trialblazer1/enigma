
"""
The below Pluglead class implements the functionality of taking a given pair of letters and swapping (encoding) each character
of the str pair to it's corresponding partner character.
"""

### The Pluglead class takes in a pair of str letters, instantiates two dictionaries, one mapping each letter to it's index and the other one mapping each index to it's corresponding letter {key:value pairs} ###

###Please do not modify the below code###

class Pluglead:
    def __init__(self, pair):
        self.pair = pair
        self.label = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        letter_to_index = {}
        index_to_letter = {}

        for i, j in enumerate(self.label):
            letter_to_index.update([(j,i)])
            index_to_letter.update([(i,j)])

    #@staticmethod
    #method to encode the pluglead pairs
    def encode(self, char):
        if char == self.pair[0]:
            return self.pair[1]
        elif char == self.pair[1]:
            return self.pair[0]
        else:
            return char

###Please do not modify the above code###