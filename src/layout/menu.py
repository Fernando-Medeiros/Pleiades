import pygame as pg

GREEN = (0, 255, 0)
RED = (200, 0, 0)
WHITE = (255, 255, 255)

main_screen = pg.display.get_surface()
font = pg.font.SysFont('garuda', 17)


def draw_rect(x_y, w_h, width=1, border=(7, 7, 7, 7)) -> pg.rect.Rect:
    return pg.draw.rect(main_screen, WHITE, (x_y, w_h), width, *border)


def draw_text(x_y, texts) -> pg.surface.Surface:
    surface = font.render(texts, True, WHITE)
    main_screen.blit(surface, x_y)
    return surface


def draw_icon(x_y, texts) -> pg.rect.Rect:
    x, y = x_y
    text = draw_text(x_y, f' {texts} ')
    draw_text((x + (text.get_width() // 3.5), y + 30), '[ + ]')
    return draw_rect(x_y, (text.get_width(), text.get_height() + 40))


class MenuUI:
    is_active = False
    centerx = main_screen.get_width()
    centery = main_screen.get_width()

    def __init__(self):
        self.power = pg.rect.Rect
        self.defense = pg.rect.Rect
        self.radius = pg.rect.Rect
        self.res_health = pg.rect.Rect
        self.speed = pg.rect.Rect

    def update(self):
        if self.is_active:
            draw_rect([0, 900], [self.centerx / 2, 100])

            self.power = draw_icon([5, 915], 'Power')
            self.defense = draw_icon([self.power.right + 15, 915], 'Defense')
            self.radius = draw_icon([self.defense.right + 15, 915], 'Radius')
            self.speed = draw_icon([self.radius.right + 15, 915], 'Speed')
            self.res_health = draw_icon(
                [self.speed.right + 15, 915], 'Res Health'
            )

        else:
            draw_text(
                (50, self.centery - 30),
                'Press Space to open or close the menu',
            )

    def events(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                self.is_active = False if self.is_active else True
