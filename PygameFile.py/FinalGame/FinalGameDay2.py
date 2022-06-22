# Sydney Chien
# 06/20/2022
# DELETE UNNESSESARY STUFF, ORGANIZE, MAKE COMMENTS BEFORE SUBMITTING
# "RPS" STANDS FOR ROCK PAPER SCISSORS
import pygame, os, time, random, math, datetime, sys
from pygame import mixer
pygame.init()


# print(pygame.font.get_fonts())
# pygame.time.delay(10000)
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)
GIANT_FONT = pygame.font.SysFont('comicsans', 100)
BOLD_FONT = pygame.font.SysFont('comicsans', 20).bold

os.system('cls')

# General Variables
WIDTH = 700   # Amount of pixels
w3 = WIDTH//3
HEIGHT = 700
colors = {"violet": (144, 13, 255), "yellow":(250, 225, 0), "pink": (255, 1, 129), "turquoise": (50, 219, 240), "white":(255,255,255), "grey":(245,245,245), "black":(0,0,0), "red":(255,0,0), "green":(0,255,0), "blue":(0,0,255), "orange":(255,128,0), "purple":(127,0,255)}
clr = colors.get("white")
game = 0
#create a display
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Rock Paper Scissor") # title of the window

blueClr = (0,0,255)
redClr = (255,0,0)
cyanClr = (0, 255, 177)

#images
bg = pygame.image.load("PygameFile.py\FinalGame\FGImages\BoxingRing.jpg") # Load the image
bg = pygame.transform.scale(bg, (WIDTH,HEIGHT)) # Scale it to the size of the screen(WIDTH, HEIGHT)

rock = pygame.image.load("PygameFile.py\FinalGame\FGImages\Rock Image.png") # Load
rock = pygame.transform.scale(rock, (150,150)) # Scale
Prock = pygame.transform.rotate(rock, 270) # Rotate 270 degrees to face right
COMrock =  pygame.transform.flip(Prock, True, False) # Flip player's rock 

paper = pygame.image.load("PygameFile.py\FinalGame\FGImages\Paper Image.png") # Same as rock
paper = pygame.transform.scale(paper, (150,150)) 
Ppaper = pygame.transform.rotate(paper, 270) 
COMpaper =  pygame.transform.flip(Ppaper, True, False)

scissor = pygame.image.load("PygameFile.py\FinalGame\FGImages\Scissor Image.png") # Same as rock
scissor = pygame.transform.scale(scissor, (150,150)) 
Pscissor = pygame.transform.rotate(scissor, 270) 
COMscissor =  pygame.transform.flip(Pscissor, True, False)


# RPS Image Positioning Var
xb = 100
yb = 325

mx = 0
my = 0

#Game Variables
speed = 2
run = True
high = 0
background = colors.get("grey") 
colorTheme = colors.get("white") # Set to colorTheme to change var in settings
mixer.music.load('PygameFile.py\journey.wav') # Play music
mixer.music.play(-1)

# Settings
def settings():
    global screen
    global colorTheme, mx, my, WIDTH, HEIGHT
    screen.fill(colorTheme)
    Title = TITLE_FONT.render("Settings", 1, colors.get("black")) # Designate title font and content
    xd = WIDTH//2 - (Title.get_width()//2) # Make  x coordinate half of screen, minus half of title for centering
    screen.blit(Title, (xd, 10)) # Display

    # Color Settings
    ColorTheme = MENU_FONT.render("Background Color:", 1, colors.get("black")) # Same as title
    screen.blit(ColorTheme, (w3, 70)) # w3 = WIDTH//3
    pygame.display.update()
    pygame.time.delay(50)

    # Color Backgrounds
    Button_White = pygame.Rect(w3, 100, 230, 50)
    Button_Orange = pygame.Rect(w3, 170, 230, 50)
    Button_Purple = pygame.Rect(w3, 240, 230, 50)
    pygame.draw.rect(screen, colors.get("grey"), Button_White)
    pygame.draw.rect(screen, colors.get("turquoise"), Button_Orange)
    pygame.draw.rect(screen, colors.get("violet"), Button_Purple)

    # Name Color Backgrounds
    textWhite = MENU_FONT.render("White", 1, colors.get("black"))
    textOrange = MENU_FONT.render("Turquoise", 1, colors.get("black"))
    textPurple = MENU_FONT.render("Violet", 1, colors.get("black"))
    screen.blit(textWhite, (w3, 110))
    screen.blit(textOrange, (w3, 180))
    screen.blit(textPurple, (w3, 250))
    pygame.display.update()
    pygame.time.delay(50)

    # Back button
    Button_Back = pygame.Rect(20, 20, 100, 50)
    pygame.draw.rect(screen, colors.get("red"), Button_Back)
    textBack = MENU_FONT.render("Back", 1, colors.get("black"))
    screen.blit(textBack, (25, 25))
    pygame.display.update()
    pygame.time.delay(50)

    # Screen Size Settings
    ScreenSize = MENU_FONT.render("Screen Size:", 1, colors.get("black"))
    screen.blit(ScreenSize, (w3, 300))
    pygame.display.update()
    pygame.time.delay(50)

    # Create Shape and Color Buttons
    Button_Size1 = pygame.Rect(w3, 350, 230, 50)
    Button_Size2 = pygame.Rect(w3, 420, 230, 50)
    Button_Size3 = pygame.Rect(w3, 490, 230, 50)
    pygame.draw.rect(screen, colors.get("grey"), Button_Size1)
    pygame.draw.rect(screen, colors.get("grey"), Button_Size2)
    pygame.draw.rect(screen, colors.get("grey"), Button_Size3)

    # Create and Position Text
    textSize1 = MENU_FONT.render("7 by 7", 1, colors.get("black"))
    textSize2= MENU_FONT.render("7 by 9", 1, colors.get("black"))
    textSize3 = MENU_FONT.render("7 by 5", 1, colors.get("black"))
    screen.blit(textSize1, (w3, 360))
    screen.blit(textSize2, (w3, 430))
    screen.blit(textSize3, (w3, 500))
    pygame.display.update()
    pygame.time.delay(50)

 # Sound Settings
    Sound = MENU_FONT.render("Sound?:", 1, colors.get("black"))
    screen.blit(Sound, (WIDTH//8, 600))
    pygame.display.update()
    pygame.time.delay(50)

    # Create Buttons
    Button_SoundY = pygame.Rect(WIDTH * .3, 550, 120, 120)
    Button_SoundN = pygame.Rect(WIDTH * .6, 550, 120, 120)
    pygame.draw.rect(screen, colors.get("grey"), Button_SoundY)
    pygame.draw.rect(screen, colors.get("grey"), Button_SoundN)
  
    # Create Text
    textSoundY = MENU_FONT.render("On", 1, colors.get("black"))
    textSoundN= MENU_FONT.render("Off", 1, colors.get("black"))
    screen.blit(textSoundY, (WIDTH * .3, 560))
    screen.blit(textSoundN, (WIDTH * .6, 560))
    pygame.display.update()
    pygame.time.delay(50)

    # Make Color Backgrounds Change Color Var, Change WIDTH and HEIGHT Var, Play Sound
    while True:
        print("I am here")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu()
                print("you quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_White.collidepoint(mx, my):
                    colorTheme = "white"
                if Button_Orange.collidepoint(mx, my):
                    colorTheme = "turquoise"
                if Button_Purple.collidepoint(mx, my):
                    colorTheme = "violet"
                if Button_Back.collidepoint(mx, my):
                    menu()
                if Button_Size1.collidepoint(mx, my):
                    WIDTH == 700
                    HEIGHT = 700
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
                if Button_Size2.collidepoint(mx, my):
                    WIDTH == 900
                    HEIGHT = 700
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
                if Button_Size3.collidepoint(mx, my):
                    WIDTH == 500
                    HEIGHT = 700
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
                if Button_SoundY.collidepoint(mx, my):
                    mixer.music.play(-1)
                if Button_SoundN.collidepoint(mx, my):
                    mixer.music.stop()

                pygame.display.update()
                settings()

# User Name
def user():
    global userName # For use in calling name later
    background = (255,255,255) # Redefine "background"
    screen.fill(background)
    pygame.display.update()
    pygame.time.delay(500)

    # Create title
    # Create Box, Relative to WIDTH and HEIGHT

    # Create Rectangle
    input_rect = pygame.Rect(WIDTH//4, HEIGHT//3, 350, 50)
    pygame.draw.rect(screen, colors.get("pink"), input_rect)

    pygame.display.update()
    pygame.time.delay(500)

    # Create Text
    Title = TITLE_FONT.render("Enter Name", 1, colors.get("black"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 10))
    pygame.display.update()
    pygame.time.delay(500)

    # Set starting userName
    userName = ""


    run = True
    while run:
        for event in pygame.event.get():
                if event.type == pygame.QUIT: # Exit button
                    print(userName)
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN: # Return -> userName set, move to menu
                    if event.key == pygame.K_RETURN:
                        print(userName)
                        menu()
                    if event.key == pygame.K_BACKSPACE: # Delete -> userName is all letters except the last
                        userName = userName[:-1]
                    else:
                        userName += event.unicode # Gives you all characters for making userName
                screen.fill("white")
                screen.blit(Title, (xd, 10))
                # Draw rectangle
                pygame.draw.rect(screen, "pink", input_rect)
                # Update the name of user
                name = MENU_FONT.render(userName, 1, "black")
                screen.blit(name, (input_rect.x+5, input_rect.y+5))
                pygame.display.flip()
        
        # Draw rect

# Menu
def menu():
    global userName
    screen.fill(colorTheme) # Background
    Title = TITLE_FONT.render("Menu", 1, colors.get("black")) # Create a title
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))

    # Create Welcome Message
    Hello = MENU_FONT.render("Hello " + str(userName) + ", Welcome to the Rock Paper Scissor Game!", 1, colors.get("blue")) # Create a title
    pd = WIDTH//2 - (Hello.get_width()//2)
    screen.blit(Hello, (pd, 100))
    
    #creating buttons
    Button_Instruct = pygame.Rect(WIDTH//3, 150, 230, 50)
    Button_Settings = pygame.Rect(WIDTH//3, 220, 230, 50)
    Button_Game1 = pygame.Rect(WIDTH//3, 290, 230, 50)
    Button_Game2 = pygame.Rect(WIDTH//3, 360, 230, 50)
    Button_Game3 = pygame.Rect(WIDTH//3, 430, 230, 50)
    Button_Score = pygame.Rect(WIDTH//3, 500, 230, 50)
    Button_Ex = pygame.Rect(WIDTH//3, 570, 230, 50)
    pygame.draw.rect(screen, colors.get("pink"), Button_Instruct)
    pygame.draw.rect(screen, colors.get("pink"), Button_Settings)
    pygame.draw.rect(screen, colors.get("pink"), Button_Game1)
    pygame.draw.rect(screen, colors.get("pink"), Button_Game2)
    pygame.draw.rect(screen, colors.get("pink"), Button_Game3)
    pygame.draw.rect(screen, colors.get("pink"), Button_Score)
    pygame.draw.rect(screen, colors.get("pink"), Button_Ex)
    
    #render 
    textInstruct = MENU_FONT.render("Instructions", 1, colors.get("black"))
    textSett = MENU_FONT.render("Settings", 1, colors.get("black"))
    textGame1 = MENU_FONT.render("Level 1", 1, colors.get("black"))
    textGame2 = MENU_FONT.render("Level 2", 1, colors.get("black"))
    textGame3 = MENU_FONT.render("Level 3", 1, colors.get("black"))
    textScore = MENU_FONT.render("Leaderboard", 1, colors.get("black"))
    textEx = MENU_FONT.render("Exit", 0, colors.get("black"))
    screen.blit(textInstruct, (WIDTH//3, 160))
    screen.blit(textSett, (WIDTH//3, 230))
    screen.blit(textGame1, (WIDTH//3, 300))
    screen.blit(textGame2, (WIDTH//3, 370))
    screen.blit(textGame3, (WIDTH//3, 440))
    screen.blit(textScore, (WIDTH//3, 510))
    screen.blit(textEx, (WIDTH//3, 580))
    pygame.display.update()

    # Buttons lead to quit, instructions, settings, game1, game2, score, exit functions
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_Instruct.collidepoint(mx, my):
                    instruction()
                if Button_Settings.collidepoint(mx, my):
                    settings()
                if Button_Game1.collidepoint(mx, my):
                    game1()
                if Button_Game2.collidepoint(mx, my):
                    game2()
                if Button_Game3.collidepoint(mx, my):
                    game3()
                if Button_Score.collidepoint(mx, my):
                    scoreboard()
                if Button_Ex.collidepoint(mx, my):
                    exit()

# Instructions
def instruction():
    #title font
    screen.fill(colorTheme)
    Title = TITLE_FONT.render("Instructions", 1, colors.get("black"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))\

    #Instructions File
    myFile = open("PygameFile.py\FinalGame\FGinstructions.txt", "r")
    content = myFile.readlines()

    #print instructions
    yi = 120   # yi automatically adds space between each printed line
    for line in content:
        Insctruc = MENU_FONT.render(line[0:-1], 1, colors.get('black'))
        screen.blit(Insctruc, (40, yi))
        pygame.display.update()
        pygame.time.delay(50)
        yi += 40
    
    #creating buttons
    Button_1 = pygame.Rect(200, 550, 100, 50)
    Button_2 = pygame.Rect(400, 550, 100, 50)
    pygame.draw.rect(screen, colors.get("pink"), Button_1)
    pygame.draw.rect(screen, colors.get("pink"), Button_2)

    #render yes and no
    text1 = MENU_FONT.render("Yes", 1, colors.get("black"))
    text2 = MENU_FONT.render("No", 1, colors.get("black"))
    screen.blit(text1, (225, 560))
    screen.blit(text2, (425, 560))
    pygame.display.update()

    # Buttons lead to Level 1 or menu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.quit()
                print("you quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_1.collidepoint(mx, my):
                    game1()
                if Button_2.collidepoint(mx, my):
                    menu()


Pcount = 0
COMcount = 0
player = 'r'

walkRight = [pygame.image.load('PygameFile.py\MovingImages\R1.png'), pygame.image.load('PygameFile.py\MovingImages\R2.png'), pygame.image.load('PygameFile.py\MovingImages\R3.png'), pygame.image.load('PygameFile.py\MovingImages\R4.png'), pygame.image.load('PygameFile.py\MovingImages\R5.png'), pygame.image.load('PygameFile.py\MovingImages\R6.png'), pygame.image.load('PygameFile.py\MovingImages\R7.png'), pygame.image.load('PygameFile.py\MovingImages\R8.png'), pygame.image.load('PygameFile.py\MovingImages\R9.png')]
walkLeft = [pygame.image.load('PygameFile.py\MovingImages\L1.png'), pygame.image.load('PygameFile.py\MovingImages\L2.png'), pygame.image.load('PygameFile.py\MovingImages\L3.png'), pygame.image.load('PygameFile.py\MovingImages\L4.png'), pygame.image.load('PygameFile.py\MovingImages\L5.png'), pygame.image.load('PygameFile.py\MovingImages\L6.png'), pygame.image.load('PygameFile.py\MovingImages\L7.png'), pygame.image.load('PygameFile.py\MovingImages\L8.png'), pygame.image.load('PygameFile.py\MovingImages\L9.png')]
bg2 = pygame.image.load('PygameFile.py\MovingImages\\bg.jpg') # Background image
bg2 = pygame.transform.scale(bg2, (WIDTH,HEIGHT))
char = pygame.image.load('PygameFile.py\MovingImages\standing.png') # Character image for standing

clock = pygame.time.Clock()

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

# RPS Level 1
def game1():
    def checkwinner():
        global player, computer
        if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
            maze()
        if (player == 'r' and computer == 'r') or (player == 'p' and computer == 'p') or (player == 's' and computer == 's'):
            tie()
        if (computer == 'r' and player == 's') or (computer == 's' and player == 'p') or (computer == 'p' and player == 'r'):
            lose()

    def RPS():
        global computer, player

        screen.blit(bg, (0,0))
        screen.blit(Prock, (xb, yb))
        screen.blit(COMrock, ((700-150)- xb, yb))

        Player = MENU_FONT.render("Player", 1, colors.get("black")) # Designate title font and content
        screen.blit(Player, (xb+50, 300)) # Display
        COM = MENU_FONT.render("COM", 1, colors.get("black")) # Designate title font and content
        screen.blit(COM, (WIDTH-(xb+100), 300)) # Display

        # Back button
        Button_Back = pygame.Rect(20, 20, 100, 50)
        pygame.draw.rect(screen, colors.get("red"), Button_Back)
        textBack = MENU_FONT.render("Back", 1, colors.get("black"))
        screen.blit(textBack, (25, 25))
        pygame.display.update()
        pygame.time.delay(50)


        computer = random.choice(['r','p','s']) # random working

        Button_R = pygame.Rect(WIDTH//12, 500, 120, 50)
        Button_P = pygame.Rect(WIDTH//12*5, 500, 120, 50)
        Button_S = pygame.Rect(WIDTH//12*9, 500, 120, 50)
        pygame.draw.rect(screen, colors.get("pink"), Button_R)
        pygame.draw.rect(screen, colors.get("pink"), Button_P)
        pygame.draw.rect(screen, colors.get("pink"), Button_S)

        textR = MENU_FONT.render("Rock", 1, colors.get("black"))
        textP = MENU_FONT.render("Paper", 1, colors.get("black"))
        textS = MENU_FONT.render("Scissors", 1, colors.get("black"))
        screen.blit(textR, (WIDTH//12+30, 510))
        screen.blit(textP, (WIDTH//12*5+30, 510))
        screen.blit(textS, (WIDTH//12*9+30, 510))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    mx = mousePos[0]
                    my = mousePos[1]
                    if Button_Back.collidepoint(mx, my):
                        menu()
                    if Button_R.collidepoint(mx, my):
                        player = 'r'
                        screen.blit(Prock, (xb, yb))
                        pygame.display.update()
                        print(player)
                        if computer == 'r':
                            screen.blit(COMrock, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        if computer == 'p':
                            screen.blit(COMpaper, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        if computer == 's':
                            screen.blit(COMscissor, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        checkwinner()
                    if Button_P.collidepoint(mx, my):
                        player = 'p'
                        screen.blit(Ppaper, (xb, yb))
                        pygame.display.update()
                        print(player)
                        if computer == 'r':
                            screen.blit(COMrock, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        if computer == 'p':
                            screen.blit(COMpaper, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        if computer == 's':
                            screen.blit(COMscissor, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        checkwinner()
                        
                    if Button_S.collidepoint(mx, my):
                        player = 's'
                        screen.blit(Pscissor, (xb, yb))
                        pygame.display.update()
                        print(player)
                        if computer == 'r':
                            screen.blit(COMrock, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        if computer == 'p':
                            screen.blit(COMpaper, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        if computer == 's':
                            screen.blit(COMscissor, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        checkwinner()
                                  

    def maze():
        global isJump, x, jumpCount, y
        print("create a maze")
        pygame.time.delay(200)
        screen.fill("yellow")
        Win = GIANT_FONT.render(("YOU WON!"), 1, colors.get("white"))
        xd = WIDTH//2 - (Win.get_width()//2)
        screen.blit(Win, (xd, 200))\
        
        pygame.display.update() 
        pygame.time.delay(1000)

        def redrawGameWindow():
            global walkCount, hitbox, y
            screen.blit(bg2, (0,0)) # Blit makes things appear on the game screen

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

    def tie():
        print("create tie screen")
        pygame.time.delay(500)
        screen.fill("violet")
        Tie = GIANT_FONT.render(("TIE!"), 1, colors.get("white"))
        xd = WIDTH//2 - (Tie.get_width()//2)
        screen.blit(Tie, (xd, 200))\
        
        pygame.display.update() 
        pygame.time.delay(1000)

        RPS()

    def lose():
        global colors
        print("create lose screen")
        pygame.time.delay(500)
        screen.fill("turquoise")
        Lose = GIANT_FONT.render(("YOU LOST!"), 1, colors.get("white"))
        xd = WIDTH//2 - (Lose.get_width()//2)
        screen.blit(Lose, (xd, 200))\
        
        pygame.display.update() 
        pygame.time.delay(1000)

        RPS()


    Game = True
    while Game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                #Menu(mainTitle,messageMenu)
                pygame.quit()
                sys.exit()
                
        pygame.display.update() 
        pygame.time.delay(100)

        RPS()

# RPS Level 2
def game2():
    def checkwinner():
        global player, computer
        if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
            maze()
        if (player == 'r' and computer == 'r') or (player == 'p' and computer == 'p') or (player == 's' and computer == 's'):
            tie()
        if (computer == 'r' and player == 's') or (computer == 's' and player == 'p') or (computer == 'p' and player == 'r'):
            lose()

    def RPS():
        global computer, player

        screen.blit(bg, (0,0))
        screen.blit(Prock, (xb, yb))
        screen.blit(COMrock, ((700-150)- xb, yb))

        Player = MENU_FONT.render("Player", 1, colors.get("black")) # Designate title font and content
        screen.blit(Player, (xb+50, 300)) # Display
        COM = MENU_FONT.render("COM", 1, colors.get("black")) # Designate title font and content
        screen.blit(COM, (WIDTH-(xb+100), 300)) # Display

        # Back button
        Button_Back = pygame.Rect(20, 20, 100, 50)
        pygame.draw.rect(screen, colors.get("red"), Button_Back)
        textBack = MENU_FONT.render("Back", 1, colors.get("black"))
        screen.blit(textBack, (25, 25))
        pygame.display.update()
        pygame.time.delay(50)


        computer = random.choice(['r','p','s']) # random working

        Button_R = pygame.Rect(WIDTH//12, 500, 120, 50)
        Button_P = pygame.Rect(WIDTH//12*5, 500, 120, 50)
        Button_S = pygame.Rect(WIDTH//12*9, 500, 120, 50)
        pygame.draw.rect(screen, colors.get("pink"), Button_R)
        pygame.draw.rect(screen, colors.get("pink"), Button_P)
        pygame.draw.rect(screen, colors.get("pink"), Button_S)

        textR = MENU_FONT.render("Rock", 1, colors.get("black"))
        textP = MENU_FONT.render("Paper", 1, colors.get("black"))
        textS = MENU_FONT.render("Scissors", 1, colors.get("black"))
        screen.blit(textR, (WIDTH//12+30, 510))
        screen.blit(textP, (WIDTH//12*5+30, 510))
        screen.blit(textS, (WIDTH//12*9+30, 510))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    mx = mousePos[0]
                    my = mousePos[1]
                    if Button_Back.collidepoint(mx, my):
                        menu()
                    if Button_R.collidepoint(mx, my):
                        player = 'r'
                        screen.blit(Prock, (xb, yb))
                        pygame.display.update()
                        print(player)
                        if computer == 'r':
                            screen.blit(COMrock, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        if computer == 'p':
                            screen.blit(COMpaper, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        if computer == 's':
                            screen.blit(COMscissor, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        checkwinner()
                    if Button_P.collidepoint(mx, my):
                        player = 'p'
                        screen.blit(Ppaper, (xb, yb))
                        pygame.display.update()
                        print(player)
                        if computer == 'r':
                            screen.blit(COMrock, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        if computer == 'p':
                            screen.blit(COMpaper, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        if computer == 's':
                            screen.blit(COMscissor, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        checkwinner()
                        
                    if Button_S.collidepoint(mx, my):
                        player = 's'
                        screen.blit(Pscissor, (xb, yb))
                        pygame.display.update()
                        print(player)
                        if computer == 'r':
                            screen.blit(COMrock, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        if computer == 'p':
                            screen.blit(COMpaper, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        if computer == 's':
                            screen.blit(COMscissor, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        checkwinner()
                                  

    def maze():
        global isJump, x, jumpCount, y
        print("create a maze")
        pygame.time.delay(200)
        screen.fill("yellow")
        Win = GIANT_FONT.render(("YOU WON!"), 1, colors.get("white"))
        xd = WIDTH//2 - (Win.get_width()//2)
        screen.blit(Win, (xd, 200))\
        
        pygame.display.update() 
        pygame.time.delay(1000)

        def redrawGameWindow():
            global walkCount, hitbox, y
            screen.blit(bg2, (0,0)) # Blit makes things appear on the game screen

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

    def tie():
        print("create tie screen")
        pygame.time.delay(200)
        screen.fill("violet")
        Tie = GIANT_FONT.render(("TIE!"), 1, colors.get("white"))
        xd = WIDTH//2 - (Tie.get_width()//2)
        screen.blit(Tie, (xd, 200))\
        
        pygame.display.update() 
        pygame.time.delay(1000)

        RPS()

    def lose():
        global colors
        print("create lose screen")
        pygame.time.delay(200)
        screen.fill("turquoise")
        Lose = GIANT_FONT.render(("YOU LOST!"), 1, colors.get("white"))
        xd = WIDTH//2 - (Lose.get_width()//2)
        screen.blit(Lose, (xd, 200))\
        
        pygame.display.update() 
        pygame.time.delay(1000)

        RPS()


    Game = True
    while Game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                #Menu(mainTitle,messageMenu)
                pygame.quit()
                sys.exit()
                
        pygame.display.update() 
        pygame.time.delay(100)

        RPS()

# RPS Level 3
def game3():
    print("HI")
    def checkwinner():
        global player, computer
        if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
            maze()
        if (player == 'r' and computer == 'r') or (player == 'p' and computer == 'p') or (player == 's' and computer == 's'):
            tie()
        if (computer == 'r' and player == 's') or (computer == 's' and player == 'p') or (computer == 'p' and player == 'r'):
            lose()

    def RPS():
        global computer, player

        screen.blit(bg, (0,0))
        screen.blit(Prock, (xb, yb))
        screen.blit(COMrock, ((700-150)- xb, yb))

        Player = MENU_FONT.render("Player", 1, colors.get("black")) # Designate title font and content
        screen.blit(Player, (xb+50, 300)) # Display
        COM = MENU_FONT.render("COM", 1, colors.get("black")) # Designate title font and content
        screen.blit(COM, (WIDTH-(xb+100), 300)) # Display

        # Back button
        Button_Back = pygame.Rect(20, 20, 100, 50)
        pygame.draw.rect(screen, colors.get("red"), Button_Back)
        textBack = MENU_FONT.render("Back", 1, colors.get("black"))
        screen.blit(textBack, (25, 25))
        pygame.display.update()
        pygame.time.delay(50)


        computer = random.choice(['r','p','s']) # random working

        Button_R = pygame.Rect(WIDTH//12, 500, 120, 50)
        Button_P = pygame.Rect(WIDTH//12*5, 500, 120, 50)
        Button_S = pygame.Rect(WIDTH//12*9, 500, 120, 50)
        pygame.draw.rect(screen, colors.get("pink"), Button_R)
        pygame.draw.rect(screen, colors.get("pink"), Button_P)
        pygame.draw.rect(screen, colors.get("pink"), Button_S)

        textR = MENU_FONT.render("Rock", 1, colors.get("black"))
        textP = MENU_FONT.render("Paper", 1, colors.get("black"))
        textS = MENU_FONT.render("Scissors", 1, colors.get("black"))
        screen.blit(textR, (WIDTH//12+30, 510))
        screen.blit(textP, (WIDTH//12*5+30, 510))
        screen.blit(textS, (WIDTH//12*9+30, 510))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    mx = mousePos[0]
                    my = mousePos[1]
                    if Button_Back.collidepoint(mx, my):
                        menu()
                    if Button_R.collidepoint(mx, my):
                        player = 'r'
                        screen.blit(Prock, (xb, yb))
                        pygame.display.update()
                        print(player)
                        if computer == 'r':
                            screen.blit(COMrock, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        if computer == 'p':
                            screen.blit(COMpaper, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        if computer == 's':
                            screen.blit(COMscissor, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        checkwinner()
                    if Button_P.collidepoint(mx, my):
                        player = 'p'
                        screen.blit(Ppaper, (xb, yb))
                        pygame.display.update()
                        print(player)
                        if computer == 'r':
                            screen.blit(COMrock, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        if computer == 'p':
                            screen.blit(COMpaper, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        if computer == 's':
                            screen.blit(COMscissor, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        checkwinner()
                        
                    if Button_S.collidepoint(mx, my):
                        player = 's'
                        screen.blit(Pscissor, (xb, yb))
                        pygame.display.update()
                        print(player)
                        if computer == 'r':
                            screen.blit(COMrock, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        if computer == 'p':
                            screen.blit(COMpaper, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        if computer == 's':
                            screen.blit(COMscissor, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        checkwinner()
                                  

    def maze():
        global isJump, x, jumpCount, y
        print("create a maze")
        pygame.time.delay(200)
        screen.fill("yellow")
        Win = GIANT_FONT.render(("YOU WON!"), 1, colors.get("white"))
        xd = WIDTH//2 - (Win.get_width()//2)
        screen.blit(Win, (xd, 200))\
        
        pygame.display.update() 
        pygame.time.delay(1000)

        def redrawGameWindow():
            global walkCount, hitbox, y
            screen.blit(bg2, (0,0)) # Blit makes things appear on the game screen

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

    def tie():
        print("create tie screen")
        pygame.time.delay(200)
        screen.fill("violet")
        Tie = GIANT_FONT.render(("TIE!"), 1, colors.get("white"))
        xd = WIDTH//2 - (Tie.get_width()//2)
        screen.blit(Tie, (xd, 200))\
        
        pygame.display.update() 
        pygame.time.delay(1000)

        RPS()

    def lose():
        global colors
        print("create lose screen")
        pygame.time.delay(200)
        screen.fill("turquoise")
        Lose = GIANT_FONT.render(("YOU LOST!"), 1, colors.get("white"))
        xd = WIDTH//2 - (Lose.get_width()//2)
        screen.blit(Lose, (xd, 200))\
        
        pygame.display.update() 
        pygame.time.delay(1000)

        RPS()


    Game = True
    while Game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                #Menu(mainTitle,messageMenu)
                pygame.quit()
                sys.exit()
                
        pygame.display.update() 
        pygame.time.delay(100)

        RPS()

# Leaderboard
def scoreboard():
    #title font
    screen.fill(colorTheme)
    Title = TITLE_FONT.render("Leaderboard", 1, colors.get("black"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))\

    # Open Scoreboard File
    myFile = open("PygameFile.py\SettingMenu\SMscore.txt", "r")
    content = myFile.readlines()


    # Print instructions
    li = 150 
    for line in content:
        Scores = MENU_FONT.render(line[0:-1], 1, colors.get('black')) 
        screen.blit(Scores, (40, li))
        pygame.display.update()
        pygame.time.delay(1000)
        li += 40 # Add 40 pixels between each printed line

    myFile.close()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu()

# Exit
def exit():
    print("here")
    screen.fill(colorTheme)
    Title = TITLE_FONT.render("Bye Bye", 1, colors.get("black"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 250))
    pygame.display.update()
    pygame.time.delay(1000)

    if high > 50:
            myFile = open("PygameFile\MenuScore.txt", 'a')
            date=datetime.datetime.now()
            scrLine = str(high) + "\t"+ date.strftime("%m-%d-%Y")+ "\n"
            myFile.write(scrLine)
            myFile.close()    

    pygame.quit()
    sys.quit()
    print("you quit")

# Call functions
user()
menu()
