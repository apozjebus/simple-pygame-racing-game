import pygame
import os
from settings import Settings
from fonts import Fonts
from events import Events

# Home Page Class

class Home():
    def __init__(self, set_in_home):
        
        # Basic Declarations
        self.settings = Settings()
        self.WINDOW = pygame.display.get_surface()
        self.Events = Events()
        self.background_color = 1
        self.text_color = 254
        self.background_direction = False
        self.text_direction = False
        self.started = False
        self.set_in_home = set_in_home
        self.level_images = {
            "1": {
                "image": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'ui', 'menu', 'map_1.png')).convert_alpha(), (525, 300)),
                "name": "Map 1",
                "topleft": (0, 390),
                "width": 525,
                "height": 300,
                "rect": pygame.rect.Rect(0, 390, 525, 300)
            },
            "2": {
                "image": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'ui', 'menu', 'map_2.png')).convert_alpha(), (525, 300)),
                "name": "Map 2",
                "topleft": (850, 390),
                "width": 525,
                "height": 300,
                "rect": pygame.rect.Rect(850, 390, 525, 300)
            },
            "3": {
                "image": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'ui', 'menu', 'map_3.png')).convert_alpha(), (525, 300)),
                "name": "Map 3",
                "topleft": (self.settings.WIDTH - 262, 390),
                "width": 525,
                "height": 300,
                "rect": pygame.rect.Rect(self.settings.WIDTH - 262, 390, 525, 300)
            },
        }
    
    def draw(self):
        self.background_color = self.background_color + 1 if self.background_direction else self.background_color - 1
        if self.background_color >= 255 or self.background_color <= 0:
            self.background_direction = not(self.background_direction)
        self.text_color = self.text_color + 1 if self.text_direction else self.text_color - 1
        if self.text_color <= 0 or self.text_color >= 255:
            self.text_direction = not(self.text_direction)
        
        if(not(self.started)):
            self.WINDOW.fill((self.background_color, self.background_color, self.background_color))
            start_label = Fonts["home_page_start_label"].render('Start', 1, (self.text_color, self.text_color, self.text_color))
            self.start_label_rect = start_label.get_rect(center = (self.settings.WIDTH // 2, self.settings.HEIGHT // 2))
            self.WINDOW.blit(start_label, self.start_label_rect.topleft)
            
        else:
            self.WINDOW.fill((self.background_color, self.background_color, self.background_color))
            # Blit Levels Label At The Top Of Screen
            levels_label = Fonts["home_page_maps_label"].render('Maps', 1, (self.text_color, self.text_color, self.text_color))
            levels_label_rect = levels_label.get_rect(midtop = (self.settings.WIDTH // 2, 10))
            self.WINDOW.blit(levels_label, levels_label_rect.topleft)
            
            for key, image in self.level_images.items():
                # Blit Image And Border
                self.WINDOW.blit(image["image"], image["rect"].topleft)
                border = image["rect"].inflate(2, 2)
                pygame.draw.rect(self.WINDOW, (255, 255, 255), border, 2)
                
                # Blit Individual Level Label
                level_label = Fonts["home_page_map_label"].render(image["name"], 1, (self.text_color, self.text_color, self.text_color))
                temp_rect = level_label.get_rect(center = (image["rect"].x + image["width"] // 2, image["rect"].y + image["height"] // 2))
                level_label_rect = level_label.get_rect().inflate(60, 40)
                level_label_rect.center = (image["rect"].x + image["width"] // 2, image["rect"].y + image["height"] // 2)
                pygame.draw.rect(self.WINDOW, (self.background_color, self.background_color, self.background_color), level_label_rect, 0, 20)
                self.WINDOW.blit(level_label, temp_rect.topleft)
                image["rect"].x += 5
                if image["rect"].left > self.settings.WIDTH:
                    image["rect"].right = 0
                
    def handle_mouse(self, pos):
        
        # Sometimes Get An Error Here, Try Except Fixes It
        try:
            if(not(self.started)):
                if self.start_label_rect.collidepoint(pos):
                    self.started = True
            else:
                for key, target in self.level_images.items():
                    if target["rect"].collidepoint(pos):
                        event = pygame.event.Event(self.Events.CHANGELEVEL, value = target["name"].split()[1])
                        pygame.event.post(event)
        except:
            pass
                