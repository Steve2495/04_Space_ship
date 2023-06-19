import pygame
from game.components.power_ups.power_up import PowerUp
from game.utils.constants import HEART, HEART_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH

class Heart(PowerUp):
    def __init__(self):
        super().__init__(HEART, HEART_TYPE)
        
