from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1, ENEMY_2, ENEMY_3

class EnemyManager:
    def __init__(self):
        self.enemies = []
        
    def update(self):
        self.add_enemy(ENEMY_1)
        self.add_enemy(ENEMY_2)
        self.add_enemy(ENEMY_3)
        for enemy in self.enemies:
            enemy.update(self.enemies)
        
    def add_enemy(self, Enem):
        if len(self.enemies)<10:
            enemy = Enemy(Enem)
            self.enemies.append(enemy)
        
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)