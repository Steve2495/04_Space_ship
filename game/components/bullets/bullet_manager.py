import pygame
from pygame.locals import *

from game.components.bullets.bullet import Bullet, BULLET_ENEMY

class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
        
    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            
            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                self.enemy_bullets.remove(bullet)
                game.playing = False
                pygame.time.delay(1000)
                break
            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'ally':
                self.bullets.remove(bullet)
                game.playing = False
                pygame.time.delay(1000)
                break
            
    def draw(self, screen, bullet_scale):
        for bullet in self.enemy_bullets:
            bullet_scale = pygame.transform.scale(BULLET_ENEMY, (10, 10))
            bullet.draw(screen, bullet_scale)
            
    def add_bullet(self, bullet):
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)
    
    