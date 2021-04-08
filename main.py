import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

#EVENTS

#Title and Icon(from flaticon)
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('icon.svg')
pygame.display.set_icon(icon)


#player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg, (playerX, playerY))

#GameLoop
running = True
while running:
    screen.fill((255,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    player()
    pygame.display.update()
