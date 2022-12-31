import pygame as pg

from .enemy.entity import Enemy
from .layout.layout import AliveEnemies, Map, Score
from .player.entity import Player


class GameController:
    is_active = True
    group_enemy = pg.sprite.Group()
    main_screen = pg.display.get_surface()

    def __init__(self):
        self.player = Player()
        self.list_enemies = []
        self.score = 0

        self.layout_map = Map()
        self.layout_score = Score()
        self.layout_alive_enemies = AliveEnemies()

    def generate_enemies(self):
        if len(self.group_enemy.sprites()) <= 20:
            self.list_enemies.append(Enemy(self.group_enemy))

        for enemy in self.list_enemies:
            if not enemy.alive():
                self.group_enemy.remove(enemy)
                self.list_enemies.remove(enemy)

    def draw(self):
        self.generate_enemies()
        self.player.update()

        self.group_enemy.draw(self.main_screen)
        self.group_enemy.update(
            playerRadius=self.player.rect_radius,
            playerRect=self.player.rect,
        )

        self.layout_map.draw()
        self.layout_score.draw(score=self.score)
        self.layout_alive_enemies.draw(group=self.group_enemy.sprites())

    def events(self, event, pos_mouse):
        self.player.events(event)

        [enemy.events(event) for enemy in self.list_enemies]
