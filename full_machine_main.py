from full_machine_pluglead import Pluglead
from full_machine_plugboard import PlugBoard
from full_machine_rotor import Rotor
from full_machine_reflector import Reflector
from full_machine_enigma import Enigma

"""
Please see the default settings below. To change the rotor settings or ring settings or key settings, see the below.

Enigma settings- Please enter the reflector followed by rotors (only 3), followed by the plugboard and the keyboard from left to right.
To change or add new plugleads, please add the letter pairs (All upper case), into the pairs list, as strings separated by a comma ',' character. 

You can choose to have no pairs at all or a maximum of 13 pairs. The key can be any three letter string (All upper case), as shown below.
"""

#historical rotors and reflectors
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
Beta = Rotor("LEYJVCNIXWPBQMDRTAKZGFUHOS", None)
Gamma = Rotor("FSOKANUERHMBTIYCWLQPZXVGJD", None)
A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")
### Please do not modify the above rotors and reflectors ###

"""
The below code uses the instantiates the initial settings of the enigma machine used to encrypt or decrypt a give message.
The below code shows us the different components like the plugboard, rings, key, rotors, plugleads and their initial positions.
"""

#plugboard
pb = PlugBoard()
pairs = ['KI', 'XN', 'FL']
pb.add(pairs)

#Enigma machine
rotors = (Beta,Gamma,V)
ref = C
key = ('MJM')
rings = (4,2,14)

enigma = Enigma(ref, rotors, pb)
enigma.ring_settings(rings)
enigma.starting_positions(key)

#encipher function
def encipher(message):
    encoded_message = ''
    for alpha in message:
        encoded_message = encoded_message + enigma.cipher(alpha)
    return encoded_message

message = "DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ"
print(encipher(message))