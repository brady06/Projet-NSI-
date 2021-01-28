#Pour cette premire partie de projet le but été de se familiariser avec le module pygame et de comprendre son fonctionnement. 
#Nous avons donc pour l'instant seuleument réussi a crée la boucle qui fait tourner le jeux, crée la fenêtre de jeux et nous commencons a implementé les premiers sprite (caractère de jeu).

import pygame
import random

#Initialise pygame
pygame.init ()

#Crée l'écran
screen = pygame.display.set_mode((1000, 1000))

#Crée un titre et des icones
pygame.display.set_caption("We Have NO Choice!?!")
icon = pygame.image.load('LOGO.png')
pygame.display.set_icon(icon)

#Joueur
playerImg =pygame.image.load('laser-gun.png')
playerImg = pygame.transform.scale(playerImg, (64, 64))
playerX = 500
playerY = 900
playerX_change = 0  
playerY_change = 0

def player(x,y):
    screen.blit(playerImg,(x,y))
#Enemy
EnemyImg =pygame.image.load('apple.png')
EnemyImg = pygame.transform.scale(EnemyImg, (64, 64))
#Fait apparaitre le personnage dans des coordonées choisit au hasard
EnemyX = random.randint(0,1000)
EnemyY = random.randint(50,500)
EnemyX_change = 0  
EnemyY_change = 0

def Enemy(x,y):
    screen.blit(EnemyImg,(x,y))



# Tourne le joue en boucle
running = True
while running:
    #Change la couleur de l'écran
    screen.fill((128,128,128))
    #playerX += 0.1
    #print(playerX)
    #Permet de fermez la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Lorsque qu'un touche est pressé vérifier si c'est une touche directionel
        if event.type == pygame.KEYDOWN:
            #print("A key has been pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
                #print("Left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
                #print("Right arrow is pressed")
            if event.key == pygame.K_UP:
                playerY_change = -0.5
                #print("Up arrow is pressed")
            if event.key == pygame.K_DOWN:
                playerY_change = 0.5
                #print("Down arrow is pressed")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
                #print("Key has been released")

    playerY += playerY_change
    playerX += playerX_change
    
    #Permet de délimiter la fenetre, empeche le joueur d'aller en dehors de la fenetre
    if playerX <= 0:
        playerX =0
    elif playerX >= 984:
        playerX = 984
        
    if playerY <= 0:
        playerY = 0
    elif playerY >= 984:
        playerY = 984
    
        
    player(playerX,playerY)
    Enemy(EnemyX,EnemyY)
    pygame.display.update()


            
            
