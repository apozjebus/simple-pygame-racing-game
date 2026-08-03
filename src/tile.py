import pygame
from settings import *

# Tile Class
class Tile(pygame.sprite.Sprite):
    def __init__(self, groups, pos, type = 'default', image = pygame.Surface((128, 128))):
        
        # Basic Declarations
        super().__init__(groups)
        self.type = type
        self.image = image
        self.rect = self.image.get_rect(topleft = pos)
        self.mask = pygame.mask.from_surface(self.image)



            