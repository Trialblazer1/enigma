import pygame

'''
The below Keyboard class implements the forward functionality in the form of a signal(index number of the corresponding 
str character) and the backward pass as a return str character of the corresponding signal(value located at that index number). 
The code also implements the graphical representation of the keyboard component to the graphical canvas.
'''

###Please do not modify the below code###

class Keyboard:
    def forward(self, letter):
        signal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        return signal

    def backward(self, signal):
        letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[signal]
        return letter

    def draw(self, screen, x, y, w, h, font):

        r = pygame.Rect(x,y,w,h)
        pygame.draw.rect(screen, "orange", r, width=2, border_radius=5)

        for i in range(26):
            letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i]
            letter = font.render(letter, True, "grey")
            text_box = letter.get_rect(center = (x+w/2,y+(i+1)*h/27))
            screen.blit(letter, text_box)

###Please do not modify the above code###