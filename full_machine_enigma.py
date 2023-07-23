"""
Enigma class that puts different functionalities of the machine together and works towards encrypting/decrypting a give message.
This class implements the functionality of setting the rings to a given position, setting the key to a given string of three characters
and enciphers/deciphers a given character, returning us back with a corresponding character output.
"""

### The Enigma instiates the reflector object, rotors (as a list object) and the plugboard object and performs the necessary operations at each level of the machine ###

###Please do not modify the below code###

class Enigma:
    def __init__(self, ref, r, pb):
        self.ref = ref
        self.r = r
        self.pb = pb
    
    #ring settings
    def ring_settings(self, rings):
        n = 0
        for rotor in (self.r):
            rotor.ring(rings[n])
            n += 1
    
    #starting positions (or) key settings
    def starting_positions(self, key):
        n = 0
        for rotor in (self.r):
            rotor.rotate(key[n])
            n += 1
    
    #encryption mechanism
    def cipher(self, letter):
        if len(self.r) == 4:
            if self.r[3].notch == None:
                self.r[3].rotate()
            elif self.r[2].notch == None and self.r[3].label[0] == self.r[3].notch:
                self.r[3].rotate()
                self.r[2].rotate()
            else:
                if self.r[2].label[0] == self.r[2].notch and self.r[3].label[0] == self.r[3].notch:
                    self.r[1].rotate()
                    self.r[2].rotate()
                    self.r[3].rotate()
                elif self.r[2].label[0] == self.r[2].notch:
                    self.r[1].rotate()
                    self.r[2].rotate()
                    self.r[3].rotate()
                elif self.r[3].label[0] == self.r[3].notch:
                    self.r[3].rotate()
                    self.r[2].rotate()
                else:
                    self.r[3].rotate()
        else:
            if self.r[2].notch == None:
                self.r[2].rotate()
            elif self.r[1].notch == None and self.r[2].label[0] == self.r[2].notch:
                self.r[2].rotate()
                self.r[1].rotate()
            else:
                if self.r[1].label[0] == self.r[1].notch and self.r[2].label[0] == self.r[2].notch:
                    self.r[0].rotate()
                    self.r[1].rotate()
                    self.r[2].rotate()
                elif self.r[1].label[0] == self.r[1].notch:
                    self.r[0].rotate()
                    self.r[1].rotate()
                    self.r[2].rotate()
                elif self.r[2].label[0] == self.r[2].notch:
                    self.r[2].rotate()
                    self.r[1].rotate()
                else:
                    self.r[2].rotate()

        return self.encipher(letter)
    
    #encryption path
    def encipher(self, letter):
        pulse = self.pb.right_to_left(letter)

        for i in range(len(self.r) - 1, -1, -1):
            pulse = self.r[i].right_to_left(pulse)

        pulse = self.ref.reflect(pulse)

        for i in range(len(self.r)):
            pulse = self.r[i].left_to_right(pulse)

        letter = self.pb.left_to_right(pulse)
        return letter

###Please do not modify the above code###