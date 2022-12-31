from random import randint

import pygame as pg

WHITE = (255, 255, 255)


def get_direction(rect) -> tuple[int, int]:
    width, height = pg.display.get_window_size()
    d_x, d_y = (-1, 1) if rect.y > height / 2 else (1, -1)
    return d_x, d_y


def create_particles(listParticles: list, rect) -> None:
    x, y = rect.center
    d_x, d_y = get_direction(rect)
    listParticles.append(
        {
            'loc': {'x': x, 'y': y},
            'vel': {'x': randint(0, 20) / 10 - d_x, 'y': d_y},
            'timer': randint(1, 4),
        }
    )


def draw_particles(listParticles: list[dict]) -> None:
    for particle in listParticles:
        particle['loc']['x'] += particle['vel']['x']
        particle['loc']['y'] += particle['vel']['y']
        particle['timer'] -= 0.1
        particle['vel']['y'] += 0.1

        pg.draw.circle(
            pg.display.get_surface(),
            WHITE,
            [int(particle['loc']['x']), int(particle['loc']['y'])],
            int(particle['timer']),
        )
        if particle['timer'] <= 0:
            listParticles.remove(particle)
