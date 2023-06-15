from game.components.enemies.enemy import Enemy
import random

class EnemyManager:
    
    def __init__(self):
        self.enemies = []
        
    def update(self, game, CURRENT_LEVEL):
        self.add_enemy(CURRENT_LEVEL)
        for enemy in self.enemies:
            enemy.update(self.enemies, game)
        
    def add_enemy(self, CURRENT_LEVEL):
        enemy_type = random.randint(1,3)
        if enemy_type == 1:
            enemy = Enemy()
        elif enemy_type == 2:
            x_speed = 5
            y_speed = 2
            move_x_for = [50,120]
            enemy = Enemy(enemy_type, x_speed, y_speed, move_x_for)
        else:
            x_speed = 4
            y_speed = 5
            move_x_for = [60,100]
            enemy = Enemy(enemy_type, x_speed, y_speed, move_x_for)
            
        if len(self.enemies) < CURRENT_LEVEL:
            self.enemies.append(enemy)
        
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)