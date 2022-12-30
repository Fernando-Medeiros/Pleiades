from random import randint

import pygame as pg

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)


def get_pos_center() -> tuple[float, float]:
    width, height = pg.display.get_window_size()
    return width / 2, height / 2


def gen_pos_random() -> tuple[int, int]:
    width, height = pg.display.get_window_size()
    pox_x = randint(-width, width * 2)
    pox_y = randint(-height, height * 2)
    return pox_x, pox_y


class Entity(pg.sprite.Sprite):
    color = YELLOW

    def __init__(self, *groups) -> None:
        super().__init__(*groups)
        self.radius = 32

        self.image = pg.Surface((self.radius, self.radius))

        self.rect = self.image.get_rect()
        self.rect.topleft = gen_pos_random()


class Enemy(Entity):
    speed = 3

    def movement(self):
        c_w, c_h = get_pos_center()

        pos_X = -self.speed if self.rect.x >= c_w else self.speed
        pos_Y = -self.speed if self.rect.y >= c_h else self.speed

        if self.alive() and self.rect.topleft != get_pos_center():
            self.rect.move_ip(pos_X, pos_Y)

    def animation(self, playerRectRadius):
        if self.rect.colliderect(playerRectRadius):
            pass

    def collide_radius(self, playerRectRadius):
        if self.rect.colliderect(playerRectRadius):
            self.color = RED
            self.speed = 2
            self.radius = 24

    def collide_death(self, playerRect):
        if self.rect.colliderect(playerRect):
            self.kill()

    def update(self, *args, **kwargs):
        self.movement()
        self.collide_radius(kwargs['playerRadius'])
        self.collide_death(kwargs['playerRect'])

        pg.draw.circle(
            pg.display.get_surface(),
            self.color,
            self.rect.center,
            self.radius / 3,
            0,
        )

        self.animation(kwargs['playerRadius'])

    def events(self, event, **kwargs):
        pass
