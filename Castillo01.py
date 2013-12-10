
class Sprite:
    def __init__(self,x,y,z):
        self.a=x
        self.b=y
        self.c=z
    def cargar(self):
        self.s1=pygame.image.load(self.a)
        self.s2=pygame.image.load(self.b)
        self.s3=pygame.image.load(self.c)        
    def animar(self):
        screen.blit(self.s1,(300,250))
        pygame.display.flip()
        reloj.tick(30)
        screen.blit(self.s2,(300,250))
        reloj.tick(30)
        pygame.display.flip()
        screen.blit(self.s3,(300,250))
        reloj.tick(30)
        pygame.display.flip()
        screen.blit(self.s2,(300,250))
        reloj.tick(30)
        pygame.display.flip()
        
        
import pygame
from pygame.locals import *
reloj=pygame.time.Clock()
height=600
width=500
screen = pygame.display.set_mode((width, height))
pygame.key.set_repeat(1, 2);
mapa=pygame.image.load("./Sprites/Mapa/Laberinto_1.png")

#Sprite cuando parte el juego
hcentro=Sprite("./Sprites/White_Male/White_Male_abajo2.png","./Sprites/White_Male/White_Male_abajo2.png","./Sprites/White_Male/White_Male_abajo2.png")
#Sprites de movimiento
hizq=Sprite("./Sprites/White_Male/White_Male_izq1.png","./Sprites/White_Male/White_Male_izq2.png","./Sprites/White_Male/White_Male_izq3.png")
hder=Sprite("./Sprites/White_Male/White_Male_der1.png","./Sprites/White_Male/White_Male_der2.png","./Sprites/White_Male/White_Male_der3.png")
harriba=Sprite("./Sprites/White_Male/White_Male_arriba1.png","./Sprites/White_Male/White_Male_arriba2.png","./Sprites/White_Male/White_Male_arriba3.png")
habajo=Sprite("./Sprites/White_Male/White_Male_abajo1.png","./Sprites/White_Male/White_Male_abajo2.png","./Sprites/White_Male/White_Male_abajo3.png")
#Cargando imagenes
hcentro.cargar()
hizq.cargar()
hder.cargar()
harriba.cargar()
habajo.cargar()

#Centrado de mapa
x,y=-440,-420
moverx,movery=0,0
speed = 1
wh=hcentro
while True:
    for event in pygame.event.get():
        moverx,movery=0,0
        sprint = pygame.key.get_mods() & KMOD_SHIFT
        if sprint:
            speed = 3
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            wh=hizq
            moverx= 20
        if keys[pygame.K_d]:
            wh=hder
            moverx= -20
        if keys[pygame.K_w]:
            wh=harriba
            movery= 20
        if keys[pygame.K_s]:
            wh=habajo
            movery= -20  

        x,y=x+moverx*speed,y+movery*speed
        speed = 1


        
        screen.fill((0,0,0))
        screen.blit(mapa,(x,y))
        #Animacion de sprites
        wh.animar()
        pygame.display.flip()
        
