import pygame as pg

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

class Player:

    def __init__(self) -> None:
        self.color = WHITE
        self.radius = 28
        self.width = 4

        self.player = self._draw_player()
        self.player_radius = self._draw_radius()


    def pos_center(self) -> tuple:
        width, height = pg.display.get_window_size()
        width = (width / 2 ) - self.radius / 4
        height = (height / 2) - self.radius / 4
        return (width, height)

    def _draw_player(self):
        return pg.draw.circle(pg.display.get_surface(), self.color, self.pos_center(), self.radius, self.width)

    def _draw_radius(self):
        color = GREEN
        radius = self.radius * 8
        width = 1
        return pg.draw.circle(pg.display.get_surface(), color, self.pos_center(), radius, width)

    def draw(self):
        self.player
        self.player_radius

    def events(self, event):
        pass