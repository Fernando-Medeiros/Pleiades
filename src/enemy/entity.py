from random import randint

import pygame as pg

from .particles import create_particles, draw_particles

RED = (255, 0, 0)
YELLOW = (255, 255, 0)


def get_pos_center() -> tuple[int, int]:
    width, height = pg.display.get_window_size()
    return int(width / 2), int(height / 2)


def gen_pos_random() -> tuple[int, int]:
    width, height = pg.display.get_window_size()
    pox_x = randint(-width, width * 2)
    pox_y = randint(-height, height * 2)
    return pox_x, pox_y


def update_movement(velocity: float, pos: float, posCenter: int) -> float:
    if pos >= posCenter:
        return -velocity
    elif pos in range(posCenter - 10, posCenter + 10):
        return 0
    else:
        return velocity


class Entity(pg.sprite.Sprite):
    def __init__(self, *groups) -> None:
        super().__init__(*groups)

        self.image = pg.image.load('static/image/nave1.png')
        self.radius = self.image.get_width()
        self.rect = self.image.get_rect()
        self.rect.topleft = gen_pos_random()

        self.list_particles = []


class Enemy(Entity):
    vel = 3

    def movement(self):
        c_w, c_h = get_pos_center()
        pos_X = update_movement(self.vel, self.rect.x, c_w)
        pos_Y = update_movement(self.vel, self.rect.y, c_h)

        if self.alive():
            self.rect.move_ip(pos_X, pos_Y)

    def draw_particles(self):
        if len(self.list_particles) <= 33:
            create_particles(self.list_particles, self.rect)
            draw_particles(self.list_particles)

    def collide_radius(self, **kwargs):
        if self.rect.colliderect(kwargs['playerRadius']):
            self.vel = 2

    def collide_and_die(self, **kwargs):
        if self.rect.colliderect(kwargs['playerRect']):
            self.kill()

    def update(self, *args, **kwargs):
        self.movement()
        self.draw_particles()
        self.collide_radius(**kwargs)
        self.collide_and_die(**kwargs)

    def events(self, event, **kwargs):
        pass
