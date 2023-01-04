import pygame as pg

GREEN = (0, 255, 0)
RED = (200, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

main_screen = pg.display.get_surface()


def pos_center(radius: int) -> tuple[float, float]:
    width, height = main_screen.get_size()
    return (width / 2) - (radius / 2), (height / 2) - (radius / 2)


class Radius:
    radius = 28

    def __init__(self):
        self.field = pg.rect.Rect

    def draw_radius(self, color, radius, width: int = 0) -> pg.rect.Rect:
        return pg.draw.circle(
            main_screen,
            color,
            pos_center(-self.radius),
            radius,
            width,
        )

    def update(self, color, radius, width):
        self.field = self.draw_radius(color, radius, width)


class Player:
    def __init__(self):
        self.defense = 10
        self.life = 25
        self.power = 5
        self.radius = 28
        self.speed = 3

        self.image = pg.image.load('static/image/nave2.png')
        self.rect = self.draw_player()

        self.field_of_life = Radius()
        self.field_of_vision = Radius()

    def animate(self):
        angle = 90
        self.image = pg.transform.rotate(self.image, angle)

    def draw_player(self) -> pg.rect.Rect:
        return main_screen.blit(self.image, pos_center(28))

    def update(self, *args, **kwargs):
        self.radius = self.image.get_width()

        self.animate()
        self.draw_player()

        self.field_of_life.update(RED, self.life * 4, 1)
        self.field_of_vision.update(WHITE, self.radius * 4, 3)

    def events(self, event):
        pass
