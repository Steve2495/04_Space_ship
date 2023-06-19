import pygame 
from game.utils.constants import SHIELD_TYPE, SPACESHIP
from game.components.power_ups.power_up_manager import PowerUpManager

class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
        self.power_up_manager = PowerUpManager()
        
    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            
            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                self.enemy_bullets = []
                print(game.player.hearts)
                if game.player.power_up_type == SHIELD_TYPE:
                    bullets_copy = list(self.bullets)  # Crear una copia de la lista de balas
                    for bullet in bullets_copy:
                        self.power_up_manager.reset()
                        self.bullets.remove(bullet)
                        if game.player.power_time_up == 0:
                            game.player.set_image((40,60), SPACESHIP)
                
                if game.player.power_up_type != SHIELD_TYPE:
                    game.player.hearts -= 1
                    if game.player.hearts == 0:
                        game.player.hearts = 1
                        game.playing = False
                        print("GAME OVER")
                        pygame.time.delay(1000)
                        game.death_count += 1

                break
            
        for bullet in self.bullets:
            bullet.update(self.bullets)
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                    self.bullets.remove(bullet)
                    game.enemy_manager.enemies.remove(enemy)
                    game.update_score()
                    break
        
    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
            
        for bullet in self.bullets:
            bullet.draw(screen)
            
    def add_bullet(self, bullet, game):
        if bullet.owner == 'enemy': # and len(self.enemy_bullets) < game.ENEMIES_PER_LEVEL // 2:
            for enemy in game.enemy_manager.enemies:
                if enemy.num_shoots == 1:
                    self.enemy_bullets.append(bullet)
                    if game.player.power_up_type == SHIELD_TYPE:
                        for bullet in self.bullets:
                            self.bullets.remove(bullet)
        if bullet.owner == 'player':
            self.bullets.append(bullet)
    
    