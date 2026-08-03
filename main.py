import pygame
import os
from settings import Settings
from events import Events
from src.level import Level
from src.home import Home
pygame.mixer.init()

# Game Class
class Game:
    def __init__(self):
        
        # Basic Declarations
        self.settings = Settings()
        self.running = True
        self.FPS = self.settings.FPS
        self.WINDOW = pygame.display.set_mode((self.settings.WIDTH, self.settings.HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.home = Home(self.set_in_home)
        self.Events = Events()
        self.music_volume = 0.3
        self.in_home = True # True If In Home Page
        pygame.mixer.music.load(os.path.join(self.settings.ASSETS_DIR, 'sounds', 'bg_music.wav'))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(self.music_volume)
    
    # Main Game Loop
    def run(self):  
        while self.running:
            if not(self.in_home):
                # Events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        self.level.handle_mouse(pos)
                    if event.type == pygame.KEYDOWN:
                        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                            self.level.in_menu = not(self.level.in_menu)
                    # Custom Events
                    if event.type == self.Events.MUSICSWITCH:
                        if event.value == False:
                            pygame.mixer.music.pause()
                        else:   
                            pygame.mixer.music.play(-1)
                    if event.type == self.Events.MUSICCHANGE:
                        if event.value == False:
                            self.music_volume = self.music_volume - 0.1 if self.music_volume > 0 else 0
                        else:
                            self.music_volume = self.music_volume + 0.1 if self.music_volume < 1 else 1
                        pygame.mixer.music.set_volume(self.music_volume)
                    if event.type == self.Events.FPSCHANGE:
                        self.settings.set_FPS(event.value)
                        self.FPS = self.settings.FPS
                    if event.type == self.Events.POWER:
                        if event.value == True:
                            self.running = False
                    if event.type == self.Events.HOME:
                        self.in_home = True
                        self.home = Home(self.set_in_home)
                    if event.type == self.Events.CHANGELEVEL:
                        self.level.set_level(event.value)
                    if event.type == self.Events.WIN:
                        self.level.delete_enemies()
                        self.level.won = True
                        self.level.state = 'won'
                        self.level.last_won = pygame.time.get_ticks()
                    if event.type == self.Events.DEAD:
                        self.level.delete_enemies()
                        self.level.won = True
                        self.level.state = 'dead'
                        self.level.last_won = pygame.time.get_ticks()
                    if event.type == self.Events.BOTWON:
                        self.level.won = True
                        self.level.state = 'bot_won'
                        self.level.last_won = pygame.time.get_ticks()
                
                self.WINDOW.fill((0, 0, 255))
                        
                # Level Call
                self.level.run()
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.home.handle_mouse(pygame.mouse.get_pos())
                    if event.type == self.Events.CHANGELEVEL:
                        self.level.set_level(event.value)
                        self.in_home = False
                    
                self.home.draw()
                    
            pygame.display.update()
            self.clock.tick(self.FPS)
        
    def set_in_home(self, value):
        self.in_home = value

# Game Call
if __name__ == "__main__":
    game = Game()
    game.run()
        