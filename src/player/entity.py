import pygame as pg

from .cannon import Cannon
from .radius import Radius

RED = (255, 0, 0)
WHITE = (255, 255, 255)

main_screen = pg.display.get_surface()


def get_pos_center(radius: int) -> tuple[float, float]:
    width, height = main_screen.get_size()
    return (width / 2) - (radius / 2), (height / 2) - (radius / 2)


class Player:
    radius_life = Radius()
    radius_vision = Radius()
    cannon = Cannon()

    def __init__(self):
        self.cannons = 3
        self.defense = 5
        self.life = 55
        self.power = 1
        self.radius = 28
        self.speed = 3

        self.score = 0
        self.fragments = 0

        self.image = pg.image.load('static/image/nave2.png')
        self.rect = pg.rect.Rect

    def _animate_sprite(self):
        angle = 90
        self.image = pg.transform.rotate(self.image, angle)

    def _draw_player(self) -> pg.rect.Rect:
        return main_screen.blit(self.image, get_pos_center(28))

    def update(self, *args, **kwargs):
        self.radius = self.image.get_width()

        self._animate_sprite()
        self.rect = self._draw_player()

        self.radius_life.update(
            color=RED,
            radius=self.life * 1.3,
            posCenter=get_pos_center(-28),
            width=1,
        )
        self.radius_vision.update(
            color=WHITE,
            radius=self.radius * 4,
            posCenter=get_pos_center(-28),
            width=1,
        )

        for index in self.radius_vision.get_collisions(kwargs['l_enemies']):
            self.cannon.load_target(kwargs['l_enemies'][index])

        self.cannon.remove_target()
        self.cannon.draw(self.speed, self.rect.center)

    def events(self, event):
        ...

    def __repr__(self) -> str:
        return 'Player -> life: {}, center: {}'.format(
            self.life, self.rect.center
        )
