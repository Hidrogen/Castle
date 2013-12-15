import pygame
import random
import engine
screen = pygame.display.set_mode((500, 500))
screen.fill((255,255,255))

input_system = engine.Input_System()
physics_system = engine.Physics_System()
render_system = engine.Render_System()

items = []
human = engine.Human(240, 240, 0, 0, "./Sprites/White_Male/White_Male.png", 100, 0, items);
engine.entities = [human]
while True:
    screen.fill((255,255,255))
    input_system.update(engine.entities[0])
    physics_system.update()
    render_system.update(screen)
    pygame.display.flip()
