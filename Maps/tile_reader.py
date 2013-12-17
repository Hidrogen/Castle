import pygame
class Map():
    def load_tiles(self, filename, w, h):
        self.tile_list = []
        tilesheet = pygame.image.load(filename).convert_alpha()
        tilesheet_width, tilesheet_height = tilesheet.get_size()
        for j in range(int(tilesheet_width/w)):
            for i in range(int(tilesheet_height/h)):
                self.tile_list.append(tilesheet.subsurface((i*w,h*j,w,h)))

    def load_csv(self, filename):
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

while True:
    pygame.init()
    screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
    screen.fill((250, 250, 250))
    Generate = Map()
    Generate.load_tiles("Castle Tiles.png", 32, 32)
    Generate.load_csv("mapCSV_Group1_Ground.csv")
    Generate.load_csv("mapCSV_Group1_Under_Wall.csv")
    Generate.load_csv("mapCSV_Group1_Wall.csv")
    Generate.load_csv("mapCSV_Group1_Techo(2).csv")
    Generate.load_csv("mapCSV_Group1_Techo.csv")
    pygame.display.flip()
