from ..enemy.entity import Enemy


def generate_enemies_by_stage(group, listEnemies):
    if len(group.sprites()) <= 20:
        listEnemies.append(Enemy(group))

    for enemy in listEnemies:
        if not enemy.alive():
            group.remove(enemy)
            listEnemies.remove(enemy)
