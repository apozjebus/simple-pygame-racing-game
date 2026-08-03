import pygame
import os
from settings import Settings
from fonts import Fonts
from events import Events

# Menu Class

class Menu():
    def __init__(self):
        
        # Basic Declarations
        self.settings = Settings()
        self.width = self.settings.WIDTH // 1.3
        self.height = self.settings.HEIGHT // 1.3
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.set_colorkey((0, 0, 0))
        borders = pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'ui', 'menu', 'borders.png')).convert_alpha()
        self.surface.blit(borders, (0, 0))
        self.layout = {
            "levels": {
                "topleft": (11, 11),
                "layout": {
                    "map_1": {
                        "name": "Map 1",
                        "topleft": (67, 60),
                        "image": pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'ui', 'menu', 'map_1.png')).convert_alpha(),
                        "width": 350,
                        "height": 200,
                        "rect": pygame.rect.Rect(67, 60, 350, 200)
                    },
                    "map_2": {
                        "name": "Map 2",
                        "topleft": (67, 317),
                        "image": pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'ui', 'menu', 'map_2.png')).convert_alpha(),
                        "width": 350,
                        "height": 200,
                        "rect": pygame.rect.Rect(67, 317, 350, 200)
                    },
                    "map_3": {
                        "name": "Map 3",
                        "topleft": (67, 573),
                        "image": pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'ui', 'menu', 'map_3.png')).convert_alpha(),
                        "width": 350,
                        "height": 200,
                        "rect": pygame.rect.Rect(67, 573, 350, 200)
                    }
                }
            },
            "vehicles": {
                "topleft": (502, 11),
                "layout": {
                    "car_red": {
                        "topleft": (506, 15),
                        "image": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'player', 'car', 'red.png')).convert_alpha(), (50, 100)),
                        "width": 185,
                        "height": 188,
                        "rect": pygame.rect.Rect(506, 15, 185, 188)
                    },
                    "car_black": {
                        "topleft": (698, 15),
                        "image": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'player', 'car', 'black.png')).convert_alpha(), (50, 100)),
                        "width": 185,
                        "height": 188,
                        "rect": pygame.rect.Rect(698, 15, 185, 188)
                    },
                    "car_blue": {
                        "topleft": (890, 15),
                        "image": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'player', 'car', 'blue.png')).convert_alpha(), (50, 100)),
                        "width": 185,
                        "height": 188,
                        "rect": pygame.rect.Rect(890, 15, 185, 188)
                    },
                    "car_green": {
                        "topleft": (1082, 15),
                        "image": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'player', 'car', 'green.png')).convert_alpha(), (50, 100)),
                        "width": 185,
                        "height": 188,
                        "rect": pygame.rect.Rect(1082, 15, 185, 188)
                    },
                    "car_yellow": {
                        "topleft": (1274, 15),
                        "image": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'player', 'car', 'yellow.png')).convert_alpha(), (50, 100)),
                        "width": 185,
                        "height": 188,
                        "rect": pygame.rect.Rect(1274, 15, 185, 188)
                    },
                    "motorcycle_red": {
                        "topleft": (506, 207),
                        "image": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'player', 'motorcycle', 'red.png')).convert_alpha(), (44, 100)),
                        "width": 185,
                        "height": 188,
                        "rect": pygame.rect.Rect(506, 207, 185, 188)
                    },
                    "motorcycle_black": {
                        "topleft": (698, 207),
                        "image": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'player', 'motorcycle', 'black.png')).convert_alpha(), (44, 100)),
                        "width": 185,
                        "height": 188,
                        "rect": pygame.rect.Rect(698, 207, 185, 188)
                    },
                    "motorcycle_blue": {
                        "topleft": (890, 207),
                        "image": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'player', 'motorcycle', 'blue.png')).convert_alpha(), (44, 100)),
                        "width": 185,
                        "height": 188,
                        "rect": pygame.rect.Rect(890, 207, 185, 188)
                    },
                    "motorcycle_green": {
                        "topleft": (1082, 207),
                        "image": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'player', 'motorcycle', 'green.png')).convert_alpha(), (44, 100)),
                        "width": 185,
                        "height": 188,
                        "rect": pygame.rect.Rect(1082, 207, 185, 188)
                    },
                    "motorcycle_yellow": {
                        "topleft": (1274, 207),
                        "image": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'player', 'motorcycle', 'yellow.png')).convert_alpha(), (44, 100)),
                        "width": 185,
                        "height": 188,
                        "rect": pygame.rect.Rect(1274, 207, 185, 188)
                    }
                }
            },
            "settings": {
                "topleft": (503, 431),
                "layout": {
                    "home": {
                        "topleft": (587, 483),
                        "image": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'ui', 'menu', 'settings', 'home.png')).convert_alpha(), (100, 100)),
                        "width": 128, 
                        "height": 128,
                        "type": "home",
                        "rect": pygame.rect.Rect(587, 483, 128, 128)
                    },
                    "music_on": {
                        "topleft": (745, 483),
                        "image": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'ui', 'menu', 'settings', 'music_on.png')).convert_alpha(), (100, 100)),
                        "width": 128, 
                        "height": 128,
                        "type": "music_switch",
                        "state": True,
                        "rect": pygame.rect.Rect(745, 483, 128, 128)
                    },
                    "music_off": {
                        "topleft": (903, 483),
                        "image": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'ui', 'menu', 'settings', 'music_off.png')).convert_alpha(), (100, 100)),
                        "width": 128, 
                        "height": 128,
                        "type": "music_switch",
                        "state": False,
                        "rect": pygame.rect.Rect(903, 483, 128, 128)
                    },
                    "music_lower": {
                        "topleft": (1061, 483),
                        "image": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'ui', 'menu', 'settings', 'music_lower.png')).convert_alpha(), (100, 100)),
                        "width": 128, 
                        "height": 128,
                        "type": "music_change",
                        "state": False,
                        "rect": pygame.rect.Rect(1061, 483, 128, 128)
                    },
                    "music_higher": {
                        "topleft": (1219, 483),
                        "image": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'ui', 'menu', 'settings', 'music_higher.png')).convert_alpha(), (100, 100)),
                        "width": 128, 
                        "height": 128,
                        "type": "music_change",
                        "state": True,
                        "rect": pygame.rect.Rect(1219, 483, 128, 128)
                    },
                    "fps_30": {
                        "topleft": (674, 653),
                        "image": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'ui', 'menu', 'settings', 'fps_30.png')).convert_alpha(), (100, 100)),
                        "width": 128, 
                        "height": 128,
                        "type": "fps",
                        "state": 30,
                        "rect": pygame.rect.Rect(674, 653, 128, 128)
                    },
                    "fps_60": {
                        "topleft": (839, 653),
                        "image": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'ui', 'menu', 'settings', 'fps_60.png')).convert_alpha(), (100, 100)),
                        "width": 128, 
                        "height": 128,
                        "type": "fps",
                        "state": 60,
                        "rect": pygame.rect.Rect(839, 653, 128, 128)
                    },
                    "fps_120": {
                        "topleft": (1004, 653),
                        "image": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'ui', 'menu', 'settings', 'fps_120.png')).convert_alpha(), (100, 100)),
                        "width": 128, 
                        "height": 128,
                        "type": "fps",
                        "state": 120,
                        "rect": pygame.rect.Rect(1004, 653, 128, 128)
                    },
                    "power": {
                        "topleft": (1166, 653),
                        "image": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'ui', 'menu', 'settings', 'power.png')).convert_alpha(), (100, 100)),
                        "width": 128, 
                        "height": 128,
                        "type": 'power',
                        "rect": pygame.rect.Rect(1166, 653, 128, 128)
                    }
                }
            }
        }
        self.Events = Events()
        self.rect = self.surface.get_rect(center = (self.settings.WIDTH // 2, self.settings.HEIGHT // 2))
        self.rect.center = (self.settings.WIDTH // 2, self.settings.HEIGHT // 2)
        self.WINDOW = pygame.display.get_surface()
        self.generate_menu()
    
    def generate_menu(self):
        
        # Draw Level Images
        for key, map in self.layout["levels"]["layout"].items():
            # Blit Image
            self.surface.blit(map["image"], map["topleft"])
            # Draw Border Around
            border = pygame.rect.Rect(map["topleft"][0] - 2, map["topleft"][1] - 2, map["width"] + 2, map["height"] + 2)
            pygame.draw.rect(self.surface, (255, 255, 255), border, 2)
            # Blit Text And Box Behind Text
            map_label = Fonts["menu_map_label"].render(map["name"], 1, (255, 255, 255))
            map_label_rect = map_label.get_rect(center = (map["topleft"][0] + map["width"] // 2, map["topleft"][1] + map["height"] // 2))
            map_label_bg_rect = pygame.rect.Rect(0, 0, map_label_rect.width + 40, map_label_rect.height + 20)
            map_label_bg_rect.center = map_label_rect.center
            pygame.draw.rect(self.surface, (99, 99, 99), map_label_bg_rect, 0, 10)
            self.surface.blit(map_label, map_label_rect.topleft)

        # Draw Car And Motorcycle Images
        for key, vehicle in self.layout["vehicles"]["layout"].items():
            # Blit Image And Background
            image_rect = vehicle["image"].get_rect(center = (vehicle["topleft"][0] + vehicle["width"] // 2, vehicle["topleft"][1] + vehicle["height"] // 2))
            bg_rect = image_rect.inflate(60, 30)
            bg_rect.center = image_rect.center
            pygame.draw.rect(self.surface, (99, 99, 99), bg_rect, 0 , 20)
            self.surface.blit(vehicle["image"], image_rect.topleft)
        
        # Draw Settings Icons
        for key, setting in self.layout["settings"]["layout"].items():
            # Blit Image And Background
            image_rect = setting["image"].get_rect(center = (setting["topleft"][0] + setting["width"] // 2, setting["topleft"][1] + setting["height"] // 2))
            bg_rect = image_rect.inflate(40, 40)
            bg_rect.center = image_rect.center
            pygame.draw.rect(self.surface, (99, 99, 99), bg_rect, 0, 20)
            self.surface.blit(setting["image"], image_rect.topleft)
        
    def handle_mouse(self, pos):
        
        # Check If Anything In Levels Has Been Clicked On
        for key, level in self.layout["levels"]["layout"].items():
            if level["rect"].collidepoint(pos):
                event = pygame.event.Event(self.Events.CHANGELEVEL, value = level["name"].split()[1])
                pygame.event.post(event)
                        
        # Check If Anything In Settings Has Been Clicked On
        for key, setting in self.layout["settings"]["layout"].items():
            if setting["rect"].collidepoint(pos):
                match setting["type"]:
                    case 'home':
                        event = pygame.event.Event(self.Events.HOME, value = True) 
                        pygame.event.post(event)
                    case 'music_switch':
                        event = pygame.event.Event(self.Events.MUSICSWITCH, value = True) if setting["state"] == True else pygame.event.Event(self.Events.MUSICSWITCH, value = False)
                        pygame.event.post(event)
                    case 'music_change':
                        event = event = pygame.event.Event(self.Events.MUSICCHANGE, value = True) if setting["state"] == True else pygame.event.Event(self.Events.MUSICCHANGE, value = False)
                        pygame.event.post(event)
                    case 'fps':
                        event = pygame.event.Event(self.Events.FPSCHANGE, value = setting["state"])
                        pygame.event.post(event)
                    case 'power':
                        event = pygame.event.Event(self.Events.POWER, value = True)
                        pygame.event.post(event)

    def draw(self):
        
        self.WINDOW.blit(self.surface, self.rect.topleft)