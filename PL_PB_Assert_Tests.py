
"""
The below PlugLead has been exclusively created only for the assert test on the enigma.pynb, please DO NOT use this class to run the code breaking or to run the full-machine tests.
"""

###Please do not modify the below code###

class PlugLead:
    def __init__(self, pair):
        self.pair = pair
        #self.label = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        #letter_to_index = {}
        #index_to_letter = {}

        #for i, j in enumerate(self.label):
            #print(i,j)
            #letter_to_index.update([(j,i)])
            #index_to_letter.update([(i,j)])

    #@staticmethod
    #method to encode the pluglead pairs
    def encode(self, char):
        #self.char = char
        if char == self.pair[0]:
            return self.pair[1]
        elif char == self.pair[1]:
            return self.pair[0]
        else:
            return char

class Plugboard(PlugLead):
    #inheritance shown as a part of the class implementation
    def __init__(self):
        #super().__init__(pair)
        #self.pair = pair
        self.leads= []
        self.label = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    ##method to add pluglead pairs to the plugboard
    def add(self, pair):
        return self.leads.append(pair)
    
    ##method to encode the pluglead pairs
    def encode(self, char):
        #result = ''
        for lead in self.leads:
            res = lead.encode(char)
            if res != char:
                return res
        return res
    
###Please do not modify the above code###
