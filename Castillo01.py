import pygame
import random
import engine
screen = pygame.display.set_mode((500, 500))
screen.fill((255,255,255))

input_system = engine.Input_System()
physics_system = engine.Physics_System()
render_system = engine.Render_System()
Generate = engine.Map()

items = []
human = engine.Human(240, 240, 0, 0, "./Sprites/White_Male/White_Male.png", 100, 0, items);
engine.entities = [human]
while True:
    screen.fill((255,255,255))
    Generate.load_tiles("./Maps/Tiles/Castle Tiles.png", 32, 32)
    Generate.load_csv("./Maps/Layers/mapCSV_Group1_Ground.csv", screen)
    Generate.load_csv("./Maps/Layers/mapCSV_Group1_Under_Wall.csv", screen)
    Generate.load_csv("./Maps/Layers/mapCSV_Group1_Wall.csv", screen)
    Generate.load_csv("./Maps/Layers/mapCSV_Group1_Techo(2).csv", screen)
    Generate.load_csv("./Maps/Layers/mapCSV_Group1_Techo.csv", screen)
    input_system.update(engine.entities[0])
    physics_system.update()
    render_system.update(screen)
    pygame.display.flip()
