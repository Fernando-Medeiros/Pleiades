import pygame as pg

RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

main_screen = pg.display.get_surface()
font = pg.font.SysFont('garuda', 17)


def get_direction(speed: float, posSelf: int, posOther: int) -> float | int:
    if posSelf > posOther:
        return -speed
    elif posSelf in range(posOther - 5, posOther + 5):
        return 0
    else:
        return speed


class CannonBall:
    radius = 7
    width = 2

    def __init__(self, posCenter):
        self.timer = 5
        self.rect = pg.draw.circle(
            main_screen, RED, posCenter, self.radius, self.width
        )

    def _collide_and_die(self, target, listCannonBalls):
        if self.timer <= 0:
            listCannonBalls.remove(self)

        elif self.rect.colliderect(target.rect):
            listCannonBalls.remove(self)
            target.life -= 1

    def _movement(self, topLeft):
        self.rect.move_ip(topLeft)
        self.timer -= 0.1
        pg.draw.circle(
            main_screen, RED, self.rect.topleft, self.radius, self.width
        )

    def update(self, **kwargs):
        self._movement(kwargs['topLeft'])
        self._collide_and_die(
            kwargs['target'],
            kwargs['listCannonBalls'],
        )


class Cannon:
    def __init__(self):
        self.max_cannonballs = 20
        self.l_targets = []
        self.l_cannonballs = []

    def load_target(self, enemy):
        if enemy and enemy.alive() and enemy not in self.l_targets:
            self.l_targets.append(enemy)

    def remove_target(self):
        [self.l_targets.remove(e) for e in self.l_targets if not e.alive()]

    def _mark_target(self, target):
        pg.draw.circle(main_screen, RED, target.rect.center, 17, 1)

    def _load_cannon(self, centerPlayer):
        if self.l_targets and len(self.l_cannonballs) < self.max_cannonballs:
            self.l_cannonballs.append(CannonBall(centerPlayer))

    def _shoot_cannonball(self, speed, centerPlayer, centerEnemy) -> tuple:
        e_x, e_y = centerEnemy
        p_x, p_y = centerPlayer
        pos_X = get_direction(speed, p_x, e_x)
        pos_Y = get_direction(speed, p_y, e_y)
        return pos_X, pos_Y

    def _show_damage(self, damage, target):
        main_screen.blit(font.render(f'{damage}', True, YELLOW), target)

    def _show_cannon_target(self, startCenter, endCenter, width: int = 2):
        return pg.draw.aaline(main_screen, WHITE, startCenter, endCenter, width)

    def draw(self, speed, centerPlayer):
        if self.l_targets:
            target = self.l_targets[0]
            self._mark_target(target)
            c = self._show_cannon_target(centerPlayer, target.rect.center)
            self._show_damage(c.center, c.center)
            self._load_cannon(centerPlayer)

            for temp, ball in enumerate(self.l_cannonballs):
                if temp % 2 == 0:
                    ball.update(
                        listCannonBalls=self.l_cannonballs,
                        target=target,
                        topLeft=self._shoot_cannonball(
                            speed,
                            centerPlayer,
                            target.rect.center,
                        ),
                    )
