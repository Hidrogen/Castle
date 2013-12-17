import pygame
from pygame.locals import *

#----------------------
#Components
#----------------------

class Position():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
class Velocity():
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Sprite():
    def __init__(self, spritesheet_url, w, h):
        self.images = []
        self.images.append
        spritesheet = pygame.image.load(spritesheet_url).convert_alpha()
        spritesheet_width, spritesheet_height = spritesheet.get_size()
        for j in range(int(spritesheet_height/h)):
            self.images.append([])
            for i in range(int(spritesheet_width/w)):
                self.images[j].append(spritesheet.subsurface((i*w,h*j,w,h)))

class Health():
    def __init__(self, hp):
        self.health = hp

class Type():
    def __init__(self, kind):
        self.kind = kind
        #Human = 0
        #Monster = 1
        #Item = 2
class Inventory():
    def __init__(self, items):
        self.owned = items
    #existe una lista cuyos elementos se refieren a las llaves, en esta clase se indica cuales tiene el jugador.
        
#----------------------       
#Entities
#----------------------
       
class Human():
    def __init__(self, xp, yp, xv, yv, sprite_loc, hp, kind, bag):
        self.position = Position(xp,yp)
        self.velocity = Velocity(xv,yv)
        self.sprites = Sprite(sprite_loc, 32, 32)
        self.health = Health(hp)
        self.bag = Inventory(bag)
        self.kind = Type(kind)

#----------------------       
#Systems
#----------------------

class Input_System():
    def __init__(self):
        self.boost = 1
        
    def update(self, element):
        #element se refiere al elemento que  va a recibir los cambios de la lista entities
        ev = pygame.event.get()
        for event in ev:
            self.sprint()
            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_a]:
                    for entity in entities:
                        entity.velocity.x = -5*self.boost
                if keys[pygame.K_d]:
                    for entity in entities:
                        entity.velocity.x = 5*self.boost
                if keys[pygame.K_w]:
                    for entity in entities:
                        entity.velocity.y = -5*self.boost
                if keys[pygame.K_s]:
                    for entity in entities:
                        entity.velocity.y = 5*self.boost
            if event.type == pygame.KEYUP:
                if event.key==pygame.K_a:
                    for entity in entities:
                        entity.velocity.x = 0
                if event.key==pygame.K_d:
                    for entity in entities:
                        entity.velocity.x = 0
                if event.key==pygame.K_w:
                    for entity in entities:
                        entity.velocity.y = 0
                if event.key==pygame.K_s:
                    for entity in entities:
                        entity.velocity.y = 0
    def sprint(self):
        if pygame.key.get_mods() & KMOD_SHIFT:
            self.boost = 2
        else:
            self.boost = 1

class Physics_System():
    def update(self):
        #Entities debiera ser una lista de entidades a nivel global o algo asi(creo)
        for entity in entities:
            entity.position.x = entity.position.x + entity.velocity.x
            entity.position.y = entity.position.y + entity.velocity.y
            
class Render_System():
    def __init__(self):
        self.counter = 0
        self.lista = []
        self.id = "d"
        
    def update(self, screen):
        self.animate()
        for entity in entities:
##-----------------------------Idle-------------------------------
            if entity.velocity.x == 0 and entity.velocity.y == 0:
                if self.id == "d":
                    self.lista = self.d
                    self.counter = 1
                if self.id == "l":
                    self.lista = self.l
                    self.counter = 1
                if self.id == "r":
                    self.lista = self.r
                    self.counter = 1
                if self.id == "u":
                    self.lista = self.u
                    self.counter = 1
##-----------------------------Idle-------------------------------
            screen.blit(self.lista[self.counter], (entity.position.x, entity.position.y))
            if self.counter >= 2:
                self.counter = 0
            else:
                self.counter += 1
        pygame.time.Clock().tick(30)

    def animate(self): #donde orientation es : u, d, l, r
## Por cosas de facilidad orientation es definido por la velocidad que tiene la entidad
        for entity in entities:
            self.d=[entity.sprites.images[0][0], entity.sprites.images[0][1], entity.sprites.images[0][2]]
            self.l=[entity.sprites.images[1][0], entity.sprites.images[1][1], entity.sprites.images[1][2]]
            self.r=[entity.sprites.images[2][0], entity.sprites.images[2][1], entity.sprites.images[2][2]]
            self.u=[entity.sprites.images[3][0], entity.sprites.images[3][1], entity.sprites.images[3][2]]
        #Reconocer la orientación
        for entity in entities:
            if entity.velocity.y < 0:
                self.lista=self.u
                self.id = "u"
            if entity.velocity.y > 0:
                self.lista=self.d
                self.id = "d"
            if entity.velocity.x > 0:
                self.lista=self.r
                self.id = "r"
            if entity.velocity.x < 0:
                self.lista=self.l
                self.id = "l"
        #reemplace la iteracion por un for.   
        pygame.time.Clock().tick(30)

#----------------------       
#Map
#----------------------

class Map():
    def load_tiles(self, filename, w, h):
        self.tile_list = []
        tilesheet = pygame.image.load(filename).convert_alpha()
        tilesheet_width, tilesheet_height = tilesheet.get_size()
        for j in range(int(tilesheet_width/w)):
            for i in range(int(tilesheet_height/h)):
                self.tile_list.append(tilesheet.subsurface((i*w,h*j,w,h)))

    def load_csv(self, filename, screen):
        layer = open(filename)
        column = 0
        row = 0
        for line in layer:
            line = line.split(",")
            for element in line:
                screen.blit(self.tile_list[int(element)], (row*32, column*32))
                row += 1
                if row >= 32:
                    row = 0
            column += 1

#----------------------       
#Other
#----------------------
#Al parecer las listas deben existir como vacias en este archivo. Me refiero a las listas como entity       
entities = []
