# Sydney Chien
# 06/20/2022
# "RPS" STANDS FOR ROCK PAPER SCISSORS
import pygame, os, time, random, math, datetime, sys
from pygame import mixer
pygame.init()

# Import Fonts
TITLE_FONT = pygame.font.SysFont('comicsans', 40) # Titles for functions
MENU_FONT = pygame.font.SysFont('comicsans', 20) # For buttons, subheaders, messages
GIANT_FONT = pygame.font.SysFont('comicsans', 100) # For stressed announcements ("YOU WIN", "YOU LOSE")
BOLD_FONT = pygame.font.SysFont('arial.bold', 40) # For Player and COM names 

os.system('cls')

# General Variables
WIDTH = 700   # Amount of pixels
w3 = WIDTH//3 # Shortcut for centering items
HEIGHT = 700

# Color Dictionary
colors = {"violet": (144, 13, 255), "yellow":(250, 225, 0), "pink": (255, 1, 129), "turquoise": (50, 219, 240), "white":(255,255,255), "grey":(245,245,245), "black":(0,0,0), "red":(255,0,0), "green":(0,255,0), "blue":(0,0,255), "orange":(255,128,0), "purple":(127,0,255), "cyan": (0,255,255)}
Wclr = colors.get("white")

#Create a Display
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE) # .RESIZABLE make window resizable
pygame.display.set_caption("Rock Paper Scissor") # title of the window

#Images
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
xb = WIDTH//7
yb = WIDTH//2

# Screen Positioning Var
mx = 0
my = 0

#Game Variables
speed = 2
run = True
high = 0
colorTheme = Wclr # Set to colorTheme to change var in settings
mixer.music.load('PygameFile.py\journey.wav') # Play music
mixer.music.play(-1)

# Settings
def settings():
    global screen, colorTheme, mx, my, WIDTH, HEIGHT
    screen.fill(colorTheme)
    Title = TITLE_FONT.render("Settings", 1, colors.get("violet")) # Designate title font and content
    xd = WIDTH//2 - (Title.get_width()//2) # Make  x coordinate half of screen, minus half of title for centering
    screen.blit(Title, (xd, 10)) # Display

    # Color Settings
    ColorTheme = MENU_FONT.render("Background Color:", 1, colors.get("violet")) # Same as title
    screen.blit(ColorTheme, (w3, 70)) # w3 = WIDTH//3
    pygame.display.update()
    pygame.time.delay(50)

    # Color Backgrounds
    Button_White = pygame.Rect(w3, 100, 230, 50) # Make button shape
    Button_Black = pygame.Rect(w3, 170, 230, 50)
    Button_Turquoise = pygame.Rect(w3, 240, 230, 50)
    pygame.draw.rect(screen, colors.get("grey"), Button_White) # Color button
    pygame.draw.rect(screen, colors.get("black"), Button_Black)
    pygame.draw.rect(screen, colors.get("turquoise"), Button_Turquoise)

    # Name Color Backgrounds
    textWhite = MENU_FONT.render("White", 1, colors.get("black")) # Make and color text
    textTurquoise = MENU_FONT.render("Black", 1, Wclr)
    textPurple = MENU_FONT.render("Turquoise", 1, colors.get("black"))
    screen.blit(textWhite, (w3, 110)) # Blit text
    screen.blit(textTurquoise, (w3, 180))
    screen.blit(textPurple, (w3, 250))
    pygame.display.update() # Update display
    pygame.time.delay(50)

    # Back button
    Button_Back = pygame.Rect(20, 20, 100, 50)
    pygame.draw.rect(screen, colors.get("red"), Button_Back)
    textBack = MENU_FONT.render("Back", 1, colors.get("black"))
    screen.blit(textBack, (25, 25))
    pygame.display.update()
    pygame.time.delay(50)

    # Screen Size Settings
    ScreenSize = MENU_FONT.render("Screen Size:", 1, colors.get("violet"))
    screen.blit(ScreenSize, (w3, 300))
    pygame.display.update()
    pygame.time.delay(50)

    # Create Shape and Color Buttons
    Button_Size1 = pygame.Rect(w3, 350, 230, 50)
    Button_Size2 = pygame.Rect(w3, 420, 230, 50)
    pygame.draw.rect(screen, colors.get("violet"), Button_Size1)
    pygame.draw.rect(screen, colors.get("violet"), Button_Size2)

    # Create and Position Text
    textSize1 = MENU_FONT.render("+100", 1, colors.get("black"))
    textSize2= MENU_FONT.render("-100", 1, colors.get("black"))
    screen.blit(textSize1, (w3, 360))
    screen.blit(textSize2, (w3, 430))
    pygame.display.update()
    pygame.time.delay(50)

 # Sound Settings
    Sound = MENU_FONT.render("Sound?:", 1, colors.get("violet"))
    screen.blit(Sound, (WIDTH//8, 600))
    pygame.display.update()
    pygame.time.delay(50)

    # Create Buttons
    Button_SoundY = pygame.Rect(WIDTH * .3, 550, 120, 120)
    Button_SoundN = pygame.Rect(WIDTH * .6, 550, 120, 120)
    pygame.draw.rect(screen, colors.get("violet"), Button_SoundY)
    pygame.draw.rect(screen, colors.get("violet"), Button_SoundN)
  
    # Create Text
    textSoundY = MENU_FONT.render("On", 1, colors.get("black"))
    textSoundN= MENU_FONT.render("Off", 1, colors.get("black"))
    screen.blit(textSoundY, (WIDTH * .35, 570))
    screen.blit(textSoundN, (WIDTH * .65, 570))
    pygame.display.update()
    pygame.time.delay(50)

    # Make Color Backgrounds Change Color Var, Change WIDTH and HEIGHT Var, Play Sound
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_White.collidepoint(mx, my):
                    colorTheme = "white" 
                if Button_Turquoise.collidepoint(mx, my):
                    colorTheme = "turquoise"
                if Button_Black.collidepoint(mx, my):
                    colorTheme = "black"
                if Button_Back.collidepoint(mx, my):
                    menu()
                if Button_Size1.collidepoint(mx, my):
                    WIDTH += 100
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
                if Button_Size2.collidepoint(mx, my):
                    WIDTH -= 100
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
    screen.fill(colorTheme)
    pygame.display.update()
    pygame.time.delay(500)

    # Create title
    # Create Box, Relative to WIDTH and HEIGHT

    # Create Rectangle
    input_rect = pygame.Rect(WIDTH//4, HEIGHT//3, 350, 50)
    pygame.draw.rect(screen, colors.get("red"), input_rect)

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
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN: # Return -> userName set, move to menu
                    if event.key == pygame.K_RETURN:
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
    Title = TITLE_FONT.render("Menu", 1, colors.get("pink")) # Create a title
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
    Title = TITLE_FONT.render("Instructions", 1, colors.get("green"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))\

    #Instructions File
    myFile = open("PygameFile.py\FinalGame\FGinstructions.txt", "r")
    content = myFile.readlines()

    #print instructions
    yi = 120   # yi automatically adds space between each printed line
    for line in content:
        Insctruc = MENU_FONT.render(line[0:-1], 1, colors.get('green'))
        screen.blit(Insctruc, (40, yi))
        pygame.display.update()
        pygame.time.delay(50)
        yi += 40
    
    #creating buttons
    Button_1 = pygame.Rect(200, 550, 100, 50)
    Button_2 = pygame.Rect(400, 550, 100, 50)
    pygame.draw.rect(screen, colors.get("green"), Button_1)
    pygame.draw.rect(screen, colors.get("green"), Button_2)

    #render yes and no
    text1 = MENU_FONT.render("Yes", 1, colors.get("black"))
    text2 = MENU_FONT.render("No", 1, colors.get("black"))
    screen.blit(text1, (225, 560))
    screen.blit(text2, (425, 560))
    pygame.display.update()

    # Back button
    Button_Back = pygame.Rect(20, 20, 100, 50)
    pygame.draw.rect(screen, colors.get("red"), Button_Back)
    textBack = MENU_FONT.render("Back", 1, colors.get("black"))
    screen.blit(textBack, (25, 25))
    pygame.display.update()
    pygame.time.delay(50)

    # Buttons lead to Level 1 or menu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_1.collidepoint(mx, my):
                    game1()
                if Button_2.collidepoint(mx, my):
                    menu()
                if Button_Back.collidepoint(mx, my):
                    menu()


player = 'r' # Define player as rock

clock = pygame.time.Clock() # Create a clock

# Define Game Var
x = 50
y = 600
width = 64
height = 64
score = 0
current_time = 0
button_press_time = 0

# RPS Level 1
def game1():
    def checkwinner(): # Check for win, lose, tie
        global player, computer
        # Winning situations
        if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
            maze()
        # Tie game situations
        if (player == 'r' and computer == 'r') or (player == 'p' and computer == 'p') or (player == 's' and computer == 's'):
            tie()
        # Losing situations
        if (computer == 'r' and player == 's') or (computer == 's' and player == 'p') or (computer == 'p' and player == 'r'):
            lose()

    def RPS():
        global computer, player, WIDTH, HEIGHT

        # Blit starting objects in position
        screen.blit(bg, (0,0)) 
        screen.blit(Prock, (xb, yb))
        screen.blit(COMrock, ((700-150)- xb, yb))

        # Name the players
        Player = BOLD_FONT.render("PLAYER", 1, colors.get("blue")) # Designate title font and content
        screen.blit(Player, (xb+30, 300)) # Display
        COM = BOLD_FONT.render("COM", 1, colors.get("red")) # Designate title font and content
        screen.blit(COM, (WIDTH-(xb+100), 300)) # Display

        # Back button
        Button_Back = pygame.Rect(20, 20, 100, 50)
        pygame.draw.rect(screen, colors.get("red"), Button_Back)
        textBack = MENU_FONT.render("Back", 1, colors.get("black"))
        screen.blit(textBack, (25, 25))
        pygame.display.update()
        pygame.time.delay(50)


        computer = random.choice(['r','p','s']) # Random choice

        # Button for rock, paper, scissors
        Button_R = pygame.Rect(WIDTH//12, 550, 120, 50)
        Button_P = pygame.Rect(WIDTH//12*5, 550, 120, 50)
        Button_S = pygame.Rect(WIDTH//12*9, 550, 120, 50)
        pygame.draw.rect(screen, colors.get("pink"), Button_R)
        pygame.draw.rect(screen, colors.get("pink"), Button_P)
        pygame.draw.rect(screen, colors.get("pink"), Button_S)

        # Text for rock, paper, scissors
        textR = MENU_FONT.render("Rock", 1, colors.get("black"))
        textP = MENU_FONT.render("Paper", 1, colors.get("black"))
        textS = MENU_FONT.render("Scissors", 1, colors.get("black"))
        screen.blit(textR, (WIDTH//12+30, 560))
        screen.blit(textP, (WIDTH//12*5+30, 560))
        screen.blit(textS, (WIDTH//12*9+30, 560))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Quit - immediately exit the window
                    menu()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    mx = mousePos[0]
                    my = mousePos[1]
                    if Button_Back.collidepoint(mx, my): # Back - quit function gives score asks to leave or stay
                        quit()
                    if Button_R.collidepoint(mx, my): # Print and Display Player
                        player = 'r'
                        screen.blit(Prock, (xb, yb))
                        pygame.display.update()
                        print(player)
                        if computer == 'r': # Print and Display COM
                            screen.blit(COMrock, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        if computer == 'p':# Print and Display COM
                            screen.blit(COMpaper, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        if computer == 's':# Print and Display COM
                            screen.blit(COMscissor, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        checkwinner()
                    if Button_P.collidepoint(mx, my): # Same as rock
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
                        
                    if Button_S.collidepoint(mx, my):# Same as rock
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
                                                          
   
    def maze(): # Maze after RPS wins
        global screen, score, button_press_time
        pygame.time.delay(200)

        # Create Winner Display
        screen.fill("yellow")
        Win = GIANT_FONT.render(("YOU WON!"), 1, Wclr)
        xd = WIDTH//2 - (Win.get_width()//2)
        screen.blit(Win, (xd, 200))\
        
        pygame.display.update() 
        pygame.time.delay(1000)


        # Class for Orange 
        class Player(object):
            
            def __init__(self):
                self.rect = pygame.Rect(190, 95, 16, 16)
        
            def move(self, dx, dy):
                
                # Move each axis separately. Note that this checks for collisions both times.
                if dx != 0:
                    self.move_single_axis(dx, 0)
                if dy != 0:
                    self.move_single_axis(0, dy)
            
            def move_single_axis(self, dx, dy):
                
                # Move Rect
                self.rect.x += dx
                self.rect.y += dy
        
                # If you collide with a wall, move out based on velocity
                for wall in walls:
                    if self.rect.colliderect(wall.rect):
                        if dx > 0: # Moving right; Hit the left side of the wall
                            self.rect.right = wall.rect.left
                        if dx < 0: # Moving left; Hit the right side of the wall
                            self.rect.left = wall.rect.right
                        if dy > 0: # Moving down; Hit the top side of the wall
                            self.rect.bottom = wall.rect.top
                        if dy < 0: # Moving up; Hit the bottom side of the wall
                            self.rect.top = wall.rect.bottom
        
        # Class to Hold a Wall Rect
        class Wall(object):
            
            def __init__(self, pos):
                walls.append(self)
                self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
        
        # Initialise Pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        
    

        clock = pygame.time.Clock()
        walls = [] # List to hold the walls
        player = Player() # Create the player
        
        # Holds the level layout in a list of strings
        level = [
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "      WWWWWWWWWWWWW    WWWWWWWWWWWWWWW",
            "      W           W                  W",
            "      W  WWWW  W  W     WWWW  W WWW  W",
            "      W     W  W        W     W   W  W",
            "      WWWW  WWWWWWWWWWWWWWW     WWW  W",
            "      W       W   W     W        W   W",
            "      W  WWWWWW   WWWW  WWWWWW   W   W",
            "      W       W      W  W    W   W   W",
            "      W  W  WWWWWWW  W  W  WWW   WWWWW",
            "      W  W        W  W       W       W",
            "      W  WWWWWWW  W  WWWWWW  WWW     W",
            "      W  W        W  W       W W     W",
            "      W  WWWWWWWWWW  W  WWWW W W     W",
            "      W        W     W  W  W   W     W",
            "      WWWWWWW  W  WWWW  W  WWW W     W",
            "      W           W     W    W W     W",
            "      W  W  WWWWWWW  WWWW  W W W     W",
            "      W  W     W  W  W   W W   W     W",
            "      WWWW  W  W  W  WW    W WWW     W",
            "      W     W    W    W  WW          W",
            "      WWWWWWWWWWWWWWW       WWWWWWWWWW",
            "      W W      WW        W      W    W",
            "      W W   WWWW   WWW   W   WWW     W",
            "      W     W    E   W   W  WW       W",
            "      WWWWWWWWWWWWWWWWWWWW           W",
            "      WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
        

        ]
        
        # W = wall, E = exit
        x = y = 0
        for row in level:
            for col in row:
                if col == "W":
                    Wall((x, y))
                if col == "E":
                    end_rect = pygame.Rect(x, y, 16, 16)
                x += 16
            y += 16
            x = 0
        
        pygame.display.update() 
        pygame.time.delay(1000)

        maze = True
        while maze:
            clock.tick(60) # 60 frames per second
            pygame.time.get_ticks() # Get time
           
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Quit -> immediately closes window
                    menu()
        
            # Move the player if an arrow key is pressed
            key = pygame.key.get_pressed() # Provide a list of 11 keys
            if key[pygame.K_LEFT]:
                player.move(-2, 0)
            if key[pygame.K_RIGHT]:
                player.move(2, 0)
            if key[pygame.K_UP]:
                player.move(0, -2)
            if key[pygame.K_DOWN]:
                player.move(0, 2)
                
        
            # If hits red, game end
            if player.rect.colliderect(end_rect):
                score += 1 # Add a point
                quit() # Show score, ask if keep playing or leave
        
            # Color background, players, wall
            screen.fill("black")
            for wall in walls:
                pygame.draw.rect(screen, (Wclr), wall.rect) # Walls are white
            pygame.draw.rect(screen, ("red"), end_rect) # End Rect is red
            pygame.draw.rect(screen, ("yellow"), player.rect) # Player is yellow
        
            pygame.display.flip() 
            clock.tick(360)

       
    def quit():
        global score
        pygame.time.delay(500)

        # Display Score
        screen.fill("red")
        Tie = GIANT_FONT.render(("SCORE: "+ str(score)), 1, Wclr) 
        xd = WIDTH//2 - (Tie.get_width()//2)
        screen.blit(Tie, (xd, 200))\
        
        #creating buttons
        Button_1 = pygame.Rect(150, 550, 150, 50)
        Button_2 = pygame.Rect(400, 550, 150, 50)
        pygame.draw.rect(screen, colors.get("white"), Button_1)
        pygame.draw.rect(screen, colors.get("white"), Button_2)

        # Render yes and no
        text1 = MENU_FONT.render("Keep Playing", 1, colors.get("black"))
        text2 = MENU_FONT.render("Leave Game", 1, colors.get("black"))
        screen.blit(text1, (175, 560))
        screen.blit(text2, (425, 560))
        pygame.display.update()

        # Buttons Lead to RPS or Menu
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    mx = mousePos[0]
                    my = mousePos[1]
                    if Button_1.collidepoint(mx, my):
                        RPS()
                    if Button_2.collidepoint(mx, my):
                        # Save Score in file 
                        myFile = open("PygameFile.py\FinalGame\FGScoreL1.txt", 'a') # Open file
                        date=datetime.datetime.now() # Get date
                        scrLine = str(score)+"        "+ userName + "       "+ date.strftime("%m-%d-%Y")+ "       "+ "Level 1" + "\n"
                        myFile.write(scrLine)     # Print the score
                        myFile.close() 
                        print(scrLine)
                        score = 0 # Set score back to 0
                        menu() # Go back to menu
        

    
    def tie():
        # Create "TIE" screen
        pygame.time.delay(500)
        screen.fill("violet")
        Tie = GIANT_FONT.render(("TIE!"), 1, Wclr)
        xd = WIDTH//2 - (Tie.get_width()//2)
        screen.blit(Tie, (xd, 200))\
        
        pygame.display.update() 
        pygame.time.delay(1000)

        RPS() # Go back to RPS

    def lose():
        # Create "LOSE" screen 
        pygame.time.delay(500)
        screen.fill("turquoise")
        Lose = GIANT_FONT.render(("YOU LOST!"), 1, Wclr)
        xd = WIDTH//2 - (Lose.get_width()//2)
        screen.blit(Lose, (xd, 200))\
        
        pygame.display.update() 
        pygame.time.delay(1000)

        RPS() # Go back to RPS


    Game = True
    while Game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT: # Quit -> Immediately close window
                pygame.quit()
                sys.exit()
                
        pygame.display.update() 
        pygame.time.delay(100)

        RPS() # Go back to RPS

# RPS Level 2
def game2():
    def checkwinner(): # Check for win, lose, tie
        global player, computer
        # Winning situations
        if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
            maze()
        # Tie game situations
        if (player == 'r' and computer == 'r') or (player == 'p' and computer == 'p') or (player == 's' and computer == 's'):
            tie()
        # Losing situations
        if (computer == 'r' and player == 's') or (computer == 's' and player == 'p') or (computer == 'p' and player == 'r'):
            lose()

    def RPS():
        global computer, player

        # Blit starting objects in position
        screen.blit(bg, (0,0)) 
        screen.blit(Prock, (xb, yb))
        screen.blit(COMrock, ((700-150)- xb, yb))

        # Name the players
        Player = BOLD_FONT.render("PLAYER", 1, colors.get("blue")) # Designate title font and content
        screen.blit(Player, (xb+30, 300)) # Display
        COM = BOLD_FONT.render("COM", 1, colors.get("red")) # Designate title font and content
        screen.blit(COM, (WIDTH-(xb+100), 300)) # Display

        # Back button
        Button_Back = pygame.Rect(20, 20, 100, 50)
        pygame.draw.rect(screen, colors.get("red"), Button_Back)
        textBack = MENU_FONT.render("Back", 1, colors.get("black"))
        screen.blit(textBack, (25, 25))
        pygame.display.update()
        pygame.time.delay(50)


        computer = random.choice(['r','p','s']) # Random choice

        # Button for rock, paper, scissors
        Button_R = pygame.Rect(WIDTH//12, 550, 120, 50)
        Button_P = pygame.Rect(WIDTH//12*5, 550, 120, 50)
        Button_S = pygame.Rect(WIDTH//12*9, 550, 120, 50)
        pygame.draw.rect(screen, colors.get("pink"), Button_R)
        pygame.draw.rect(screen, colors.get("pink"), Button_P)
        pygame.draw.rect(screen, colors.get("pink"), Button_S)

        # Text for rock, paper, scissors
        textR = MENU_FONT.render("Rock", 1, colors.get("black"))
        textP = MENU_FONT.render("Paper", 1, colors.get("black"))
        textS = MENU_FONT.render("Scissors", 1, colors.get("black"))
        screen.blit(textR, (WIDTH//12+30, 560))
        screen.blit(textP, (WIDTH//12*5+30, 560))
        screen.blit(textS, (WIDTH//12*9+30, 560))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Quit - immediately exit the window
                    menu() 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    mx = mousePos[0]
                    my = mousePos[1]
                    if Button_Back.collidepoint(mx, my): # Back - quit function gives score asks to leave or stay
                        quit()
                    if Button_R.collidepoint(mx, my): # Print and Display Player
                        player = 'r'
                        screen.blit(Prock, (xb, yb))
                        pygame.display.update()
                        print(player)
                        if computer == 'r': # Print and Display COM
                            screen.blit(COMrock, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        if computer == 'p':# Print and Display COM
                            screen.blit(COMpaper, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        if computer == 's':# Print and Display COM
                            screen.blit(COMscissor, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        checkwinner()
                    if Button_P.collidepoint(mx, my): # Same as rock
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
                        
                    if Button_S.collidepoint(mx, my):# Same as rock
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
                                  

    def maze(): # Maze after RPS wins
        global screen, score

        # Create Winner Display
        pygame.time.delay(200)
        screen.fill("yellow")
        Win = GIANT_FONT.render(("YOU WON!"), 1, Wclr)
        xd = WIDTH//2 - (Win.get_width()//2)
        screen.blit(Win, (xd, 200))\
        
        pygame.display.update() 
        pygame.time.delay(1000)


        # Class for Orange 
        class Player(object):
            
            def __init__(self):
                self.rect = pygame.Rect(190, 95, 16, 16)
        
            def move(self, dx, dy):
                
                # Move each axis separately. Note that this checks for collisions both times.
                if dx != 0:
                    self.move_single_axis(dx, 0)
                if dy != 0:
                    self.move_single_axis(0, dy)
            
            def move_single_axis(self, dx, dy):
                
                # Move the rect
                self.rect.x += dx
                self.rect.y += dy
        
                # If you collide with a wall, move out based on velocity
                for wall in walls:
                    if self.rect.colliderect(wall.rect):
                        if dx > 0: # Moving right; Hit the left side of the wall
                            self.rect.right = wall.rect.left
                        if dx < 0: # Moving left; Hit the right side of the wall
                            self.rect.left = wall.rect.right
                        if dy > 0: # Moving down; Hit the top side of the wall
                            self.rect.bottom = wall.rect.top
                        if dy < 0: # Moving up; Hit the bottom side of the wall
                            self.rect.top = wall.rect.bottom
        
        # Class to Hold a Wall Rect
        class Wall(object):
            
            def __init__(self, pos):
                walls.append(self)
                self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
        
        # Initialise Pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()

        clock = pygame.time.Clock()
        walls = [] # List to hold the walls
        player = Player() # Create the player
        
        # Holds the level layout in a list of strings.
        level = [
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "      WWWWWWWWWWWWW    WWWWWWWWWWWWWWW",
            "      W           W                  W",
            "      W  WWWW  W  W     WWWW  W WWW  W",
            "      W     W  W        W     W   W  W",
            "      WWWW  WWWWWWWWWWWWWWW     WWW  W",
            "      W       W   W     W        W   W",
            "      W  WWWWWW   WWWW  WWWWWW   W   W",
            "      W       W      W  W    W   W   W",
            "      W  W  WWWWWWW  W  W  WWW   WWWWW",
            "      W  W        W  W       W       W",
            "      W  WWWWWWW  W  WWWWWW  WWW     W",
            "      W  W        W  W       W W     W",
            "      W  WWWWWWWWWW  W  WWWW W W     W",
            "      W        W     W  W  W   W     W",
            "      WWWWWWW  W  WWWW  W  WWW W     W",
            "      W           W     W    W W     W",
            "      W  W  WWWWWWW  WWWW  W W W     W",
            "      W  W     W  W  W   W W   W     W",
            "      WWWW  W  W  W  WW    W WWW     W",
            "      W     W    W    W  WW          W",
            "      WWWWWWWWWWWWWWW       WWWWWWWWWW",
            "      W W      WW        W      W    W",
            "      W W   WWWW   WWW   W   WWW     W",
            "      W     W    E   W   W  WW       W",
            "      WWWWWWWWWWWWWWWWWWWW           W",
            "      WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
        

        ]
        
        # W = wall, E = exit
        x = y = 0
        for row in level:
            for col in row:
                if col == "W":
                    Wall((x, y))
                if col == "E":
                    end_rect = pygame.Rect(x, y, 16, 16)
                x += 16
            y += 16
            x = 0
            
        old_time = pygame.time.get_ticks()

        running = True
        while running:
            clock.tick(60) # 60 frames per second
            pygame.time.get_ticks() # Get time
        
            
            current_time = pygame.time.get_ticks()
            if current_time - old_time > 60000: # 60 seconds to finish
                quit() # Give score, ask to play again or leave
                                                                                       # Subtract from 60 for countDOWN
            countdown = (f"COUNTDOWN: {60 - (current_time - old_time)//1000} seconds") # Convert milliseconds to seconds 
            print(countdown)
            pygame.display.flip()
            clock.tick(60)
            

            for event in pygame.event.get(): # Quit -> Immediately close window
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
               
                            
            # Move the player if an arrow key is pressed
            key = pygame.key.get_pressed() # Provide a list of 11 keys
            if key[pygame.K_LEFT]:
                player.move(-2, 0)
            if key[pygame.K_RIGHT]:
                player.move(2, 0)
            if key[pygame.K_UP]:
                player.move(0, -2)
            if key[pygame.K_DOWN]:
                player.move(0, 2)
                
        
            # Red Rect gets hit -> Game end 
            if player.rect.colliderect(end_rect):
                score += 1 # Earn a point
                quit() # Keep Playing/Leave game function
        
            CDcolor = "white"
            if current_time - old_time > 50000:
                CDcolor = "red"

            # Color background, players, wall, Countdown
            screen.fill("black")
            CD = TITLE_FONT.render((countdown), 1, colors.get(CDcolor))
            xd = WIDTH//2 - (CD.get_width()//2)
            screen.blit(CD, (xd, 30))\

            for wall in walls:
                pygame.draw.rect(screen, (255, 255, 255), wall.rect)
            pygame.draw.rect(screen, (255, 0, 0), end_rect)
            pygame.draw.rect(screen, (255, 200, 0), player.rect)
            pygame.display.flip()
            clock.tick(360)

       
    def quit():
        # Display Score
        pygame.time.delay(500)
        screen.fill("red")
        Tie = GIANT_FONT.render(("SCORE: "+ str(score)), 1, Wclr)
        xd = WIDTH//2 - (Tie.get_width()//2)
        screen.blit(Tie, (xd, 200))\

        #creating buttons
        Button_1 = pygame.Rect(150, 550, 150, 50)
        Button_2 = pygame.Rect(400, 550, 150, 50)
        pygame.draw.rect(screen, colors.get("white"), Button_1)
        pygame.draw.rect(screen, colors.get("white"), Button_2)

        # Render yes and no
        text1 = MENU_FONT.render("Keep Playing", 1, colors.get("black"))
        text2 = MENU_FONT.render("Leave Game", 1, colors.get("black"))
        screen.blit(text1, (175, 560))
        screen.blit(text2, (425, 560))
        pygame.display.update()

        # Buttons lead to Level 1 or menu
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    mx = mousePos[0]
                    my = mousePos[1]
                    if Button_1.collidepoint(mx, my):
                        RPS()
                    if Button_2.collidepoint(mx, my):
                        # Save score stuff
                        myFile = open("PygameFile.py\FinalGame\FGScoreL1.txt", 'a')
                        date=datetime.datetime.now()
                        scrLine = str(score)+"        "+ userName + "       "+ date.strftime("%m-%d-%Y")+"       "+ "Level 2" +"\n"
                        myFile.write(scrLine)     # Print the high score
                        myFile.close() 
                        print(scrLine)
                        menu()
        

    
    def tie():
        # Create "TIE" screen
        pygame.time.delay(500)
        screen.fill("violet")
        Tie = GIANT_FONT.render(("TIE!"), 1, Wclr)
        xd = WIDTH//2 - (Tie.get_width()//2)
        screen.blit(Tie, (xd, 200))\
        
        pygame.display.update() 
        pygame.time.delay(1000)

        RPS()

    def lose():
        # Create "LOSE" screen
        pygame.time.delay(500)
        screen.fill("turquoise")
        Lose = GIANT_FONT.render(("YOU LOST!"), 1, Wclr)
        xd = WIDTH//2 - (Lose.get_width()//2)
        screen.blit(Lose, (xd, 200))\
        
        pygame.display.update() 
        pygame.time.delay(1000)

        RPS()


    Game = True
    while Game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()
                
        pygame.display.update() 
        pygame.time.delay(100)

        RPS() # Go back to RPS


# RPS Level 3
def game3():
    def checkwinner(): # Check for win, lose, tie
        global player, computer
        # Winning situations
        if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
            maze()
        # Tie game situations
        if (player == 'r' and computer == 'r') or (player == 'p' and computer == 'p') or (player == 's' and computer == 's'):
            tie()
        # Losing situations
        if (computer == 'r' and player == 's') or (computer == 's' and player == 'p') or (computer == 'p' and player == 'r'):
            lose()

    def RPS():
        global computer, player

        # Blit starting objects in position
        screen.blit(bg, (0,0)) 
        screen.blit(Prock, (xb, yb))
        screen.blit(COMrock, ((700-150)- xb, yb))

        # Name the players
        Player = BOLD_FONT.render("PLAYER", 1, colors.get("blue")) # Designate title font and content
        screen.blit(Player, (xb+30, 300)) # Display
        COM = BOLD_FONT.render("COM", 1, colors.get("red")) # Designate title font and content
        screen.blit(COM, (WIDTH-(xb+100), 300)) # Display

        # Back button
        Button_Back = pygame.Rect(20, 20, 100, 50)
        pygame.draw.rect(screen, colors.get("red"), Button_Back)
        textBack = MENU_FONT.render("Back", 1, colors.get("black"))
        screen.blit(textBack, (25, 25))
        pygame.display.update()
        pygame.time.delay(50)


        computer = random.choice(['r','p','s']) # Random choice

        # Button for rock, paper, scissors
        Button_R = pygame.Rect(WIDTH//12, 550, 120, 50)
        Button_P = pygame.Rect(WIDTH//12*5, 550, 120, 50)
        Button_S = pygame.Rect(WIDTH//12*9, 550, 120, 50)
        pygame.draw.rect(screen, colors.get("pink"), Button_R)
        pygame.draw.rect(screen, colors.get("pink"), Button_P)
        pygame.draw.rect(screen, colors.get("pink"), Button_S)

        # Text for rock, paper, scissors
        textR = MENU_FONT.render("Rock", 1, colors.get("black"))
        textP = MENU_FONT.render("Paper", 1, colors.get("black"))
        textS = MENU_FONT.render("Scissors", 1, colors.get("black"))
        screen.blit(textR, (WIDTH//12+30, 560))
        screen.blit(textP, (WIDTH//12*5+30, 560))
        screen.blit(textS, (WIDTH//12*9+30, 560))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Quit - immediately exit the window
                    menu()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    mx = mousePos[0]
                    my = mousePos[1]
                    if Button_Back.collidepoint(mx, my): # Back - quit function gives score asks to leave or stay
                        quit()
                    if Button_R.collidepoint(mx, my): # Print and Display Player
                        player = 'r'
                        screen.blit(Prock, (xb, yb))
                        pygame.display.update()
                        print(player)
                        if computer == 'r': # Print and Display COM
                            screen.blit(COMrock, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        if computer == 'p':# Print and Display COM
                            screen.blit(COMpaper, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        if computer == 's':# Print and Display COM
                            screen.blit(COMscissor, ((700-150)- xb, yb))
                            pygame.display.update()
                            print(computer)
                        checkwinner()
                    if Button_P.collidepoint(mx, my): # Same as rock
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
                        
                    if Button_S.collidepoint(mx, my):# Same as rock
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
                                  

    def maze(): # Maze after RPS wins
        global screen, score
        pygame.time.delay(200)

        # Create Winner Display
        screen.fill("yellow")
        Win = GIANT_FONT.render(("YOU WON!"), 1, Wclr)
        xd = WIDTH//2 - (Win.get_width()//2)
        screen.blit(Win, (xd, 200))\
        
        pygame.display.update() 
        pygame.time.delay(1000)


        # Class for Orange 
        class Player(object):
            
            def __init__(self):
                self.rect = pygame.Rect(190, 95, 16, 16)
        
            def move(self, dx, dy):
                
                # Move each axis separately. Note that this checks for collisions both times.
                if dx != 0:
                    self.move_single_axis(dx, 0)
                if dy != 0:
                    self.move_single_axis(0, dy)
            
            def move_single_axis(self, dx, dy):
                
                # Move Rect
                self.rect.x += dx
                self.rect.y += dy
        
                # If you collide with a wall, move out based on velocity
                for wall in walls:
                    if self.rect.colliderect(wall.rect):
                        if dx > 0: # Moving right; Hit the left side of the wall
                            self.rect.right = wall.rect.left
                        if dx < 0: # Moving left; Hit the right side of the wall
                            self.rect.left = wall.rect.right
                        if dy > 0: # Moving down; Hit the top side of the wall
                            self.rect.bottom = wall.rect.top
                        if dy < 0: # Moving up; Hit the bottom side of the wall
                            self.rect.top = wall.rect.bottom
        
        # Class to Hold a Wall Rect
        class Wall(object):
            
            def __init__(self, pos):
                walls.append(self)
                self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
        
        # Initialise Pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        
    

        clock = pygame.time.Clock() # Create a clock for accurate time
        walls = [] # List to hold the walls
        player = Player() # Create the player
        
        # Holds the level layout in a list of strings.
        level = [
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "      WWWWWWWWWWWWW    WWWWWWWWWWWWWWW",
            "      W           W                  W",
            "      W  WWWW  W  W     WWWW  W WWW  W",
            "      W     W  W        W     W   W  W",
            "      WWWW  WWWWWWWWWWWWWWW     WWW  W",
            "      W       W   W     W        W   W",
            "      W  WWWWWW   WWWW  WWWWWW   W   W",
            "      W       W      W  W    W   W   W",
            "      W  W  WWWWWWW  W  W  WWW   WWWWW",
            "      W  W        W  W       W       W",
            "      W  WWWWWWW  W  WWWWWW  WWW     W",
            "      W  W        W  W       W W     W",
            "      W  WWWWWWWWWW  W  WWWW W W     W",
            "      W        W     W  W  W   W     W",
            "      WWWWWWW  W  WWWW  W  WWW W     W",
            "      W           W     W    W W     W",
            "      W  W  WWWWWWW  WWWW  W W W     W",
            "      W  W     W  W  W   W W   W     W",
            "      WWWW  W  W  W  WW    W WWW     W",
            "      W     W    W    W  WW          W",
            "      WWWWWWWWWWWWWWW       WWWWWWWWWW",
            "      W W      WW        W      W    W",
            "      W W   WWWW   WWW   W   WWW     W",
            "      W     W    E   W   W  WW       W",
            "      WWWWWWWWWWWWWWWWWWWW           W",
            "      WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
        

        ]
        
        # W = wall, E = exit
        x = y = 0
        for row in level:
            for col in row:
                if col == "W":
                    Wall((x, y))
                if col == "E":
                    end_rect = pygame.Rect(x, y, 16, 16)
                x += 16
            y += 16
            x = 0
        
        old_time = pygame.time.get_ticks()

        running = True
        while running:
            clock.tick(60) # 60 frames per second
            pygame.time.get_ticks() # Get time
        
            
            current_time = pygame.time.get_ticks()
            if current_time - old_time > 30000: # 30 seconds to finish
                quit() # Give score, ask to play again or leave
                                                                                       # Subtract from 60 for countDOWN
            countdown = (f"COUNTDOWN: {30 - (current_time - old_time)//1000} seconds") # Convert milliseconds to seconds 
            print(countdown)
            pygame.display.flip()
            clock.tick(60)
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Quit -> immediately closes window
                    pygame.quit()
                    sys.exit()

                            
            # Move the player if an arrow key is pressed
            key = pygame.key.get_pressed()  # Provide a list of 11 keys
            if key[pygame.K_LEFT]:
                player.move(-2, 0)
            if key[pygame.K_RIGHT]:
                player.move(2, 0)
            if key[pygame.K_UP]:
                player.move(0, -2)
            if key[pygame.K_DOWN]:
                player.move(0, 2)
                
        
            # Red Rect gets hit -> Game end 
            if player.rect.colliderect(end_rect):
                score += 1 # Earn a point
                quit() # Keep Playing/Leave game function

            CDcolor = "white"
            if current_time - old_time > 25000:
                CDcolor = "red"

            # Color background, players, wall, countdowm
            screen.fill("black")
            CD = TITLE_FONT.render((countdown), 1, colors.get(CDcolor))
            xd = WIDTH//2 - (CD.get_width()//2)
            screen.blit(CD, (xd, 30))\

            for wall in walls:
                pygame.draw.rect(screen, (255, 255, 255), wall.rect)
            pygame.draw.rect(screen, (255, 0, 0), end_rect)
            pygame.draw.rect(screen, (255, 200, 0), player.rect)

            pygame.display.flip()
            clock.tick(360)

       
    def quit():
        pygame.time.delay(500)
        screen.fill("red")
        Tie = GIANT_FONT.render(("SCORE: "+ str(score)), 1, Wclr)
        xd = WIDTH//2 - (Tie.get_width()//2)
        screen.blit(Tie, (xd, 200))\

        #creating buttons
        Button_1 = pygame.Rect(150, 550, 150, 50)
        Button_2 = pygame.Rect(400, 550, 150, 50)
        pygame.draw.rect(screen, colors.get("white"), Button_1)
        pygame.draw.rect(screen, colors.get("white"), Button_2)

        # Render yes and no
        text1 = MENU_FONT.render("Keep Playing", 1, colors.get("black"))
        text2 = MENU_FONT.render("Leave Game", 1, colors.get("black"))
        screen.blit(text1, (175, 560))
        screen.blit(text2, (425, 560))
        pygame.display.update()

        # Buttons lead to Level 1 or menu
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    mx = mousePos[0]
                    my = mousePos[1]
                    if Button_1.collidepoint(mx, my):
                        RPS()
                    if Button_2.collidepoint(mx, my):
                        # Save score stuff
                        myFile = open("PygameFile.py\FinalGame\FGScoreL1.txt", 'a')
                        date=datetime.datetime.now()
                        scrLine = str(score)+"       "+ userName + "       "+ date.strftime("%m-%d-%Y")+ "        "+ "Level 3" +"\n"
                        myFile.write(scrLine)     # Print the high score
                        myFile.close() 
                        print(scrLine)
                        menu()
        

    
    def tie():
        # Create "TIE" screen
        pygame.time.delay(500)
        screen.fill("violet")
        Tie = GIANT_FONT.render(("TIE!"), 1, Wclr)
        xd = WIDTH//2 - (Tie.get_width()//2)
        screen.blit(Tie, (xd, 200))\
        
        pygame.display.update() 
        pygame.time.delay(1000)

        RPS() # Go back to RPS

    def lose():
        # Create "LOSE" screen 
        pygame.time.delay(500)
        screen.fill("turquoise")
        Lose = GIANT_FONT.render(("YOU LOST!"), 1, Wclr)
        xd = WIDTH//2 - (Lose.get_width()//2)
        screen.blit(Lose, (xd, 200))\
        
        pygame.display.update() 
        pygame.time.delay(1000)

        RPS() # Go back to RPS


    Game = True
    while Game:
        for event in pygame.event.get(): 
            if event.type==pygame.QUIT: # Quit -> Immediately close window
                    quit()
                
        pygame.display.update() 
        pygame.time.delay(100)

        RPS()



# Leaderboard
def scoreboard():
    #title font
    screen.fill(colorTheme)
    Title = TITLE_FONT.render("Leaderboard", 1, colors.get("yellow"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))\

    # Back button
    Button_Back = pygame.Rect(20, 20, 100, 50)
    pygame.draw.rect(screen, colors.get("red"), Button_Back)
    textBack = MENU_FONT.render("Back", 1, colors.get("black"))
    screen.blit(textBack, (25, 25))
    pygame.display.update()
    pygame.time.delay(50)

    # Open Scoreboard File
    myFile = open("PygameFile.py\FinalGame\FGScoreL1.txt", "r")
    content = myFile.readlines()


    # Print instructions
    li = 150 
    for line in content:
        Scores = MENU_FONT.render(line[0:-1], 1, colors.get('yellow')) 
        screen.blit(Scores, (40, li))
        pygame.display.update()
        pygame.time.delay(1000)
        li += 40 # Add 40 pixels between each printed line

    myFile.close()

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_Back.collidepoint(mx, my):
                    menu()
        

# Exit
def exit():
    screen.fill(colorTheme)
    Title = TITLE_FONT.render("Bye Bye", 1, colors.get("blue"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 250))
    pygame.display.update()
    pygame.time.delay(1000)

    pygame.quit()
    sys.exit()

# Call functions
user()
menu()
