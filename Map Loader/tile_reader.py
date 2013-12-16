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
def load_csv(filename):
    layer = open(filename)
    for line in layer:
        line = line.split(",")
        for element in line:
            #if "0":
                #blit la tile correspondiente a 0. (vacio en este caso)

if __name__=='__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    screen.fill((250, 250, 250))
    load_csv("mapCSV_Group1_Ground.csv")
    table = load_tiles("Castle Tiles.png", 32, 32)
    for y, row in enumerate(table):
        for x, tile in enumerate(row):
            screen.blit(tile, (x*32, y*32))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.locals.QUIT:
        pass
#este codigo lo saque de wiki sheep. No es mio.
