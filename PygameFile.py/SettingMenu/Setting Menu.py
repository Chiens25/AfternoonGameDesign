# Sydney Chien
# 06/14/2022

import pygame, os, time, random, math, datetime, sys
from pygame import mixer
pygame.init()


# print(pygame.font.get_fonts())
# pygame.time.delay(10000)
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)

os.system('cls')

# General Variables
WIDTH = 700   # Amount of pixels
w3 = WIDTH//3
HEIGHT = 700
colors = {"white":(255,255,255), "grey":(245,245,245), "black":(0,0,0), "red":(255,0,0), "green":(0,255,0), "blue":(0,0,255), "pink":(204,0,204), "orange":(255,128,0), "yellow":(255,255,0), "purple":(127,0,255)}
clr = colors.get("white")
game = 0
#create a display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game") # title of the window

blueClr = (0,0,255)
redClr = (255,0,0)
cyanClr = (0, 255, 177)

#images
bg = pygame.image.load("PygameFile.py\Images\\bgSmaller.jpg")
char = pygame.image.load("PygameFile.py\Images\PixelArtTutorial.png")
char = pygame.transform.scale(char, (50,50))
# screen.blit(bg, (0,0))
# pygame.display.update()
# pygame.time.delay(5000)

#circle var
cx = 350
cy = 350
rad = 25

#square var
hb = 50
wb = 50
xb = 325
yb = 325
square = pygame.Rect(xb,yb,wb,hb) #create the object to draw

#char var
charx = xb
chary = yb

mx = 0
my = 0

#inscribed square
ibox = rad*math.sqrt(2)
xig = cx-(ibox/2)
yig = cy-(ibox/2)
insSquare = pygame.Rect(xig,yig,ibox,ibox)

#bounce
mountainSquare = pygame.Rect(250, 320, 180, 250)

#Game Variables
speed = 2
run = True
background = colors.get("grey")
colorTheme = colors.get("white")
mixer.music.load('PygameFile.py\journey.wav')
mixer.music.play(-1)

def settings():
    global screen
    global colorTheme, mx, my
    screen.fill(colorTheme)
    Title = TITLE_FONT.render("Settings", 1, colors.get("black"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 10))

    # Color Settings
    ColorTheme = MENU_FONT.render("Background Color:", 1, colors.get("black"))
    screen.blit(ColorTheme, (w3, 70))
    pygame.display.update()
    pygame.time.delay(50)

    # Color Backgrounds
    Button_White = pygame.Rect(w3, 100, 230, 50)
    Button_Orange = pygame.Rect(w3, 170, 230, 50)
    Button_Purple = pygame.Rect(w3, 240, 230, 50)
    pygame.draw.rect(screen, colors.get("grey"), Button_White)
    pygame.draw.rect(screen, colors.get("orange"), Button_Orange)
    pygame.draw.rect(screen, colors.get("purple"), Button_Purple)

    # Name Color Backgrounds
    textWhite = MENU_FONT.render("White", 1, colors.get("black"))
    textOrange = MENU_FONT.render("Orange", 1, colors.get("black"))
    textPurple = MENU_FONT.render("Purple", 1, colors.get("black"))
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

    Button_Size1 = pygame.Rect(w3, 350, 230, 50)
    Button_Size2 = pygame.Rect(w3, 420, 230, 50)
    Button_Size3 = pygame.Rect(w3, 490, 230, 50)

    pygame.draw.rect(screen, colors.get("grey"), Button_Size1)
    pygame.draw.rect(screen, colors.get("grey"), Button_Size2)
    pygame.draw.rect(screen, colors.get("grey"), Button_Size3)

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

    Button_SoundY = pygame.Rect(WIDTH * .3, 550, 120, 120)
    Button_SoundN = pygame.Rect(WIDTH * .6, 550, 120, 120)
    

    pygame.draw.rect(screen, colors.get("grey"), Button_SoundY)
    pygame.draw.rect(screen, colors.get("grey"), Button_SoundN)
  

    textSoundY = MENU_FONT.render("On", 1, colors.get("black"))
    textSoundN= MENU_FONT.render("Off", 1, colors.get("black"))
    screen.blit(textSoundY, (WIDTH * .3, 560))
    screen.blit(textSoundN, (WIDTH * .6, 560))
    pygame.display.update()
    pygame.time.delay(50)

    # Make Color Backgrounds Change Color Var, Change WIDTH and HEIGHT Var
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
                    colorTheme = "orange"
                if Button_Purple.collidepoint(mx, my):
                    colorTheme = "purple"
                if Button_Back.collidepoint(mx, my):
                    menu()
                if Button_Size1.collidepoint(mx, my):
                    WIDTH == 700
                    HEIGHT = 700
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
                if Button_Size2.collidepoint(mx, my):
                    print("here")
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

                    

# Menu
def menu():
    screen.fill(colorTheme)
    Title = TITLE_FONT.render("Menu", 1, colors.get("black")) # Create a title
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    
    #creating buttons
    Button_Instruct = pygame.Rect(WIDTH//3, 200, 230, 50)
    Button_Settings = pygame.Rect(WIDTH//3, 270, 230, 50)
    Button_Game1 = pygame.Rect(WIDTH//3, 340, 230, 50)
    Button_Game2 = pygame.Rect(WIDTH//3, 410, 230, 50)
    Button_Score = pygame.Rect(WIDTH//3, 480, 230, 50)
    Button_Ex = pygame.Rect(WIDTH//3, 550, 230, 50)
    pygame.draw.rect(screen, colors.get("pink"), Button_Instruct)
    pygame.draw.rect(screen, colors.get("pink"), Button_Settings)
    pygame.draw.rect(screen, colors.get("pink"), Button_Game1)
    pygame.draw.rect(screen, colors.get("pink"), Button_Game2)
    pygame.draw.rect(screen, colors.get("pink"), Button_Score)
    pygame.draw.rect(screen, colors.get("pink"), Button_Ex)
    
    #render 
    textInstruct = MENU_FONT.render("Instructions", 1, colors.get("black"))
    textSett = MENU_FONT.render("Settings", 1, colors.get("black"))
    textGame1 = MENU_FONT.render("Game 1", 1, colors.get("black"))
    textGame2 = MENU_FONT.render("Game 2", 1, colors.get("black"))
    textScore = MENU_FONT.render("Scoreboard", 1, colors.get("black"))
    textEx = MENU_FONT.render("Exit", 0, colors.get("black"))
    screen.blit(textInstruct, (WIDTH//3, 200))
    screen.blit(textSett, (WIDTH//3, 270))
    screen.blit(textGame1, (WIDTH//3, 340))
    screen.blit(textGame2, (WIDTH//3, 410))
    screen.blit(textScore, (WIDTH//3, 480))
    screen.blit(textEx, (WIDTH//3, 550))
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
                if Button_Instruct.collidepoint(mx, my):
                    instruction()
                if Button_Settings.collidepoint(mx, my):
                    settings()
                if Button_Game1.collidepoint(mx, my):
                    game1()
                if Button_Game2.collidepoint(mx, my):
                    game2()
                if Button_Score.collidepoint(mx, my):
                    scoreboard()
                if Button_Ex.collidepoint(mx, my):
                    exit()

def instruction():
    #title font
    screen.fill(colorTheme)
    Title = TITLE_FONT.render("Instructions", 1, colors.get("black"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))\

    #Instructions File
    myFile = open("PygameFile.py\instructions.txt", "r")
    content = myFile.readlines()

    #print instructions
    yi = 150
    for line in content:
        Insctruc = MENU_FONT.render(line[0:-1], 1, colors.get('black'))
        screen.blit(Insctruc, (40, yi))
        pygame.display.update()
        pygame.time.delay(50)
        yi += 40
    
    #creating buttons
    Button_1 = pygame.Rect(200, 400, 100, 50)
    Button_2 = pygame.Rect(400, 400, 100, 50)
    pygame.draw.rect(screen, colors.get("pink"), Button_1)
    pygame.draw.rect(screen, colors.get("pink"), Button_2)

    #render yes and no
    text1 = MENU_FONT.render("Yes", 1, colors.get("black"))
    text2 = MENU_FONT.render("No", 1, colors.get("black"))
    screen.blit(text1, (225, 410))
    screen.blit(text2, (425, 410))
    pygame.display.update()
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

# Game 2
def game2():
    global insSquare, rad, yb, xb
    score = 0
    screen.fill(colors.get('white'))
    pygame.display.update()
    Game=True
    while Game:
        screen.blit(bg, (0,0))
        # screen.fill(backgrnd)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                menu()
        keys= pygame.key.get_pressed() #this is a list
        #mve square
        if keys[pygame.K_RIGHT] and square.x < WIDTH -(wb):
            square.x += speed
            xb += speed
        if keys[pygame.K_LEFT] and  square.x > speed:
            square.x -= speed
            xb -= speed
        if keys[pygame.K_UP] and square.y >speed:   #means clser t 0
            square.y -= speed
            yb -= speed
        if keys[pygame.K_DOWN] and square.y <HEIGHT -hb:  #means clser t max value HEIGHT
            square.y += speed
            yb += speed
            #mve Circle
        if keys[pygame.K_d] and cx < WIDTH -(rad):
            cx += speed
            insSquare.x += speed
        if keys[pygame.K_a] and  cx > (speed+rad):
            cx -= speed
            insSquare.x -= speed
        if keys[pygame.K_w] and cy >(speed+rad):   #means clser t 0
            cy -= speed
            insSquare.y -= speed
        if keys[pygame.K_s] and cy <HEIGHT -(rad):  #means clser t max value HEIGHT
            cy += speed
            insSquare.y += speed

        if square.colliderect(insSquare):
            print("BOOM")
            rad+=1
            cx=random.randint(rad, WIDTH-rad)
            cy=random.randint(rad, HEIGHT-rad)
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            score += 1
            insSquare=pygame.Rect(xig,yig,ibox,ibox)

        #rect(surface, color, rect) -> Rect
        pygame.draw.rect(screen, colors.get("red"),square)
        screen.blit(char, (xb, yb))
        #circle(surface, color, center, radius)
        pygame.draw.circle(screen, colors.get("red"), (cx,cy), rad)
        pygame.draw.rect(screen, colors.get("red"), insSquare)
        pygame.display.update()
        pygame.time.delay(5)

# Game 1
def game1():
    global insSquare, rad, yb, xb
    score = 0

    screen.fill(colors.get('white'))

    pygame.display.update()

    Game=True
    while Game:
        screen.fill(colors.get('white'))
        # screen.fill(backgrnd)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                menu()
                
        keys= pygame.key.get_pressed() #this is a list
        #mve square
        if keys[pygame.K_RIGHT] and square.x < WIDTH -(wb):
            square.x += speed
            xb += speed
        if keys[pygame.K_LEFT] and  square.x > speed:
            square.x -= speed
            xb -= speed
        if keys[pygame.K_UP] and square.y >speed:   #means clser t 0
            square.y -= speed
            yb -= speed
        if keys[pygame.K_DOWN] and square.y <HEIGHT -hb:  #means clser t max value HEIGHT
            square.y += speed
            yb += speed
            #mve Circle
        if keys[pygame.K_d] and cx < WIDTH -(rad):
            cx += speed
            insSquare.x += speed
        if keys[pygame.K_a] and  cx > (speed+rad):
            cx -= speed
            insSquare.x -= speed
        if keys[pygame.K_w] and cy >(speed+rad):   #means clser t 0
            cy -= speed
            insSquare.y -= speed
        if keys[pygame.K_s] and cy <HEIGHT -(rad):  #means clser t max value HEIGHT
            cy += speed
            insSquare.y += speed

        if square.colliderect(insSquare):
            print("BOOM")
            rad+=1
            cx=random.randint(rad, WIDTH-rad)
            cy=random.randint(rad, HEIGHT-rad)
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            score += 1
            insSquare=pygame.Rect(xig,yig,ibox,ibox)

        #rect(surface, color, rect) -> Rect
        pygame.draw.rect(screen, blueClr,square)
        #circle(surface, color, center, radius)
        pygame.draw.circle(screen, cyanClr, (cx,cy), rad)
        pygame.draw.rect(screen, cyanClr, insSquare)
        pygame.display.update()
        pygame.time.delay(5)
    score = 0

    screen.fill(colors.get('white'))

    pygame.display.update()

    Game=True
    while Game:
        screen.fill(colors.get('white'))
        # screen.fill(backgrnd)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                menu()
                
        keys= pygame.key.get_pressed() #this is a list
        #mve square
        if keys[pygame.K_RIGHT] and square.x < WIDTH -(wb):
            square.x += speed
            xb += speed
        if keys[pygame.K_LEFT] and  square.x > speed:
            square.x -= speed
            xb -= speed
        if keys[pygame.K_UP] and square.y >speed:   #means clser t 0
            square.y -= speed
            yb -= speed
        if keys[pygame.K_DOWN] and square.y <HEIGHT -hb:  #means clser t max value HEIGHT
            square.y += speed
            yb += speed
            #mve Circle
        if keys[pygame.K_d] and cx < WIDTH -(rad):
            cx += speed
            insSquare.x += speed
        if keys[pygame.K_a] and  cx > (speed+rad):
            cx -= speed
            insSquare.x -= speed
        if keys[pygame.K_w] and cy >(speed+rad):   #means clser t 0
            cy -= speed
            insSquare.y -= speed
        if keys[pygame.K_s] and cy <HEIGHT -(rad):  #means clser t max value HEIGHT
            cy += speed
            insSquare.y += speed

        if square.colliderect(insSquare):
            print("BOOM")
            rad+=1
            cx=random.randint(rad, WIDTH-rad)
            cy=random.randint(rad, HEIGHT-rad)
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            score += 1
            insSquare=pygame.Rect(xig,yig,ibox,ibox)

        #rect(surface, color, rect) -> Rect
        pygame.draw.rect(screen, blueClr,square)
        #circle(surface, color, center, radius)
        pygame.draw.circle(screen, cyanClr, (cx,cy), rad)
        pygame.draw.rect(screen, cyanClr, insSquare)
        pygame.display.update()
        pygame.time.delay(5)


def scoreboard():
     #title font
    screen.fill(colorTheme)
    Title = TITLE_FONT.render("Scoreboard", 1, colors.get("black"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))\

    #Instructions File
    myFile = open("PygameFile.py\\instructions.txt", "r")
    content = myFile.readlines()

    #print instructions
    li = 150
    for line in content:
        Scores = MENU_FONT.render(line[0:-1], 1, colors.get('black'))
        screen.blit(Scores, (40, li))
        pygame.display.update()
        pygame.time.delay(50)
        li += 40
    


def exit():
    print("here")
    screen.fill(colorTheme)
    Title = TITLE_FONT.render("Bye Bye", 1, colors.get("black"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 250))
    pygame.display.update()
    pygame.time.delay(1000)

    #if high > 50:
            #myFile = open("PygameFile\MenuScore.txt", 'a')
            #date=datetime.datetime.now()
            #scrLine = str(high) + "\t"+ date.strftime("%m-%d-%Y")+ "\n"
            #myFile.write(scrLine)
            #myFile.close()    

    pygame.quit()
    sys.quit()
    print("you quit")
        
menu()
