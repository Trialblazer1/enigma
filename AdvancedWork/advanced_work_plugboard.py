import pygame

'''
The below Plugboard class implements the functionality of adding plug leads to the plugboard and swapping each character 
of the str pair to it's corresponding partner character. It also implements the forward functionality in the form of a 
signal(index number of the corresponding str character) and the backward pass as a return int character of the corresponding 
signal(index number of the corresponding str character). The code also implements the graphical representation of the 
plugboard component to the graphical canvas.
'''

###Please do not modify the below code###

class Plugboard:
    def __init__(self, pairs):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for pair in pairs:
            A = pair[0]
            B = pair[1]
            pos_A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(A)
            pos_B = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(B)
            self.left = self.left[:pos_A] + B + self.left[pos_A+1:]
            self.left = self.left[:pos_B] + A + self.left[pos_B + 1:]

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal

    def draw(self, screen, x, y, w, h, font):

        r = pygame.Rect(x,y,w,h)
        pygame.draw.rect(screen, "orange", r, width=2, border_radius=5)

        for i in range(26):
            letter = self.left[i]
            letter = font.render(letter, True, "grey")
            text_box = letter.get_rect(center = (x+w/4,y+(i+1)*h/27))
            screen.blit(letter, text_box)

            letter = self.right[i]
            letter = font.render(letter, True, "grey")
            text_box = letter.get_rect(center=(x+w*3/4,y+(i+1)*h/27))
            screen.blit(letter, text_box)

###Please do not modify the above code###
