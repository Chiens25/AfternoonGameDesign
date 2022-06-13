# Sydney Chien
# Importing images to use in the game
# Learning how to move characters

import pygame
pygame.init()

win = pygame.display.set_mode((500,480)) # Windown size

pygame.display.set_caption("First Game") # Name Game 

# Provided by Youtube Guy
# REMEMBER TO COPY RELATIVE PATH
walkRight = [pygame.image.load('PygameFile.py\MovingImages\R1.png'), pygame.image.load('PygameFile.py\MovingImages\R2.png'), pygame.image.load('PygameFile.py\MovingImages\R3.png'), pygame.image.load('PygameFile.py\MovingImages\R4.png'), pygame.image.load('PygameFile.py\MovingImages\R5.png'), pygame.image.load('PygameFile.py\MovingImages\R6.png'), pygame.image.load('PygameFile.py\MovingImages\R7.png'), pygame.image.load('PygameFile.py\MovingImages\R8.png'), pygame.image.load('PygameFile.py\MovingImages\R9.png')]
walkLeft = [pygame.image.load('PygameFile.py\MovingImages\L1.png'), pygame.image.load('PygameFile.py\MovingImages\L2.png'), pygame.image.load('PygameFile.py\MovingImages\L3.png'), pygame.image.load('PygameFile.py\MovingImages\L4.png'), pygame.image.load('PygameFile.py\MovingImages\L5.png'), pygame.image.load('PygameFile.py\MovingImages\L6.png'), pygame.image.load('PygameFile.py\MovingImages\L7.png'), pygame.image.load('PygameFile.py\MovingImages\L8.png'), pygame.image.load('PygameFile.py\MovingImages\L9.png')]
bg = pygame.image.load('PygameFile.py\MovingImages\\bg.jpg') # Background image
char = pygame.image.load('PygameFile.py\MovingImages\standing.png') # Character image for standing

clock = pygame.time.Clock()

# Setting all used variables
x = 50
y = 400
width = 64
height = 64
vel = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0


def redrawGameWindow():
    global walkCount
    win.blit(bg, (0,0)) # Blit makes things appear on the game window

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount +=1
    else:
        win.blit(char, (x,y))
    
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
    elif keys[pygame.K_RIGHT] and x < 500 - width - vel:
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
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
            
    redrawGameWindow()

pygame.quit()