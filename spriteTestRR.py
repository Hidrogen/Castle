#Components
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
#----------------------
#Entities

class Human():
    def __init__(self, xp, yp, xv, yv, sprite_loc):
        self.position = Position(xp,yp)
        self.velocity = Velocity(xv,yv)
        self.sprites = Sprite(sprite_loc, 32, 32)

#----------------------
#Systems

class Entity_Manager():
    def __init__(self):
        self.mask = []
        self.entities_holder = []
    def create_entity(self,entity):
        self.mask = []
        self.entities_holder.append(entity)
    def destroy_entity(self, entity_index):
        self.mask.remove(mask[entity_index]);
        self.entities_holder.remove(entities_holder[entity_index]);

class Input_System():
    def update(self):
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    for entity in entities:
                        entity.velocity.x = -2;
                elif event.key==pygame.K_d:
                    for entity in entities:
                        entity.velocity.x = 2;
                elif event.key==pygame.K_w:
                    for entity in entities:
                        entity.velocity.y = -2;
                elif event.key==pygame.K_s:
                    for entity in entities:
                        entity.velocity.y = 2;
            if event.type == pygame.KEYUP:
                if event.key==pygame.K_a:
                    for entity in entities:
                        entity.velocity.x = 0;
                elif event.key==pygame.K_d:
                    for entity in entities:
                        entity.velocity.x = 0;
                elif event.key==pygame.K_w:
                    for entity in entities:
                        entity.velocity.y = 0;
                elif event.key==pygame.K_s:
                    for entity in entities:
                        entity.velocity.y = 0;


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

#----------------------
#Testing
import pygame
import random
screen = pygame.display.set_mode((500, 500))
screen.fill((255,255,255))

entity_manager = Entity_Manager()
input_system = Input_System()
physics_system = Physics_System()
render_system = Render_System()

human = Human(240, 240, 0, 0, "./Sprites/White_Male/White_Male.png");
entities = [human]
fpsClock = pygame.time.Clock()
while True:
    screen.fill((255,255,255))
    input_system.update()
    physics_system.update();
    render_system.update();
    pygame.display.update()
    fpsClock.tick(60)
