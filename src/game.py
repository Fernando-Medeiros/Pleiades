import pygame as pg

from .enemy.entity import Enemy
from .layout.hud import AliveEnemie, Fragment, Life, Map, Score, Stage
from .layout.menu import MenuUI
from .layout.status import StatusUI
from .player.entity import Player

main_screen = pg.display.get_surface()


class GameController:
    is_active = True
    group_enemy = pg.sprite.Group()

    def __init__(self):
        self.stage = 1
        self.score = 0
        self.fragments = 0
        self.list_enemies = []

        self.player = Player()

        self.hud_alive_enemies = AliveEnemie()
        self.hud_fragment = Fragment()
        self.hud_life = Life()
        self.hud_map = Map()
        self.hud_score = Score()
        self.hud_stage = Stage()

        self.menu = MenuUI()
        self.status = StatusUI()

    def generate_enemies(self):
        if len(self.group_enemy.sprites()) <= 29:
            self.list_enemies.append(Enemy(self.group_enemy))

        for enemy in self.list_enemies:
            if not enemy.alive():
                self.group_enemy.remove(enemy)
                self.list_enemies.remove(enemy)

    def draw(self):
        self.generate_enemies()
        self.player.update()

        self.group_enemy.draw(main_screen)
        self.group_enemy.update(
            playerRadius=self.player.field_of_vision.field,
            playerRect=self.player.rect,
            playerLife=self.player,
        )

        self.hud_map.draw()
        self.hud_score.draw(score=self.score)
        self.hud_fragment.draw(fragments=self.fragments)
        self.hud_life.draw(life=self.player.life)
        self.hud_alive_enemies.draw(group=self.group_enemy.sprites())
        self.hud_stage.draw(stage=self.stage)

        self.menu.update()
        self.status.update(
            life=self.player.life,
            power=self.player.power,
            defense=self.player.defense,
            radius=self.player.radius,
            speed=self.player.speed,
        )

    def events(self, event):
        self.player.events(event)
        self.menu.events(event)
        self.status.events(event)
        [enemy.events(event) for enemy in self.list_enemies]
