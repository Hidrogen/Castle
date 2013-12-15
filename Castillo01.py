import pygame
import random
import Componentes
screen = pygame.display.set_mode((500, 500))
screen.fill((255,255,255))

input_system = Componentes.Input_System()
physics_system = Componentes.Physics_System()
render_system = Componentes.Render_System()

items = []
human = Componentes.Human(240, 240, 0, 0, "./Sprites/White_Male/White_Male.png", 100, 0, items);
Componentes.entities = [human]
while True:
    screen.fill((255,255,255))
    input_system.update()
    physics_system.update()
    render_system.update(screen)
    pygame.display.flip()
