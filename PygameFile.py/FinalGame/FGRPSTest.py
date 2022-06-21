# Sydney Chien
# 6/20/22
# Figure out how to create a RPS and Maze game 
# Paste confirmed progress into actual game
# Integrate new color scheme

import pygame, os, time, random, math, datetime, sys
from pygame import mixer
pygame.init()

# print(pygame.font.get_fonts())
# pygame.time.delay(10000)
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)
GIANT_FONT = pygame.font.SysFont('comicsans', 100)

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


#images
bg = pygame.image.load("PygameFile.py\FinalGame\FGImages\BoxingRing.jpg")
bg = pygame.transform.scale(bg, (WIDTH,HEIGHT))
rock = pygame.image.load("PygameFile.py\FinalGame\FGImages\Rock Image.png")
rock = pygame.transform.scale(rock, (150,150)) 
Prock = pygame.transform.rotate(rock, 270) 
COMrock =  pygame.transform.flip(Prock, True, False)
paper = pygame.image.load("PygameFile.py\FinalGame\FGImages\Paper Image.png")
paper = pygame.transform.scale(paper, (150,150)) 
Ppaper = pygame.transform.rotate(paper, 270) 
COMpaper =  pygame.transform.flip(Ppaper, True, False)
scissor = pygame.image.load("PygameFile.py\FinalGame\FGImages\Scissor Image.png")
scissor = pygame.transform.scale(scissor, (150,150)) 
Pscissor = pygame.transform.rotate(scissor, 270) 
COMscissor =  pygame.transform.flip(Pscissor, True, False)


# RPS Positioning Var
xb = 100
yb = 325

mx = 0
my = 0

#Game Variables
speed = 2
run = True
high = 0
background = colors.get("grey")
colorTheme = colors.get("white")
mixer.music.load('PygameFile.py\journey.wav')
mixer.music.play(-1)

# DONT PUT IN FINAL CODE !!!!
def menu():
    print("menu")

Pcount = 0
COMcount = 0
player = 'r'

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
    print("create a maze")
    screen.fill("yellow")
    Win = GIANT_FONT.render(("YOU WON!"), 1, colors.get("white"))
    xd = WIDTH//2 - (Win.get_width()//2)
    screen.blit(Win, (xd, 200))\
    
    pygame.display.update() 
    pygame.time.delay(1000)

def tie():
    global colors
    print("create tie screen")
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

