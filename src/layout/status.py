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
    text = draw_text(x_y, f' {texts} ')
    return draw_rect(x_y, text.get_size())


class StatusUI:
    is_active = False
    centerx = main_screen.get_width()
    centery = main_screen.get_width()

    def update(self, **kwargs):
        if self.is_active:
            draw_rect([self.centerx / 2, 900], [self.centerx / 2, 100])

            x, y = self.centerx / 2 + 15, 915

            for key, value in kwargs.items():
                icon = draw_icon((x, y), f'{key.capitalize()} -> {value}')

                if icon.x >= 800:
                    x, y = (self.centerx / 2) + 15, y + (icon.height + 10)
                else:
                    x = icon.right + 15

        else:
            draw_text(
                (
                    self.centerx / 2 + 150,
                    self.centery - 30,
                ),
                'Press Enter to open or close the status',
            )

    def events(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                self.is_active = False if self.is_active else True
