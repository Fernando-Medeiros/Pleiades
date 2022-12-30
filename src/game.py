import pygame as pg

from .enemy.entity import Enemy
from .player.entity import Player

WHITE = (255, 255, 255)


class GameController:
    is_active = True
    group_enemy = pg.sprite.Group()
    font = pg.font.SysFont('garuda', 20)

    def __init__(self):
        self.player = Player()
        self.list_enemies = []
        self.score = 0

        self.main_screen = pg.display.get_surface()

    def draw_score(self):
        surface = self.font.render('Score: {}'.format(self.score), True, WHITE)
        self.main_screen.blit(surface, (20, 20))

    def draw_alive_enemies(self):
        surface = self.font.render(
            'Enemies: {}'.format(len(self.group_enemy.sprites())),
            True,
            WHITE,
        )
        self.main_screen.blit(surface, (20, 40))

    def generate_enemies(self):
        if len(self.group_enemy.sprites()) <= 20:
            self.list_enemies.append(Enemy(self.group_enemy))

        for enemy in self.list_enemies:
            if not enemy.alive():
                self.group_enemy.remove(enemy)
                self.list_enemies.remove(enemy)

    def draw(self):
        self.generate_enemies()
        self.draw_score()
        self.draw_alive_enemies()

        self.player.update()

        self.group_enemy.draw(self.main_screen)
        self.group_enemy.update(
            playerRadius=self.player.rect_radius, playerRect=self.player.rect
        )

    def events(self, event, pos_mouse):
        self.player.events(event)

        [enemy.events(event) for enemy in self.list_enemies]
