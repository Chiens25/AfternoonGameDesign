# Sydney Chien
# We are going to learn basic pygame functions
 # Find colors: Search "rgb color chart"
import pygame, os, time
pygame.init()
os.system('cls')

WIDTH = 700 # Pixels
HEIGHT = 700

colors = {"white":(255,255,255), "pink": (255, 0, 255), "yellow": (255,255,0), "green": (0,255,0), "black": (0,0,0), "grey": (192,192,192), "orange": (255,165,0), "violet": (148,0,211), "red": (255,0,0), "blue": (0,0,255)}
clr = colors.get("white")


# Create a display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game") # Title of window
pygame.time.delay(3000)
blueClr = (0, 0, 255)
redClr = (255, 0, 0)
cyanClr = (0, 255, 177)
# screen.fill(blueClr)
# pygame.display.update() # Have to do after any change that the user can see
# pygame.time.delay(3000)
hb = 50 # Height value
wb = 50
xb = 325 # Where it will be displayed
yb = 325
square = (xb, yb, hb, wb)

run = True
background = clr
while run:
    screen.fill(background)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print("you quit")
    # rect(surface, color, object)
    pygame.draw.rect(screen, blueClr, square)
    # circle(surface, color, center, radius)
    pygame.draw.circle(screen, cyanClr, (350, 350), 25)
    pygame.display.update()

   
    