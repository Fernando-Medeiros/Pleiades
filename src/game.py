import pygame as pg

from .layout.hud import AliveEnemie, Fragment, Life, Map, Score, Stage
from .layout.menu import MenuUI
from .layout.status import StatusUI
from .player.entity import Player
from .stage.stages import generate_enemies_by_stage

main_screen = pg.display.get_surface()


class GameController:
    is_active = True

    group_enemy = pg.sprite.Group()
    hud_alive_enemies = AliveEnemie()
    hud_fragment = Fragment()
    hud_life = Life()
    hud_map = Map()
    hud_score = Score()
    hud_stage = Stage()
    player = Player()
    menu = MenuUI()
    status = StatusUI()

    stage = 1
    list_enemies = []

    def draw(self):
        generate_enemies_by_stage(self.group_enemy, self.list_enemies)

        self.player.update(
            l_enemies=self.list_enemies,
        )

        self.group_enemy.draw(main_screen)
        self.group_enemy.update(
            playerRadius=self.player.radius_vision.field,
            playerRect=self.player.rect,
            playerLife=self.player,
        )

        self.hud_map.draw()
        self.hud_score.draw(score=self.player.score)
        self.hud_fragment.draw(fragments=self.player.fragments)
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
            cannons=self.player.cannons,
        )

    def events(self, event):
        self.player.events(event)
        self.menu.events(event)
        self.status.events(event)
        [enemy.events(event) for enemy in self.list_enemies]
