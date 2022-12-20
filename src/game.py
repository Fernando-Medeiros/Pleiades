import pygame as pg

from .enemy.entity import Enemy
from .player.entity import Player


class GameController:
    is_active = True

    def __init__(self):
        self.player = Player()
        self.enemy = Enemy()
        

    def draw(self):
        self.player.draw()
        self.enemy.draw()

    def events(self, event, pos_mouse):
        self.player.events(event)
        self.enemy.events(event)