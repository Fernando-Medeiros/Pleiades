import pygame as pg


class Radius:
    def __init__(self):
        self.field = pg.rect.Rect

    def _draw(self, color, radius, posCenter, width: int = 0) -> pg.rect.Rect:
        return pg.draw.circle(
            pg.display.get_surface(),
            color,
            posCenter,
            radius,
            width,
        )

    def get_collisions(self, listEnemies) -> list[int]:
        return self.field.collidelistall(listEnemies)

    def update(self, **kwargs):
        self.field = self._draw(
            kwargs['color'],
            kwargs['radius'],
            kwargs['posCenter'],
            kwargs['width'],
        )
