import pygame
import pygame.locals


def load_tiles(filename, w, h):
    tile_table = []
    tile_table.append
    tilesheet = pygame.image.load(filename).convert_alpha()
    tilesheet_width, tilesheet_height = tilesheet.get_size()
    tile_table = []
    for j in range(int(tilesheet_width/w)):
        tile_table.append([])
        for i in range(int(tilesheet_height/h)):
            tile_table[j].append(tilesheet.subsurface((i*w,h*j,w,h)))
    return tile_table

def load_csv(filename, tile_table):
    layer = open(filename)
    column = 0
    row = 0
    for line in layer:
        line = line.split(",")
        for element in line:
            if element == "0":
                screen.blit(tile_table[0][0], (row*32, column*32))
            if element == "167":
                screen.blit(tile_table[10][7], (row*32, column*32))
            if element == "183":
                screen.blit(tile_table[11][7], (row*32, column*32))
            row += 1
            if row >= 16:
                row = 0
        column += 1

if __name__=='__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    screen.fill((250, 250, 250))
    table = load_tiles("Castle Tiles.png", 32, 32)
##    for y, row in enumerate(table):
##        for x, tile in enumerate(row):
##            screen.blit(tile, (x*32, y*32))
    load_csv("mapCSV_Group1_Ground.csv", table)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.locals.QUIT:
        pass
