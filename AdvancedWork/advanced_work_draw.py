import pygame

'''
The Draw function shown below activates a canvas of certain length and width, which in turn gives a graphical representation 
enigma machine in action. This class gives us a visual representation of each enigma component, along with their titles 
on top of each component. Please note that Left: left rotor, Middle: middle rotor and Right: right rotor. 
'''

###Please do not modify the below code###

def Draw(enigma, path, screen, width, height, margin, gap, font):

    w = (width - margin["left"] - margin["right"] - 6) / 12
    h = height - margin["top"] - margin["bottom"]

    a = [margin["top"]+(signal+1)*h/27 for signal in path]
    b = [width-margin["right"]-w/2]

    for i in range(4,-1,-1):
        b.append(margin["left"]+(i)*(w+gap/1.83)+w*3/4)
        b.append(margin["left"]+(i)*(w+gap/1.83)+w*1/4)
    for i in range(1,5):
        b.append(margin["left"]+(i)*(w+gap/1.83)+w*1/4)
        b.append(margin["left"]+(i)*(w+gap/1.83)+w*3/4)
    b.append(width-margin["right"]-w/2)

    if len(path) > 0:
        for i in range(1,len(path)):
            if i < 10:
                color = "#43aa8b"
            elif i < 11:
                color = "#f9c74f"
            else:
                color = "#e63946"
            start = (b[i-1],a[i-1])
            end = (b[i],a[i])
            pygame.draw.line(screen, color, start, end, width=5)

    x = margin["left"]
    y = margin["top"]

    for comp in [enigma.ref, enigma.r1, enigma.r2, enigma.r3, enigma.pb, enigma.kb]:
        comp.draw(screen, x, y, w, h, font)
        x += gap

    #add names
    names = ['Reflector', 'Left', 'Middle', 'Right', 'Plugboard', 'Keyboard']
    y = margin["top"]*3/3.5
    for i in range(6):
        x = margin["left"] + (i)*(w+gap/1.83)+w*2/3.75
        title = font.render(names[i], True, "beige")
        text_box = title.get_rect(center = (x,y))
        screen.blit(title, text_box)

###Please do not modify the above code###