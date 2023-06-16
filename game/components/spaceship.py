import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH

from game.components.bullets.bullet import Bullet

class Spaceship(Sprite):
    scale = [40, 60]
    X_POS = ( SCREEN_WIDTH // 2) - 40
    Y_POS = SCREEN_HEIGHT - scale[1]
    
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.scale[0], self.scale[1]))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'
        
        self.shooting_time = random.randint(30,50)
        
    def move_left(self):
        if self.rect.left == 0:
            self.rect.x = SCREEN_WIDTH - (self.scale[0] - 10)
        
        if self.rect.left > 0:
            self.rect.x = self.rect.x - 10
    
    def move_right(self):
        if self.rect.right == SCREEN_WIDTH:
            self.rect.x = -10
            
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x = self.rect.x + 10
    
    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y = self.rect.y -10        
    
    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - self.scale[1]:
            self.rect.y = self.rect.y + 10

    def shoot(self, bullet_manager):
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)

    
    def update(self, user_input, game):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        if user_input[pygame.K_RIGHT]:
            self.move_right()
        if user_input[pygame.K_UP]:
            self.move_up()
        if user_input[pygame.K_DOWN]:
            self.move_down()
        if user_input[pygame.K_SPACE]:
            self.shoot(game.bullet_manager)
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
    def repaint(self, screen):
        screen.blit(self.image_2, (self.rect.x, self.rect.y))
        
    