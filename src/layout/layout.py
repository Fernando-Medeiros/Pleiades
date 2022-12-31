import pygame as pg

WHITE = (255, 255, 255)

main_screen = pg.display.get_surface()
font = pg.font.SysFont('garuda', 20)


def get_window_size() -> tuple[float, float]:
    return pg.display.get_window_size()


class Map:
    def draw(self):
        map = pg.transform.scale(main_screen, (200, 200))
        width, height = get_window_size()
        main_screen.blit(map, (width - 200, -20))


class Score:
    def draw(self, **kwargs):
        surface = font.render('Score: {}'.format(kwargs['score']), True, WHITE)
        main_screen.blit(surface, (20, 20))


class AliveEnemies:
    def draw(self, **kwargs):
        surface = font.render(
            'Enemies: {}'.format(len(kwargs['group'])), True, WHITE
        )
        main_screen.blit(surface, (20, 40))
