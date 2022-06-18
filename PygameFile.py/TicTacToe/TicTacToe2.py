# Sydney Chien
# TICTACTOE


import os, random, time, pygame, math, datetime,sys
os.system('cls')

pygame.init()

TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)
GIANT_FONT = pygame.font.SysFont('comicsans', 100)
WIDTH=700 #like constant
HEIGHT=700
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51),
"RED" : (255, 0, 0),
"GREEN" : (0, 255, 0),
"BLUE" : (0, 0,255),
# SHADES,
"BLACK" : (0, 0, 0),}

clr=colors.get("limeGreen")
messageMenu=['Instructions', 'Settings', 'Game 1', 'Game 2', 'Scoreboard', 'Exit']
messageSettings=["Background Colors", "Screen Size", "Sound On/Off"]
mainTitle="Circle eats Square Menu"
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("Tic Tac Toe")  #change the title of my window
backgrnd=colors.get("pink")

#game Variable
player=1 # CONTROL player 1 is X and -1 is O
markers=[] # Array to control the plays
lineWidth=10 # Line thinkness
Game=True # Control Main Game
MxMy=(0,0) # Checks Click
gameOver=False # Check if game is over
winner = 0 # Who WON the game 1, -1, 0 (TIE)

print(markers)  
cirClr=colors.get("blue") # Color for the Circle
xClr=colors.get("BLACK") # Color for the X
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
    pygame.display.update() \

def Xwinnerult():
    screen.fill("YELLOW")
    Title = GIANT_FONT.render(("X IS THE CHAMPION"), 1, colors.get("white"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 300))\
    
    pygame.display.update()
    pygame.time.delay(500)

    pygame.quit()
    sys.exit()
    print("you quit")
    # UPDATE FILE


def Owinnerult():
    screen.fill("YELLOW")
    Title = GIANT_FONT.render(("O IS THE CHAMPION"), 1, colors.get("white"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 300))\
    
    pygame.display.update()
    pygame.time.delay(500)

    pygame.quit()
    sys.exit()
    print("you quit")
    # UPDATE FILE
                    

def tieult():
    screen.fill("YELLOW")
    Title = TITLE_FONT.render(("IT'S A TIE"), 1, colors.get("white"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 300))\
    
    pygame.time.delay(500)
    pygame.display.update()

    pygame.quit()
    sys.quit()
    print("you quit")

Xcount=0
Ocount=0

def checkWinner():
    global Xcount, Ocount, gameOver, winner
    X_POS = 0
    A_POS = 1
    B_POS = 2
    for row in markers: # CHECK COLUMNS
        if sum(row) == 3:
            winner = 1
            gameOver = True
            
    for row in markers: # CHECK COLUMNS
        if sum(row) == -3:
            winner = -1
            gameOver = True
            
    if markers [0][X_POS] + markers [1][X_POS] + markers [2][X_POS] == 3:# Check ROWS 
        winner = 1
        gameOver = True
        
    if markers [0][X_POS] + markers [1][X_POS] + markers [2][X_POS] == -3:  
        winner = -1
        gameOver = True
    
    if markers [0][A_POS] + markers [1][A_POS] + markers [2][A_POS] == 3:# Check ROWS 
        winner = 1
        gameOver = True
        
    if markers [0][A_POS] + markers [1][A_POS] + markers [2][A_POS] == -3:  
        winner = -1
        gameOver = True
    
    if markers [0][B_POS] + markers [1][B_POS] + markers [2][B_POS] == 3:# Check ROWS 
        winner = 1
        gameOver = True
        
    if markers [0][B_POS] + markers [1][B_POS] + markers [2][B_POS] == -3:  
        winner = -1
        gameOver = True
        
   # CHECK DIAGONALS
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
        text = GIANT_FONT.render("X WINS", 1, "white")
       
       

    if winner == -1:
        Ocount+=1
        text = GIANT_FONT.render("O WINS", 1, "white")
      
        
    
    if winner == 0:
        text = GIANT_FONT.render("XO TIE", 1, "white")
        
    screen.fill("red")
    screen.blit(text, (WIDTH//4, 50))\

 
    PlayAgain = MENU_FONT.render("Play Again?:", 1, colors.get("white"))
    screen.blit(PlayAgain, (WIDTH//8, 300))
    

    XScoretext = MENU_FONT.render(("X's Wins:"+ str(Xcount)), 1, colors.get("white"))
    screen.blit(XScoretext, (WIDTH//3, 200))
   

    OScoretext = MENU_FONT.render(("O's Wins:"+ str(Ocount)), 1, colors.get("white"))
    screen.blit(OScoretext, (WIDTH//3*2, 200))
   

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
                    if Xcount > Ocount:
                        Xwinnerult()
                    if Ocount > Xcount:
                        Owinnerult()
                    if Ocount == Xcount:
                        tieult()
                    pygame.quit()
                    sys.quit()
                    print("you quit")
                    # Add X/O score date

zero_Array()
print()

while Game:
    screen.fill(backgrnd)
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


