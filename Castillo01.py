import pygame
from pygame.locals import *       
from Componentes import *          
import pygame
from pygame.locals import *
reloj=pygame.time.Clock()
width=800
height=600
screen = pygame.display.set_mode((width, height))
pygame.key.set_repeat(1, 2);
mapa=pygame.image.load("./Sprites/Mapa/Laberinto_1.png")
white_male=Sprite( 32, 32,"./Sprites/White_Male/White_male.png", 10, 1, 1, [])
#Centrado de mapa
x,y=-440,-420
moverx,movery=0,0
speed = 1
#wh=hcentro
orient="0"
while True:
    for event in pygame.event.get():
        moverx,movery=0,0
        sprint = pygame.key.get_mods() & KMOD_SHIFT
        if sprint:
            speed = 3
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            orient="l"
            moverx= 20
        if keys[pygame.K_d]:
            orient="r"
            moverx= -20
        if keys[pygame.K_w]:
            orient="u"
            movery= 20
        if keys[pygame.K_s]:
            orient="d"
            movery= -20
        x,y=x+moverx*speed,y+movery*speed
        speed = 1
        screen.fill((0,0,0))
        screen.blit(mapa,(x,y))
        if orient !="0":
            white_male.animar(screen,orient)
        else:
            white_male.initial_position(screen,300,250)
        pygame.display.flip()
        
