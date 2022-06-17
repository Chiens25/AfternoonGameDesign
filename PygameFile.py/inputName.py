# Sydmey Chien
# 6/17/22
# Get user name
# Create screen
# Title = Enter your name 
# Fonts
# Create Box
# Create name var
# Add the letter
# If  press BACKSPACE delete last character
# If press RETURN they are done

import pygame, os, time, random, math, datetime, sys
from pygame import mixer
pygame.init()

# Colors
colors = {"white":(255,255,255), "grey":(245,245,245), "black":(0,0,0), "red":(255,0,0), "green":(0,255,0), "blue":(0,0,255), "pink":(204,0,204), "orange":(255,128,0), "yellow":(255,255,0), "purple":(127,0,255)}

# print(pygame.font.get_fonts())
# pygame.time.delay(10000)
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)

os.system('cls')

# General Variables
WIDTH = 700   # Amount of pixels
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Input Username") # title of the window
clock = pygame.time.Clock()

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
                    pygame.quit()
                    sys.exit()
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
