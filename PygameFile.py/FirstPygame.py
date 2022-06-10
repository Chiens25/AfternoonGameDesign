# Sydney Chien
# We are going to learn basic pygame functions
 # Find colors: Search "rgb color chart"
from locale import CHAR_MAX
from turtle import circle
import pygame, os, random, math, time
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

# images
bg = pygame.image.load("PygameFile.py\Images\\bgSmaller.jpg")
char = pygame.image.load("PygameFile.py\Images\PixelArtTutorial.png")
char = pygame.transform.scale(char, (50,50))
# screen.fill(blueClr)
# pygame.display.update() # Have to do after any change that the user can see
# pygame.time.delay(3000)

# Var for square
hb = 50 # Height value
wb = 50
xb = 325 # Where it will be displayed
yb = 325
square = pygame.Rect(xb, yb, hb, wb)

charx = xb
chary = yb

# Var for circle
cx = 350
cy = 350
rad = 25
ibox = rad*math.sqrt(2)
xig = cx-(ibox/2)
yig = cy-(ibox/2)

speed = 1
run = True
background = clr
while run:
    screen.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print("you quit")
        # Mouse position coordinates
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            print(mousePos)
# Square movement
    keys = pygame.key.get_pressed() # provide a list of 11 keys
    if keys [pygame.K_a] and square.x > speed:
        square.x -= speed
    if keys[pygame.K_d] and square.x < WIDTH - (wb+speed):
        square.x += speed
    if keys [pygame.K_w] and square.y > speed:
        square.y -= speed
    if keys[pygame.K_d] and square.y < HEIGHT - (hb+speed):
        square.y += speed
# Circle movement
    if keys [pygame.K_LEFT] and cx > (speed+rad):
        cx -= speed
        inSquare.x -= speed
    if keys[pygame.K_RIGHT] and cx < WIDTH - (rad+speed):
        cx += speed
        inSquare.x += speed
    if keys [pygame.K_UP] and cy > (rad+speed):
        cy -= speed
        inSquare.y -= speed
    if keys[pygame.K_DOWN] and cy < HEIGHT - (rad+speed):
        cy += speed
        inSquare.y += speed

    # rect(surface, color, object)
    if square.collidepoint((cx,cy)):
        print("BOOM")
        cx = random.randint(rad,WIDTH-rad)
        cy = random.randint(rad,HEIGHT-rad)
        rad+= 5
        # Inscibed square
        ibox = rad*math.sqrt(2)
        xig = cx-(ibox/2)
        yig = cy-(ibox/2)
        inSquare = pygame.Rect(xig,yig,ibox, ibox)
        screen.blit(char, (200,200))

    # Mountain collid
    if square.colliderect(mountainSquare):
        square.x = 10
        square.y = 10
        charx = 10
        chary = 10
        
        #Bounce
        mountainSquare = pygame.Rect(200,270,180,250)
        pygame.draw.rect(screen, colors.get("white"), mountainSquare)
        
    pygame.draw.rect(screen, blueClr, square)
    # circle(surface, color, center, radius)
    pygame.draw.circle(screen, cyanClr, (cx, cy), rad) # Circle is not an object
    pygame.display.update()
    pygame.time.delay(5)
   
    