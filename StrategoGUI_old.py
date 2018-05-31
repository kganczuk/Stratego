import pygame as pg
import itertools
import Stratego

BLACK = pg.Color('black')
GREY = pg.Color('grey')
RED = pg.Color('red')
BLUE = pg.Color('blue')
LEFT_BUTTON = (1, 0, 0)

class StrategoGUI:
    def __init__(self, board_size, tile_size):
        pg.init()
        self.colors = itertools.cycle((RED, BLUE))
        self.screen = pg.display.set_mode((board_size*tile_size, board_size*tile_size))
        self.clock = pg.time.Clock()
        self.tile_size = tile_size
        self.width = self.height = board_size*tile_size
        self.background = pg.Surface((self.width, self.height))
        self.background.fill(GREY)
        self.draw_board(self.height, self.width, tile_size, self.background)
        self.run(tile_size, self.background, self.screen)

    def draw_board(self, height, width, tile_size, background):
        for y in range(0, height, tile_size):
            for x in range(0, width, tile_size):
                self.draw_field(x, y, tile_size, BLACK, background, 1)

    def run(self, tile_size, background, screen):
        game_exit = False
        while not game_exit:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game_exit = True
                else:
                    x, y = int(pg.mouse.get_pos()[0] / tile_size) * tile_size, int(pg.mouse.get_pos()[1] / tile_size) * tile_size
                    if pg.mouse.get_pressed() == LEFT_BUTTON:
                        self.draw_field(x, y, tile_size, next(self.colors), background)

            screen.blit(background, (0, 0))

            pg.display.flip()
            self.clock.tick(100)

        pg.quit()

    def draw_field(self, x, y, size, color, background, width=0):
        rect = (x, y, size, size)
        pg.draw.rect(background, color, rect, width)


gui = StrategoGUI(10, 100)