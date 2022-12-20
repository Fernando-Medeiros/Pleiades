import pygame as pg

NAME = 'Pleiades Outpost'
FRAME = 30
DISPLAY = 1000, 1000

class Main:
    def __init__(self):
        self.init_game()
        self.clock = pg.time.Clock()
        self.main_screen = pg.display.set_mode(DISPLAY, pg.SCALED | pg.RESIZABLE)


    def init_game(self):
        pg.init()
        pg.font.init()
        pg.mixer.init()


    def draw(self):
        pass


    def events(self):
        for event in pg.event.get():

            if event.type == pg.QUIT:
                quit()
        

    def update(self):
        self.clock.tick(FRAME)
        self.draw()
        self.events()
        pg.display.set_caption('{} | {:.2f}'.format(NAME, self.clock.get_fps()))
        pg.display.update()


if __name__ == '__main__':
    main = Main()
    while True:
        main.update()
