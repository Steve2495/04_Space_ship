import pygame
import random

from game.components.power_ups.shield import Shield
from game.components.power_ups.heart import Heart
from game.utils.constants import SPACESHIP_SHIELD, SHIELD_TYPE, HEART_TYPE , SPACESHIP, DEFAULT_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(5000, 10000)
        self.duration = random.randint(3,5)
        self.current_time = pygame.time.get_ticks()
        
    def generate_power_up(self):
        power_up = [Shield(), Heart()]
        self.random_power_up = random.randint(0,1)
        self.when_appears += random.randint(5000, 10000)
        self.power_ups.append(power_up[self.random_power_up])
        
    def update(self, game):
        self.current_time = pygame.time.get_ticks()
        if len(self.power_ups) == 0 and self.current_time >= self.when_appears:
            self.generate_power_up()
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up) and isinstance(power_up, Shield):
                power_up.start_time = pygame.time.get_ticks()
                game.player.power_up_type = SHIELD_TYPE
                game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                game.player.has_power_up = True
                # print(game.player.power_time_up)
                game.player.set_image((65, 75), SPACESHIP_SHIELD)
                self.power_ups.remove(power_up)

            if game.player.rect.colliderect(power_up) and isinstance(power_up, Heart):
                game.draw_heart(margin=(SCREEN_WIDTH - 45, SCREEN_HEIGHT - 80))
                game.player.hearts += 1
                self.power_ups.remove(power_up)

                
        if game.player.power_time_up != 0 and pygame.time.get_ticks() >= game.player.power_time_up:
            game.player.set_image((40,60), SPACESHIP)
            game.player.power_up_type = DEFAULT_TYPE
            game.player.power_time_up = 0
                
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
            
    def reset(self):
        self.current_time = pygame.time.get_ticks()
        self.power_ups = []
        self.when_appears = random.randint(5000,10000)
        self.duration = random.randint(5,8)
        