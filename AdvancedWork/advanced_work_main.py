import pygame

from advanced_work_keyboard import Keyboard
from advanced_work_plugboard import Plugboard
from advanced_work_rotor import Rotor
from advanced_work_reflector import Reflector
from advanced_work_enigma import Enigma
from advanced_work_draw import Draw

#historical rotors and reflectors
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")
###Please do not modify the above rotors and reflectors###

'''
Please see the default settings below. To change the rotor settings or ring settings or key settings, see the below.
Enigma settings- Please enter the reflector followed by rotors (only 3), followed by the plugboard and the keyboard from left to right.
To change or add new plugleads, please add the letter pairs (All upper case), into the pairs list, as strings separated by a comma ',' character. You can choose to have no pairs at all or a maximum of 13 pairs.
The key can be any three letter string (All upper case), as shown below.
'''

pairs = ['AB', 'CD', 'EF']
pb = Plugboard(pairs)
kb = Keyboard()
enigma = Enigma(B,I,II,III,pb,kb)
enigma.set_rings((1,1,1))
enigma.set_key("AAZ")


###Please do not modify the below code###
"""
The below code uses the library pygame and instantiates the canvas that according to the specified length and width parameters.
The below code shows us the different components, the letter size and color etc. on the simulator on a different window.
"""

pygame.init()
pygame.font.init()
pygame.display.set_caption("Enigma Simulator")

mono = pygame.font.SysFont("FreeMono", 25)
bold = pygame.font.SysFont("FreeMono", 25, bold=True)

width = 1400
height = 750
screen = pygame.display.set_mode((width, height))
margin = {"top":100, "bottom":25, "left":50, "right":100}
gap = 230

input = ""
output = ""
path = []

animating = True
while animating:
    screen.fill("#333333")

    text = mono.render(input, True, "beige")
    text_box = text.get_rect(center=(width/2,margin["top"]/6))
    screen.blit(text, text_box)
    text = bold.render(output, True, "beige")
    text_box = text.get_rect(center=(width/2,margin["top"]/6+30))
    screen.blit(text, text_box)

    Draw(enigma, path, screen, width, height, margin, gap, bold)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                input = input + ' '
                output = output + ' '
            else:
                key = event.unicode
                if key in "abcdefghijklmnopqrstuvwxyz" or key in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    letter = key.upper()
                    input = input + letter
                    path, cipher = enigma.encipher(letter)
                    output = output + cipher

###Please do not modify the above code###

