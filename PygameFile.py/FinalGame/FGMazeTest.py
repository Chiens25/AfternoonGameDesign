# Sydney Chien
# Importing images to use in the game
# Learning how to move characters

import pygame
pygame.init()

# print(pygame.font.get_fonts())
# pygame.time.delay(10000)
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)
GIANT_FONT = pygame.font.SysFont('comicsans', 100)

colors = {"violet": (144, 13, 255), "yellow":(250, 225, 0), "pink": (255, 1, 129), "turquoise": (50, 219, 240), "white":(255,255,255), "grey":(245,245,245), "black":(0,0,0), "red":(255,0,0), "green":(0,255,0), "blue":(0,0,255), "orange":(255,128,0), "purple":(127,0,255)}

# General Variables
WIDTH = 700   # Amount of pixels
w3 = WIDTH//3
HEIGHT = 700


screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Windown size

pygame.display.set_caption("First Game") # Name Game 

# Provided by Youtube Guy
# REMEMBER TO COPY RELATIVE PATH
walkRight = [pygame.image.load('PygameFile.py\MovingImages\R1.png'), pygame.image.load('PygameFile.py\MovingImages\R2.png'), pygame.image.load('PygameFile.py\MovingImages\R3.png'), pygame.image.load('PygameFile.py\MovingImages\R4.png'), pygame.image.load('PygameFile.py\MovingImages\R5.png'), pygame.image.load('PygameFile.py\MovingImages\R6.png'), pygame.image.load('PygameFile.py\MovingImages\R7.png'), pygame.image.load('PygameFile.py\MovingImages\R8.png'), pygame.image.load('PygameFile.py\MovingImages\R9.png')]
walkLeft = [pygame.image.load('PygameFile.py\MovingImages\L1.png'), pygame.image.load('PygameFile.py\MovingImages\L2.png'), pygame.image.load('PygameFile.py\MovingImages\L3.png'), pygame.image.load('PygameFile.py\MovingImages\L4.png'), pygame.image.load('PygameFile.py\MovingImages\L5.png'), pygame.image.load('PygameFile.py\MovingImages\L6.png'), pygame.image.load('PygameFile.py\MovingImages\L7.png'), pygame.image.load('PygameFile.py\MovingImages\L8.png'), pygame.image.load('PygameFile.py\MovingImages\L9.png')]
bg = pygame.image.load('PygameFile.py\MovingImages\\bg.jpg') # Background image
bg = pygame.transform.scale(bg, (WIDTH,HEIGHT))
char = pygame.image.load('PygameFile.py\MovingImages\standing.png') # Character image for standing

clock = pygame.time.Clock()

# Setting all used variables
x = 50
y = 600
width = 64
height = 64

hitbox = pygame.Rect(x,y,width, height)

vel = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0
Block1 = pygame.Rect(100, 500, 100, 50)

def redrawGameWindow():
    global walkCount, hitbox, y
    screen.blit(bg, (0,0)) # Blit makes things appear on the game screen

    Button_Back = pygame.Rect(20, 20, 100, 50)
    pygame.draw.rect(screen, colors.get("red"), Button_Back)
    textBack = MENU_FONT.render("Back", 1, colors.get("black"))
    screen.blit(textBack, (25, 25))

    Block1 = pygame.Rect(100, 500, 100, 50)
    pygame.draw.rect(screen, colors.get("black"), Block1)

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        screen.blit(walkLeft[walkCount//3], (x,y))
        hitbox = pygame.Rect(x,y,width,height)
        walkCount -= 1
    elif right:
        screen.blit(walkRight[walkCount//3], (x,y))
        hitbox = pygame.Rect(x,y,width,height)
        walkCount +=1
    else:
        screen.blit(char, (x,y))
        hitbox = pygame.Rect(x,y,width,height)
    
    
    pygame.display.update()



#mainloop
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get(): # Allow for quit
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    # Move left only if not at the left border
    if keys[pygame.K_LEFT] and x > vel:# Left arrow key
        x -= vel
        left = True
        right = False
    # Same for right
    elif keys[pygame.K_RIGHT] and x < 700 - width - vel:
        x += vel
        right = True
        left = False
    else: # If not, stay in place
        right = False
        left = False
        walkCount = 0
        
    if not(isJump): # Space key to use jump
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
        
    else:

        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            if Block1.colliderect(hitbox):
                if neg > 0:
                    print("we are above")
                if neg < 0:
                    print("we are below")
            jumpCount -= 1
            
        else:
            isJump = False
            jumpCount = 10
            
    redrawGameWindow()

pygame.quit()