# Sydney Chien
# 06/14/2022

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
high = 0
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

# User Name
def user():
    background = (255,255,255)
    screen.fill(background)
    pygame.display.update()
    pygame.time.delay(500)

    # Create title
    # Create Box, Relative to WIDTH and HEIGHT


    input_rect = pygame.Rect(WIDTH//3, HEIGHT//3, 200, 50)
    pygame.draw.rect(screen, colors.get("pink"), input_rect)

    pygame.display.update()
    pygame.time.delay(500)


    Title = TITLE_FONT.render("Enter Name", 1, colors.get("black"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 10))
    pygame.display.update()
    pygame.time.delay(500)

    userName = ""

    run = True
    while run:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Menu
                    print(userName)
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print(userName)
                        menu()
                    if event.key == pygame.K_BACKSPACE:
                        userName = userName[:-1]
                    else:
                        userName += event.unicode # Gives you all characters
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


gameOver=False # Check if game is over
Xcount = 0
Ocount = 0

# Game 2
def game2():
    global gameOver
    print("I am here")
    #game Variable
    player=1 # CONTROL player 1 is X and -1 is O
    markers=[] # Array to control the plays
    lineWidth=10 # Line thinkness
    Game=True # Control Main Game
    MxMy=(0,0) # Checks Click
    
    winner = 0 # Who WON the game 1, -1, 0 (TIE)

    print(markers)  
    # Function to set our Array to 0
    def zero_Array(): 
        for x in range(3):
            row= [0] *3
            markers.append(row)

    # Function to draw the Grid lines
    def draw_grid():
        lineClr=colors.get("white")
        for x in range(1,3):
            pygame.draw.line(screen,lineClr,(0,HEIGHT//3*x),(WIDTH,HEIGHT//3*x),lineWidth)  #Hztal line
            pygame.draw.line(screen,lineClr,(WIDTH//3*x, 0),(WIDTH//3*x,HEIGHT),lineWidth)  #Vert line
        pygame.time.delay(100)
    # Function to draw X and O markers
    def draw_Markers():
        cirClr=colors.get("blue") # Color for the Circle
        xClr=colors.get("black") # Color for the X
        xValue=0
        for x in markers:   # getting a rw
            yValue=0
            for y in x:  #each elem fthe rw
                if y ==1:
                    pygame.draw.line(screen,xClr,(xValue * WIDTH//3 + 15, yValue * HEIGHT//3 + 15), (xValue * WIDTH//3 + WIDTH//3-15, yValue * WIDTH//3 + WIDTH//3-15),lineWidth)
                    pygame.draw.line(screen, xClr,(xValue*WIDTH//3 +WIDTH//3-15, yValue*HEIGHT//3+15),(xValue *WIDTH//3+15,yValue*HEIGHT//3+HEIGHT//3-15),lineWidth)
                if y==-1:
                    pygame.draw.circle(screen,cirClr,(xValue*WIDTH//3+WIDTH//6,yValue*HEIGHT//3 +HEIGHT//6),WIDTH//6-15, lineWidth)
                yValue +=1
            xValue +=1
        pygame.display.update() 

    def Xwinnerult():
        screen.fill("YELLOW")
        Title = TITLE_FONT.render(("PLAYER 1 IS THE CHAMPION"), 1, colors.get("white"))
        xd = WIDTH//2 - (Title.get_width()//2)
        screen.blit(Title, (xd, 50))\
        
        pygame.time.delay(1000)
        pygame.display.update()

    def Owinnerult():
        screen.fill("YELLOW")
        Title = TITLE_FONT.render(("PLAYER 2 IS THE CHAMPION"), 1, colors.get("white"))
        xd = WIDTH//2 - (Title.get_width()//2)
        screen.blit(Title, (xd, 50))\
        
        pygame.time.delay(1000)
        pygame.display.update()
                        

            

    Xcount=0
    Ocount=0

    def checkWinner():
        global Xcount, Ocount, gameOver, winner
        X_POS = 0
        for row in markers: # CHECK COLUMNS
            if sum(row) == 3:
                winner = 1
                gameOver = True
                
        for row in markers: # CHECK COLUMNS
            if sum(row) == -3:
                winner = -1
                gameOver = True
                
        # CHECK DIAGONALS
        if markers [0][X_POS] + markers [1][X_POS] + markers [2][X_POS] == 3:# Check COLUMNS 
            winner = 1
            gameOver = True
            
        if markers [0][X_POS] + markers [1][X_POS] + markers [2][X_POS] == -3:  
            winner = -1
            gameOver = True
            

        if markers [0][0] + markers [1][1] + markers [2][2] == 3:
            winner = 1
            gameOver = True
            
            
        if markers [2][0] + markers [1][1] + markers [0][2] == 3: 
            winner = 1
            gameOver = True
            

        if markers [0][0] + markers [1][1] + markers [2][2] == -3: 
            winner = -1
            gameOver = True
            
        if markers [2][0] + markers [1][1] + markers [0][2] == -3:
            winner = -1
            gameOver = True
            
        # Check for CAT GAME
        if gameOver == False: # BOOLEAN = Not gameOver
            tie = True
            for ROW in markers:
                for COL in ROW:
                    if COL == 0:
                        tie = False
            if tie: 
                gameOver = True
                winner = 0
                

    


    def gameEnd():
        global markers, Xcount, Ocount, winner
        markers = []
        zero_Array()

        if winner == 1:
            Xcount+=1
            Xwin = GIANT_FONT.render("X WINS", 1, "white")
            screen.fill("red")
            screen.blit(Xwin, (WIDTH//4, 50))\

            pygame.time.delay(1000)
            pygame.display.update()

        if winner == -1:
            Ocount+=1
            Owin = GIANT_FONT.render("O WINS", 1, "white")
            screen.fill("red")
            screen.blit(Owin, (WIDTH//4, 50))\

            pygame.time.delay(1000)
            pygame.display.update()
        
        if winner == 0:
            Tie = GIANT_FONT.render("XO TIE GAME", 1, "white")
            screen.fill("red")
            screen.blit(Tie, (WIDTH//4, 50))\

            pygame.time.delay(1000)
            pygame.display.update()

        if Xcount == 3:
            Xcount = 0
            Ocount = 0
            Xwinnerult()
        if Ocount == -3:
            Xcount = 0
            Ocount = 0
            Owinnerult()
    
        PlayAgain = MENU_FONT.render("Play Again?:", 1, colors.get("white"))
        screen.blit(PlayAgain, (WIDTH//8, 300))
        pygame.display.update()
        pygame.time.delay(50)
        #creating buttons
        Button_1 = pygame.Rect(200, 400, 100, 50)
        Button_2 = pygame.Rect(400, 400, 100, 50)
        pygame.draw.rect(screen, colors.get("pink"), Button_1)
        pygame.draw.rect(screen, colors.get("pink"), Button_2)

        #render yes and no
        text1 = MENU_FONT.render("Yes", 1, colors.get("white"))
        text2 = MENU_FONT.render("No", 1, colors.get("white"))
        screen.blit(text1, (225, 410))
        screen.blit(text2, (425, 410))
        pygame.display.update()
        run = True
        while run:
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
                        markers.clear()
                        markers = []
                        zero_Array()
                        run = False


                    if Button_2.collidepoint(mx, my):
                        pygame.quit()
                        sys.quit()
                        print("you quit")

    zero_Array()
    print()

    while Game:
        screen.fill("pink")
        draw_grid()
        draw_Markers()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                #Menu(mainTitle,messageMenu)
                pygame.quit()
                sys.exit()
                print("You quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                MxMy = pygame.mouse.get_pos()
                cellx=MxMy[0]//(WIDTH//3)
                celly=MxMy[1]//(HEIGHT//3)
                print(cellx, celly)
                if markers[cellx][celly]==0:
                    markers[cellx][celly]=player
                    player *=-1
                    checkWinner()
                    if gameOver:
                        print("Game Over")
                        gameOver = False
                        gameEnd()
                        print("Game Over")

                

                
            
            
            
    pygame.display.update() 
    pygame.time.delay(100)

# Game 1
def game1():
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

    #rect(surface, color, object)
    pygame.draw.rect(screen, colors.get("blue"), square)
    pygame.draw.rect(screen, colors.get("blue"), insSquare)

    #circle(surface, color, center, radius)
    pygame.draw.circle(screen, colors.get("red"), (cx, cy), rad)
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

    if high > 50:
            myFile = open("PygameFile\MenuScore.txt", 'a')
            date=datetime.datetime.now()
            scrLine = str(high) + "\t"+ date.strftime("%m-%d-%Y")+ "\n"
            myFile.write(scrLine)
            myFile.close()    

    pygame.quit()
    sys.quit()
    print("you quit")

user()
menu()
