import pygame as pg

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)


def pos_center(radius: int) -> tuple[float, float]:
    width, height = pg.display.get_window_size()
    return (width / 2) - (radius / 2), (height / 2) - (radius / 2)


class Radius:
    radius = 28
    width = 1

    def _draw_radius(self, color, radius, width: int = 0) -> pg.rect.Rect:
        return pg.draw.circle(
            pg.display.get_surface(),
            color,
            pos_center(-self.radius),
            radius,
            width,
        )


class Player(Radius):
    def __init__(self):
        self.image = pg.image.load('static/image/nave2.png')
        self.rect = self._draw_player()
        self.rect_radius = self._draw_radius(GREEN, self.radius * 8, 3)

    def _draw_player(self) -> pg.rect.Rect:
        return pg.display.get_surface().blit(
            self.image, pos_center(self.radius)
        )

    def update(self, *args, **kwargs):
        self._draw_player()
        self._draw_radius(GREEN, self.radius * 8, 3)
        self._draw_radius(YELLOW, self.radius * 4, 1)
        self._draw_radius(WHITE, self.radius * 2, 1)

    def events(self, event):
        pass
