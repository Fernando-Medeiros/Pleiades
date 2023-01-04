import pygame as pg

WHITE = (255, 255, 255)

main_screen = pg.display.get_surface()
font = pg.font.SysFont('garuda', 17)


def get_window_size() -> tuple[int, int]:
    return pg.display.get_window_size()


class Map:
    def draw(self):
        display_scale = pg.transform.scale(main_screen, (200, 200))
        width, height = get_window_size()
        main_screen.blit(display_scale, (width - 200, -20))


class Score:
    def draw(self, **kwargs):
        surface = font.render('Score: {}'.format(kwargs['score']), True, WHITE)
        main_screen.blit(surface, (15, 5))


class Fragment:
    def draw(self, **kwargs):
        surface = font.render(
            'Fragments: {}'.format(kwargs['fragments']), True, WHITE
        )
        main_screen.blit(surface, (15, 25))


class Life:
    def draw(self, **kwargs):
        surface = font.render('Life: {}'.format(kwargs['life']), True, WHITE)
        main_screen.blit(surface, (15, 45))


class AliveEnemie:
    def draw(self, **kwargs):
        surface = font.render(
            'Enemies: {}'.format(len(kwargs['group'])), True, WHITE
        )
        main_screen.blit(surface, (15, 65))


class Stage:
    def draw(self, **kwargs):
        surface = font.render('Stage: {}'.format(kwargs['stage']), True, WHITE)
        main_screen.blit(
            surface, (main_screen.get_width() / 2 - surface.get_width() / 2, 5)
        )
