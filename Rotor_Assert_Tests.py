
"""
The below rotor_from_name class has been exclusively created only for the assert tests on the enigma.pynb, please DO NOT USE this class to run the code breaking or to run the full-machine tests.
"""

###Please do not modify the below code###

class rotor_from_name:
    I = ("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
    II = ("AJDKSIRUXBLHWTMCQGZNPYFVOE")
    III = ("BDFHJLCPRTXVZNYEIWGAKMUSQO")
    IV = ("ESOVPZJAYQUIRHXLNFTGKDCMWB")
    V = ("VZBRGITYUPSDNHLXAWMJQOFECK")
    Beta = ("LEYJVCNIXWPBQMDRTAKZGFUHOS")
    Gamma = ("FSOKANUERHMBTIYCWLQPZXVGJD")
    VI = ("JPGVOUMFYQBENHZRDKASXLICTW")
    VII = ("NZJHGRCXMYSWBOUFAIVLPEKQDT")
    VIII = ("FKQHTLXOCBJSPDZRAMEWNIUYGV")

    def __init__(self, char):
        self.label = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.char = char
        self.original_label = {}
        self.rotor_label = {}
        self.original_index = {}
        self.rotor_index = {}
        self.rotor = self.wiring_assign()
    
    #method to assign each rotor wiring to the rotor object 
    def wiring_assign(self):
        if self.char == "I":
            self.rotor = rotor_from_name.I
        elif self.char == "II":
            self.rotor = rotor_from_name.II
        elif self.char == "III":
            self.rotor = rotor_from_name.III
        elif self.char == "IV":
            self.rotor = rotor_from_name.IV
        elif self.char == "V":
            self.rotor = rotor_from_name.V
        elif self.char == "Beta":
            self.rotor = rotor_from_name.Beta
        elif self.char == "Gamma":
            self.rotor = rotor_from_name.Gamma
        elif self.char == "VI":
            self.rotor = rotor_from_name.VI
        elif self.char == "VII":
            self.rotor = rotor_from_name.VII
        elif self.char == "VIII":
            self.rotor = rotor_from_name.VIII

        return self.rotor
    
    ##splits the letters into their own dictionaries
    def label_split(self):
        for i, j in enumerate(self.label):
            # print(i,j)
            self.original_label.update([(i, j)])
            self.original_index.update([(j, i)])

        for i, j in enumerate(self.rotor):
            # print(i,j)
            self.rotor_label.update([(i, j)])
            self.rotor_index.update([(j, i)])

        return
    
    #method to encrypt a letter going right side to left side (keyboard to rotor to reflector)
    def encode_right_to_left(self, letter):
        self.label_split()
        right = self.original_index[letter]
        return self.rotor_label[right]
    
    #method to encrypt a letter going left side to right side (reflector to rotor to keyboard)
    def encode_left_to_right(self, letter):
        self.label_split()
        left = self.rotor_index[letter]
        return self.original_label[left]

    #def show(self):
        #print(self.original_label)
        #print(self.rotor_label)


###Please do not modify the above code###