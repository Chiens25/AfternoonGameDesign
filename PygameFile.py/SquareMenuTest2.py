# Sydney Chien
# 06/14/2022


from cgitb import text
from locale import CHAR_MAX
from re import T
from xml.etree.ElementTree import TreeBuilder
import pygame, os, time, random, math, datetime
pygame.init()


# print(pygame.font.get_fonts())
# pygame.time.delay(10000)
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)

os.system('cls')

# General Variables
WIDTH = 700#amount of pixels
HEIGHT = 700
colors = {"white":(255,255,255), "grey":(96,96,96), "black":(0,0,0), "red":(255,0,0), "green":(0,255,0), "blue":(0,0,255), "pink":(204,0,204), "orange":(255,128,0), "yellow":(255,255,0), "purple":(127,0,255)}
clr = colors.get("white")
game = 0
#create a display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game") # title of the window

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

#inscribed square
ibox = rad*math.sqrt(2)
xig = cx-(ibox/2)
yig = cy-(ibox/2)
insSquare=pygame.Rect(xig,yig,ibox,ibox)

#bounce
mountainSquare = pygame.Rect(250, 320, 180, 250)

#Game Variables
speed = 2
run = True
background = colors.get("grey")


def settings():
    screen.fill(colors.get("white"))
    Title = TITLE_FONT.render("Settings", 1, colors.get("black"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))

    # Color Settings
    ColorTheme = MENU_FONT.render("Color Theme:", 1, colors.get("black"))

    # Color Buttons
    Button_Pink = pygame.Rect(100, 400, 100, 50)
    Button_Orange = pygame.Rect(300, 400, 100, 50)
    Button_Purple = pygame.Rect(500, 400, 100, 50)
    pygame.draw.rect(screen, colors.get("pink"), Button_Pink)
    pygame.draw.rect(screen, colors.get("orange"), Button_Orange)
    pygame.draw.rect(screen, colors.get("purple"), Button_Purple)

    # Name Color Buttons
    textPink = MENU_FONT.render("Pink", 1, colors.get("black"))
    textOrange = MENU_FONT.render("Orange", 1, colors.get("black"))
    textPurple = MENU_FONT.render("Purple", 1, colors.get("black"))
    screen.blit(textPink, (125, 410))
    screen.blit(textOrange, (325, 410))
    screen.blit(textPurple, (525, 410))
    pygame.display.update()
    pygame.time.delay(100000)

    # Make Color Buttons Change Colors of Theme
    while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    print("you quit")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    mx = mousePos[0]
                    my = mousePos[1]
                if Button_Pink.collidepoint(mx, my):
                    colorTheme = "pink"
                if Button_Orange.collidepoint(mx, my):
                    colorTheme = "orange"
                if Button_Purple.collidepoint(mx, my):
                    colorTheme = "purple"
                else: 
                    colorTheme = "pink"
                    


def menu():
    screen.fill(colors.get("white"))
    Title = TITLE_FONT.render("Menu", 1, colors.get("black")) # Create a title
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    
    #creating buttons
    Button_Instruct = pygame.Rect(200, 400, 100, 50)
    Button_Settings = pygame.Rect(400, 400, 100, 50)
    Button_Game1 = pygame.Rect(200, 500, 100, 50)
    Button_Game2 = pygame.Rect(400, 500, 100, 50)
    Button_Score = pygame.Rect(200, 600, 100, 50)
    Button_Ex = pygame.Rect(400, 600, 100, 50)
    pygame.draw.rect(screen, colors.get("colorTheme"), Button_Instruct)
    pygame.draw.rect(screen, colors.get("colorTheme"), Button_Settings)
    pygame.draw.rect(screen, colors.get("colorTheme"), Button_Game1)
    pygame.draw.rect(screen, colors.get("colorTheme"), Button_Game2)
    pygame.draw.rect(screen, colors.get("colorTheme"), Button_Score)
    pygame.draw.rect(screen, colors.get("colorTheme"), Button_Ex)
    
    #render 
    textInstruct = MENU_FONT.render("Instructions", 1, colors.get("black"))
    textSett = MENU_FONT.render("Settings", 1, colors.get("black"))
    textGame1 = MENU_FONT.render("Game 1", 1, colors.get("black"))
    textGame2 = MENU_FONT.render("Game 2", 1, colors.get("black"))
    textScore = MENU_FONT.render("Scoreboard", 1, colors.get("black"))
    textEx = MENU_FONT.render("Exit", 0, colors.get("black"))
    screen.blit(textInstruct, (225, 410))
    screen.blit(textSett, (425, 410))
    screen.blit(textGame1, (225, 510))
    screen.blit(textGame2, (425, 510))
    screen.blit(textScore, (225, 610))
    screen.blit(textEx, (425, 610))
    pygame.display.update()
    pygame.time.delay(100000)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                print("you quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_Instruct.collidepoint(mx, my):
                    instruction()
                if Button_Settings.collidepoint(mx, my):
                    settings()
                if Button_Game1.collidepoint(mx, my):
                    return True 
                    game = 1
                if Button_Game2.collidepoint(mx, my):
                    return True
                    game = 2
                if Button_Score.collidepoint(mx, my):
                    instruction()
                if Button_Ex.collidepoint(mx, my):
                    exit()

def instruction():
    #title font
    screen.fill(colors.get("white"))
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
    pygame.draw.rect(screen, colors.get("colorTheme"), Button_1)
    pygame.draw.rect(screen, colors.get("colorTheme"), Button_2)

    #render yes and no
    text1 = MENU_FONT.render("Yes", 1, colors.get("black"))
    text2 = MENU_FONT.render("No", 1, colors.get("black"))
    screen.blit(text1, (225, 410))
    screen.blit(text2, (425, 410))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                print("you quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_1.collidepoint(mx, my):
                    return True
                    game = 1
                if Button_2.collidepoint(mx, my):
                    menu()

#functions
menu()
run = instruction()

# Game 2
while run and game == 2:
    # screen.fill(background)
    pygame.draw.rect(screen, colors.get("white"), mountainSquare)
    screen.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print("you quit")
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            # print(mousePos)
    keys = pygame.key.get_pressed() #allow us to see what key was pressed

    

    #square movement
    if keys[pygame.K_d] and square.x < WIDTH-wb:
        square.x += speed
        charx += speed
    if keys[pygame.K_a] and square.x > 0:
        square.x -= speed
        charx -= speed
    if keys[pygame.K_s] and square.y < HEIGHT-hb:
        square.y += speed
        chary += speed
    if keys[pygame.K_w] and square.y > 0:
        square.y -= speed
        chary -= speed

    #circle and inscribed square movement
    if keys[pygame.K_RIGHT] and cx < WIDTH-rad:
        cx += speed
        insSquare.x += speed
    if keys[pygame.K_LEFT] and cx > 0+rad:
        cx -= speed
        insSquare.x -= speed
    if keys[pygame.K_DOWN] and cy < HEIGHT-rad:
        cy += speed
        insSquare.y += speed
    if keys[pygame.K_UP] and cy > 0+rad:
        cy -= speed
        insSquare.y -= speed
    
    #circle square collide
    if square.colliderect(insSquare): 
        print("BOOM")
        cx = random.randint(rad, WIDTH-rad)
        cy = random.randint(rad, HEIGHT-rad)
        rad += 5
        ibox = rad*math.sqrt(2)
        xig = cx-(ibox/2)
        yig = cy-(ibox/2)
        insSquare=pygame.Rect(xig,yig,ibox,ibox)
    
    #mountain collide square
    if square.colliderect(mountainSquare):
        square.x = 10
        square.y = 10
        charx = 10
        chary = 10
    
    #mountain collide circle
    if insSquare.colliderect(mountainSquare):
        cx = rad + 10
        cy = rad + 10
        ibox = rad*math.sqrt(2)
        xig = cx-(ibox/2)
        yig = cy-(ibox/2)
        insSquare=pygame.Rect(xig,yig,ibox,ibox)

    #rect(surface, color, object)
    pygame.draw.rect(screen, colors.get("blue"), square)
    pygame.draw.rect(screen, colors.get("blue"), insSquare)
    screen.blit(char, (charx, chary))

    #circle(surface, color, center, radius)
    pygame.draw.circle(screen, colors.get("red"), (cx, cy), rad)
    
    pygame.display.update()
    pygame.time.delay(5)

count = 0
high = 0

while run and game == 1:
    # screen.fill(background)
    background = "white"
    screen.fill(background)

    #square movement
    if keys[pygame.K_d] and square.x < WIDTH-wb:
        square.x += speed
    if keys[pygame.K_a] and square.x > 0:
        square.x -= speed
    if keys[pygame.K_s] and square.y < HEIGHT-hb:
        square.y += speed
    if keys[pygame.K_w] and square.y > 0:
        square.y -= speed

    #circle and inscribed square movement
    if keys[pygame.K_RIGHT] and cx < WIDTH-rad:
        cx += speed
        insSquare.x += speed
    if keys[pygame.K_LEFT] and cx > 0+rad:
        cx -= speed
        insSquare.x -= speed
    if keys[pygame.K_DOWN] and cy < HEIGHT-rad:
        cy += speed
        insSquare.y += speed
    if keys[pygame.K_UP] and cy > 0+rad:
        cy -= speed
        insSquare.y -= speed

    #circle square collide
    if square.colliderect(insSquare): 
        print("BOOM")
        cx = random.randint(rad, WIDTH-rad)
        cy = random.randint(rad, HEIGHT-rad)
        rad += 5
        ibox = rad*math.sqrt(2)
        xig = cx-(ibox/2)
        yig = cy-(ibox/2)
        insSquare=pygame.Rect(xig,yig,ibox,ibox)
        count+=1
        score = 800-40*count
        if score > high:   
            high=score
        print("Your score is "+str(score))
        input("Press enter: ")
        os.system('cls')
        print(high)

    #rect(surface, color, object)
    pygame.draw.rect(screen, colors.get("blue"), square)
    pygame.draw.rect(screen, colors.get("blue"), insSquare)

    #circle(surface, color, center, radius)
    pygame.draw.circle(screen, colors.get("red"), (cx, cy), rad)
    pygame.display.update()
    pygame.time.delay(5)

    Button_Menu = pygame.Rect(50, 100, 100, 50)
    pygame.draw.rect(screen, colors.get("colorTheme"), Button_Menu)
    text10 = MENU_FONT.render("Back", 1, colors.get("black"))
    screen.blit(text10, (75, 110))
    while True:
        if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    mx = mousePos[0]
                    my = mousePos[1]
                    if Button_Menu.collidepoint(mx, my):
                        score = 800-40*count
                    if score > high:   
                        high=score
                    print("Your score is "+str(score))
                    menu()
                            


def exit():
    run = False
    print("you quit")
    if high > 50:
            myFile = open("Game 2\G2score.txt", 'a')
            date=datetime.datetime.now()
            scrLine = str(high) + "\t"+ date.strftime("%m-%d-%Y")+ "\n"
            myFile.write(scrLine)
            myFile.close()
        
