from random import randint

import pygame as pg

from .particles import create_particles, draw_particles

RED = (255, 0, 0)


def get_pos_center() -> tuple[int, int]:
    width, height = pg.display.get_surface().get_size()
    return int(width / 2), int(height / 2)


def gen_pos_random() -> tuple[int, int]:
    width, height = pg.display.get_surface().get_size()
    pox_x = randint(-width, width * 2)
    pox_y = randint(-height, height * 2)
    return pox_x, pox_y


def direction(speed: float, posSelf: int, posOther: int) -> float | int:
    if posSelf > posOther:
        return -speed
    elif posSelf in range(posOther - 5, posOther + 5):
        return 0
    else:
        return speed


class Enemy(pg.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.life = 5
        self.speed = 3

        self.list_particles = []

        self.image = pg.image.load('static/image/nave1.png')
        self.radius = self.image.get_width()
        self.rect = self.image.get_rect()
        self.rect.topleft = gen_pos_random()

    def _movement(self):
        c_w, c_h = get_pos_center()
        pos_X = direction(self.speed, self.rect.x, c_w)
        pos_Y = direction(self.speed, self.rect.y, c_h)

        if self.alive():
            self.rect.move_ip(pos_X, pos_Y)

    def _animate(self):
        angle = -90
        self.image = pg.transform.rotate(self.image, angle)

    def _draw_particles(self):
        if len(self.list_particles) <= 33:
            create_particles(self.list_particles, self.rect)
            draw_particles(self.list_particles)

    def _collide_radius(self, playerRadius):
        if self.rect.colliderect(playerRadius):
            self.speed = 1

    def _collide_and_die(self, playerLife, playerRect):
        if self.rect.colliderect(playerRect):
            playerLife.life -= 1
            self.kill()

    def _check_life_and_die(self):
        if self.life <= 0:
            self.kill()

    def update(self, *args, **kwargs):
        self._check_life_and_die()

        self._animate()
        self._movement()
        self._draw_particles()
        self._collide_radius(kwargs['playerRadius'])
        self._collide_and_die(kwargs['playerLife'], kwargs['playerRect'])

    def events(self, event, **kwargs):
        ...

    def __str__(self) -> str:
        return 'Enemy -> life: {}, speed: {}, center: {}'.format(
            self.life, self.speed, self.rect.center
        )
