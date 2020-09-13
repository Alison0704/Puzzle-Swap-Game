import pygame
import random

pygame.init()
pygame.font.init()

#Create game window
screen = pygame.display.set_mode((800,600))

#Adding images(background,blocks,buttons)
background = pygame.image.load('actual background.png')
blocks = pygame.image.load('blocks.png')
button1 = pygame.image.load('button 1.png')
button2 = pygame.image.load('button 2.png')

#Changing window title
pygame.display.set_caption("Puzzle Swap Game")

#Changing window icon
icon = pygame.image.load('mascot.png')
pygame.display.set_icon(icon)

list_button = []
for i in range(12):
    choice = random.randint(1, 2)
    if choice == 1:
        finalbutton = button1
    else:
        finalbutton = button2
    list_button.append(finalbutton)

def change(key):
    if list_button[key] == button2:
        list_button[key] = []
        list_button[key] = button1
    else:
        list_button[key] = []
        list_button[key] = button2
    if key == 0:
        if list_button[key + 1] == button2:
            list_button[key + 1] = []
            list_button[key + 1] = button1
        else:
            list_button[key + 1] = []
            list_button[key + 1] = button2
    if key == 11:
        if list_button[key - 1] == button2:
            list_button[key - 1] = []
            list_button[key - 1] = button1
        else:
            list_button[key - 1] = []
            list_button[key - 1] = button2
    if key > 0 and key < 11:
            if list_button[key-1] == button2:
                list_button[key-1] = []
                list_button[key-1] = button1
            else:
                list_button[key-1] = []
                list_button[key-1] = button2

            if list_button[key+1] == button2:
                list_button[key+1] = []
                list_button[key+1] = button1
            else:
                list_button[key+1] = []
                list_button[key+1] = button2
startscene = True
gameplay = True
endscene = True
while startscene:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            startscene = False
            gameplay = False
            endscene = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                startscene = False

    pygame.display.update()
while gameplay:
    screen.blit(background,(0,0))
    screen.blit(blocks,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameplay = False
            endscene = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
               change(0)
            if event.key == pygame.K_2:
               change(1)
            if event.key == pygame.K_3:
               change(2)
            if event.key == pygame.K_4:
               change(3)
            if event.key == pygame.K_5:
               change(4)
            if event.key == pygame.K_6:
               change(5)
            if event.key == pygame.K_a:
               change(6)
            if event.key == pygame.K_b:
               change(7)
            if event.key == pygame.K_c:
               change(8)
            if event.key == pygame.K_d:
               change(9)
            if event.key == pygame.K_e:
               change(10)
            if event.key == pygame.K_f:
               change(11)



    #adding the twelve buttons in the game
    screen.blit(list_button[0], (10,30))
    screen.blit(list_button[1], (10, 120))
    screen.blit(list_button[2], (10, 220))
    screen.blit(list_button[3], (10, 310))
    screen.blit(list_button[4], (10, 400))
    screen.blit(list_button[5], (10, 490))
    screen.blit(list_button[6], (710, 30))
    screen.blit(list_button[7], (710, 120))
    screen.blit(list_button[8], (710, 220))
    screen.blit(list_button[9], (710, 310))
    screen.blit(list_button[10], (710, 400))
    screen.blit(list_button[11], (710, 490))

    pygame.display.update()
while endscene:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            endscene = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                startscene = False
    pygame.display.update()