import pygame

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
        
class Sprite():

    def __init__(self, w, h, sprites, hp, speed, kind, bag):
      Entity.__init__(self, sprites, hp, speed, kind, bag)
      self.images = []
      self.images.append
      spritesheet = pygame.image.load(self.spritesheet_url).convert_alpha()
      spritesheet_width, spritesheet_height = spritesheet.get_size()
      print(range(int(spritesheet_height/h)-1))
      print(range(int(spritesheet_width/w)-1))
      for j in range(int(spritesheet_height/h)):
        self.images.append([])
        for i in range(int(spritesheet_width/w)):
          self.images[j].append(spritesheet.subsurface((i*w,h*j,w,h)))

class Input_System():
    def update(self):
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                Human.velocity.x = 0;
                Human.velocity.y = 1;

    def sprint(self, new_velX, new_velY):
            Human.velocity.x = new_velX
            Human.velocity.y = new_velY

class Physics_System():
    def update(self):
        #Entities debiera ser una lista de entidades a nivel global o algo asi(creo)
        for entity in entities:
            entity.position.x = entity.position.x + entity.velocity.x
            entity.position.y = entity.position.y + entity.velocity.y
            
class Render_System():
    def update(self):
        for entity in entities:
            screen.blit(entity.sprites.images[0][0], (entity.position.x, entity.position.y))

    def animate(self, screen, orientation): #donde orientation es : u, d, l, r
        self.d=[Sprite.images[0][0], Sprite.images[0][1], Sprite.images[0][2]]
        self.l=[Sprite.images[1][0], Sprite.images[1][1], Sprite.images[1][2]]
        self.r=[Sprite.images[2][0], Sprite.images[2][1], Sprite.images[2][2]]
        self.u=[Sprite.images[3][0], Sprite.images[3][1], Sprite.images[3][2]]
        #Reconocer la orientación
        if orientation=="u":
            lista=self.u
        elif orientation=="d":
            lista=self.d
        elif orientation=="r":
            lista=self.r
        elif orientation=="l":
            lista=self.l
        #reemplace la iteracion por un for.   
        for i in range(3):    
            screen.blit(lista[i],(300,250))
            pygame.display.flip()
            pygame.time.Clock().tick(30)
        #screen.blit(self.s2,(300,250))
        #reloj.tick(30)
        #pygame.display.flip()
        #screen.blit(self.s3,(300,250))
        #reloj.tick(30)
        #pygame.display.flip()
        #screen.blit(self.s2,(300,250))
        #reloj.tick(30)
        #pygame.display.flip()
            
#----------------------       
#End
#----------------------

