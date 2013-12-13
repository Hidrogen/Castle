class Entity:
    def __init__(self, sprites, hp, speed, kind, bag):
        self.i0 = sprites[0]
        self.i1 = sprites[1]
        self.i2 = sprites[2]
        self.health = hp
        self.speed = speed
## parametro kind es un numero entero 0,1 o 2.
        #0 = Humano
        #1 = Monstruo
        #2 = Item
        if kind == 0:
            self.human = True
            self.monster = False
            self.item = False
        elif kind == 1:
            self.human = False
            self.monster = True
            self.item = False
        elif kind == 2:
            self.human = False
            self.monster = False
            self.item = True
## bag es una ista vacia inicialmente    
        self.bag = bag


class Sprite(Entity):
    #hay que cambiar estos self por los definidos en la entidad.
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

sprites_human= []#Sublistas con los directorios de los spritesb = Sprite()
##class Health(Player):
##    hp el parametro que entra en la entidad Player es un numero entero
##    def death(self):
##        if self.health <= 0:
##            falta animacion para la muerte. Y romper el main loop o algo.


class Speed(Entity):
    def current_speed(self):
        return self.speed
    def sprint(self, new_speed):
        self.speed = new_speed

class Type(Entity):
    def get_kind(self):
        if self.human:
            return 0
        if self.monster:
            return 1
        if self.item:
            return 2
## la idea de la clase Team es evaluar cuando colisionen son ambos 0, ambos 1 o distintos.

class Inventory(Entity):
    #existe una lista cuyos elementos se refieren a las llaves, en esta clase se indica cuales tiene el jugador.
    def get_item(self):
#en caso de coalision con un item agregarlo al inventario
        #self.bag.append(entidad llave)
        
in_game_items = []#Aca se refieren como elementos las entidades llave.

class Coalition(Entity):
    #realmente no se como hacer esto.
    #evaluar los limites del sprite y sumarlos propiamente a la posicion y ver si se toca con algo?
    #tiene que haber un metodo que no demande tantos recursos y sea mas facil.

class AI(Entity):
## este dejarlo para despues.    

            

