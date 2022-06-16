# Sydney Chien

import pygame, os, time
pygame.init()
os.system('cls')

WIDTH = 700#amount of pixels
HEIGHT = 700
colors = {"white":(255,255,255), "grey":(96,96,96), "black":(0,0,0), "red":(255,0,0), "green":(0,255,0), "blue":(0,0,255), "pink":(204,0,204), "orange":(255,128,0), "yellow":(255,255,0), "purple":(127,0,255)}
clr = colors.get("white")

#create a display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game") # title of the window
# pygame.time.delay(1000)
blueClr = (0,0,255)
redClr = (255,0,0)
cyanClr = (0, 255, 177)
# screen.fill(cyanClr)
# pygame.display.update() #have to do after any change that the user can see
# pygame.time.delay(1000)
hb = 50
wb = 50
xb = 325
yb = 325
square = (xb,yb,wb,hb) #create the object to draw

run = True
background = redClr
while run:
    screen.fill(background)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print("you quit")
    #rect(surface, color, object)
    pygame.draw.rect(screen, blueClr, square)

    #circle(surface, color, center, radius)
    pygame.draw.circle(screen, cyanClr, (350, 350), 25)
    pygame.display.update()