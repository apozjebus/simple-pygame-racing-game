import pygame

class Events():
    def __init__(self):
        self.HOME = pygame.USEREVENT + 1
        self.MUSICSWITCH = pygame.USEREVENT + 2
        self.MUSICCHANGE = pygame.USEREVENT + 3
        self.FPSCHANGE = pygame.USEREVENT + 4
        self.POWER = pygame.USEREVENT + 5
        self.CHANGELEVEL = pygame.USEREVENT + 6
        self.WIN = pygame.USEREVENT + 7
        self.DEAD = pygame.USEREVENT + 8
        self.BOTWON = pygame.USEREVENT + 9