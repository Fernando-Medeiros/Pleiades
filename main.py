from datetime import datetime

import pygame as pg

TITLE = 'Pleiades Outpost'
FRAME = 30
DISPLAY = (1000, 1000)


class Main:
    def __init__(self):
        self.init_pygame()
        self.clock = pg.time.Clock()
        self.main_screen = pg.display.set_mode(
            DISPLAY, pg.SCALED | pg.RESIZABLE
        )

        soundtrack = pg.mixer.Sound('static/soundtrack/main.mp3')
        soundtrack.play(-1)

        from src.game import GameController

        self.game_controller = GameController()

    def init_pygame(self):
        pg.init()
        pg.font.init()
        pg.mixer.init()

    def draw(self):
        self.main_screen.fill((0, 0, 0))
        self.game_controller.draw()

    def events(self):
        for event in pg.event.get():

            if event.type == pg.QUIT:
                quit()

            self.game_controller.events(event)

    def update(self):
        self.clock.tick(FRAME)
        self.draw()
        self.events()
        pg.display.set_caption(
            '{} | {:.2f} | {}'.format(
                TITLE,
                self.clock.get_fps(),
                datetime.now().strftime('%H:%M:%S'),
            )
        )
        pg.display.update()


if __name__ == '__main__':
    main = Main()
    while True:
        main.update()
