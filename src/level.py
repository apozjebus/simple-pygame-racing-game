import pygame
import os
from support import *
from fonts import Fonts
from settings import Settings
from .player import Player
from .tile import Tile
from .menu import Menu
from .enemy import Enemy

# Level Class

class Level:
    def __init__(self):
        
        # Basic Declarations
        self.settings = Settings()
        self.obstacle_sprites = pygame.sprite.Group()
        self.WINDOW = pygame.display.get_surface()
        self.levels = {
            "1": {
                "name": "map_1",
                "csv_data": get_csv_data(os.path.join(self.settings.ASSETS_DIR, 'csv', 'map_1', 'map_1_Border.csv')),
                "image_path": os.path.join(self.settings.ASSETS_DIR, 'imgs', 'map_floors', 'map_1.png'),
                "player_spawn": (3000, 9750),
                "finish_line_rect": pygame.rect.Rect(14000, 3200, 128, 384),
                "record": None,
                "enemies": [],
                "enemies_spawn": (3300, 9776),
                "enemies_path": [(5008, 9744), (5056, 8896), (5792, 8848), (5856, 6160), (6064, 5568), (8368, 5568), (8400, 9888), (8784, 9936), (8768, 10544), (10528, 10528), (10576, 9520), (11440, 9504), (11456, 3648), (11872, 3344), (15792, 3376)]
            },
            "2": {
                "name": "map_2",
                "csv_data": get_csv_data(os.path.join(self.settings.ASSETS_DIR, 'csv', 'map_2', 'map_2_Border.csv')),
                "image_path": os.path.join(self.settings.ASSETS_DIR, 'imgs', 'map_floors', 'map_2.png'),
                "player_spawn": (2304, 9856),
                "finish_line_rect": pygame.rect.Rect(16640, 8866, 640, 128),
                "record": None,
                "enemies": [],
                "enemies_spawn": (2550, 9904),
                "enemies_path": [(2752, 9872), (2752,6688), (3840, 6672), (3872, 3760), (2752, 3760), (2768, 2112), (3248, 2080), (3280, 1712), (5040, 1728), (5072, 10016), (7712, 10016), (7712, 8528), (6480, 8480), (6480, 1600), (7984, 1632), (8032, 2864), (8880, 2896), (8864, 5264), (7648, 5312), (7664, 6800), (8992, 6864), (9056, 9120), (10288, 9152), (10304, 10112), (11440, 10128), (11408, 4448), (9936, 4368), (9936, 1344), (12192, 1360), (12224, 2720), (13088, 2784), (13104, 6448), (12736, 6448), (12752, 8480), (13344, 8528), (13392, 10128), (14640, 10128), (14640, 6848), (14272, 6816), (14272, 3664), (15104, 3600), (15168, 1488), (16960, 1488), (16960, 11008)]
            },
            "3": {
                "name": "map_3",
                "csv_data": get_csv_data(os.path.join(self.settings.ASSETS_DIR, 'csv', 'map_3', 'map_3_Border.csv')),
                "image_path": os.path.join(self.settings.ASSETS_DIR, 'imgs', 'map_floors', 'map_3.png'),
                "player_spawn": (1664, 10624),
                "finish_line_rect": pygame.rect.Rect(16808, 6912, 128, 384),
                "record": None,
                "enemies": [],
                "enemies_spawn": (1872, 10688),
                "enemies_path": [(4864, 10656), (4896, 6608), (3664, 6560), (3648, 2896), (6816, 2832), (6832, 1552), (8608, 1568), (8672, 5280), (10016, 5344), (10080, 9248), (12048, 9232), (12112, 6096), (13952, 6096), (14032, 7952), (15776, 7952), (15824, 7104), (17568, 7104)]
            },
        }
        self.current_level = self.levels["1"]
        self.visible_sprites = YSortCameraClass(self.current_level)
        self.player = Player([self.visible_sprites], self.obstacle_sprites, self.current_level["player_spawn"], self.set_menu_play, self.current_level["finish_line_rect"])
        self.menu = Menu()
        self.in_menu = False # True If In Menu
        self.play = False # True If Player Has Started Playing
        self.time_taken = 0
        self.generate_map()
        self.won = False
        self.last_won = None
        self.won_cd = 3000
        self.enemy_count = 1
        self.state = ''

    def run(self):
        
        if self.won:
            if self.state == 'won':            
                if self.current_level["record"] == None:
                    record_message = 'New Record: '
                    self.current_level["record"] = self.time_taken
                else:
                    if self.time_taken <= self.current_level["record"]:
                        record_message = 'New Record: '
                        self.current_level["record"] = self.time_taken
                    else:
                        record_message = ''
                        
                won_message = Fonts["won_time_message"].render(record_message + '{:.2f}'.format(self.time_taken / 1000) + 's', 1, (255, 255, 255))
                won_message_rect = won_message.get_rect(center = (self.settings.WIDTH // 2, self.settings.HEIGHT // 2))
                bg_rect = won_message_rect.inflate(60, 40)
                bg_rect.center = won_message_rect.center
                self.visible_sprites.draw(self.WINDOW, self.player)
                self.draw_ui()
                pygame.draw.rect(self.WINDOW, (90, 90, 90), bg_rect, 0, 10)
                self.WINDOW.blit(won_message, won_message_rect.topleft)
                
            elif self.state == 'dead':
                for enemy in self.current_level["enemies"]:
                    enemy.image = pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'player', 'car', 'explosion.png')), (400, 400))
                    
                won_message = Fonts["won_time_message"].render('You Died', 1, (255, 255, 255))
                won_message_rect = won_message.get_rect(center = (self.settings.WIDTH // 2, self.settings.HEIGHT // 2))
                bg_rect = won_message_rect.inflate(60, 40)
                bg_rect.center = won_message_rect.center
                self.visible_sprites.draw(self.WINDOW, self.player)
                self.draw_ui()
                pygame.draw.rect(self.WINDOW, (90, 90, 90), bg_rect, 0, 10)
                self.WINDOW.blit(won_message, won_message_rect.topleft)
                self.delete_enemies()
            
            elif self.state == 'bot_won':
                won_message = Fonts["won_time_message"].render('Bot Won', 1, (255, 255, 255))
                won_message_rect = won_message.get_rect(center = (self.settings.WIDTH // 2, self.settings.HEIGHT // 2))
                bg_rect = won_message_rect.inflate(60, 40)
                bg_rect.center = won_message_rect.center
                self.visible_sprites.draw(self.WINDOW, self.player)
                self.draw_ui()
                pygame.draw.rect(self.WINDOW, (90, 90, 90), bg_rect, 0, 10)
                self.WINDOW.blit(won_message, won_message_rect.topleft)
                
            now = pygame.time.get_ticks()
            if now - self.last_won > self.won_cd:
                self.won = False
                self.set_level(-1)
        else:
            if(self.in_menu):
                self.last_time_taken = pygame.time.get_ticks()
                self.draw_menu()
            elif(self.play):
                # Update Sprites And Time Passed
                self.visible_sprites.update()
                now = pygame.time.get_ticks()
                self.time_taken += now - self.last_time_taken
                self.last_time_taken = now
                self.visible_sprites.draw(self.WINDOW, self.player)
                self.draw_ui()
            else:
                self.visible_sprites.draw(self.WINDOW, self.player)
                self.draw_ui()
        
    def draw_ui(self):
        
        # Load Images
        ui_rect = pygame.rect.Rect(self.settings.WIDTH - 300, -10, 400, 200)
        pygame.draw.rect(self.WINDOW, (50, 50, 50), ui_rect, 0, 10)
        menu_icon = pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'ui', 'menu_icon_open.png')), (100, 100))
        self.menu_icon_rect = menu_icon.get_rect(topleft = (0, 0))
        speed_label = Fonts["speed_label"].render(str(abs(round(self.player.speed))) + 'km/h', 1, (255, 255, 255))
        speed_label_rect = speed_label.get_rect(topright = (self.settings.WIDTH - 10, 10))
        time_taken_label = Fonts["time_taken_label"].render('{:.2f}'.format(self.time_taken / 1000), 1, (255, 255, 255))
        time_taken_label_rect = time_taken_label.get_rect(topright = (self.settings.WIDTH - 10, 10 + speed_label.get_height() + 5))
        
        # Print Record Label If It Exists
        if self.current_level["record"] != None:
            record_label = Fonts["record_label"].render('Record: ' + '{:.2f}'.format(self.current_level["record"] / 1000) + 's', 1, (255, 255, 255))
            record_rect = record_label.get_rect(topright = (self.settings.WIDTH - 10, 20 + speed_label.get_height() + time_taken_label.get_height()))
            self.WINDOW.blit(record_label, record_rect.topleft)
        else:
            record_label = Fonts["record_label"].render('Record: None', 1, (255, 255, 255))
            record_rect = record_label.get_rect(topright = (self.settings.WIDTH - 10, 20 + speed_label.get_height() + time_taken_label.get_height()))
            self.WINDOW.blit(record_label, record_rect.topleft)
        
        # If Player Hasnt Started Map Yet, Render Start Sign
        if(not(self.play)):
            bg = pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'ui', 'dark_bg.png')), (self.settings.WIDTH, self.settings.HEIGHT))
            start_surface = pygame.surface.Surface((400, 100))
            start_surface.fill((50, 50, 50))
            self.start_rect = start_surface.get_rect(center = (self.settings.WIDTH // 2, self.settings.HEIGHT // 2))
            start_label = Fonts["start_label"].render('Start', 1, (255, 255, 255))
            start_label_rect = start_label.get_rect(center = (self.start_rect.width // 2, self.start_rect.height // 2))
            start_surface.blit(start_label, start_label_rect.topleft)
            
        # Draw 
        self.WINDOW.blit(menu_icon, self.menu_icon_rect.topleft)
        self.WINDOW.blit(speed_label, speed_label_rect.topleft)
        self.WINDOW.blit(time_taken_label, time_taken_label_rect.topleft)
        
        if(not(self.play)):
            self.WINDOW.blit(bg, (0, 0))
            self.WINDOW.blit(start_surface, self.start_rect.topleft)
        
    def draw_menu(self):
        
        # Load Images
        menu_icon = pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'ui', 'menu_icon_close.png')), (100, 100))
        self.menu_icon_rect = menu_icon.get_rect(topleft = (0, 0))
        
        # Draw 
        self.WINDOW.fill((30, 30, 30))
        self.WINDOW.blit(menu_icon, self.menu_icon_rect.topleft)
        self.menu.draw()
        
    def generate_map(self):
        
        for row_index, row in enumerate(self.current_level["csv_data"]):
            for cell_index, cell in enumerate(row):
                if cell != '-1':
                    Tile([self.obstacle_sprites], (cell_index * self.settings.TILESIZE, row_index * self.settings.TILESIZE))
    
    def handle_mouse(self, pos):
        
        # Check If Level Started
        if(self.play):
            # Check If In Menu
            if(self.in_menu):
                # Check If Clicking Menu Open 
                if(self.menu_icon_rect.collidepoint(pos)):
                    self.in_menu = not(self.in_menu)
                # Need To Get Offset X And Y Because Images Are Blit Based On The Menu Surface
                menu_offset_x = pos[0] - (self.settings.WIDTH - self.menu.rect.width) // 2
                menu_offset_y = pos[1] - (self.settings.HEIGHT - self.menu.rect.height) // 2
                self.player.check_vehicle_change((menu_offset_x, menu_offset_y), self.menu.layout["vehicles"]["layout"])
                self.menu.handle_mouse((menu_offset_x, menu_offset_y))
            else:
                if(self.menu_icon_rect.collidepoint(pos)):
                    self.in_menu = not(self.in_menu)
        else:
            # Had Errors Here Sometimes When Launching So Added A Try Except
            try:
                if self.start_rect.collidepoint(pos):
                    self.player.enemies = []
                    self.play = True
                    self.last_time_taken = pygame.time.get_ticks()
                    for i in range(self.enemy_count):
                        enemy = Enemy([self.visible_sprites], self.current_level["enemies_spawn"], self.current_level["finish_line_rect"], self.current_level["enemies_path"])
                        self.current_level["enemies"].append(enemy)
                        self.player.enemies.append(enemy)
            except:
                pass
    
    def set_menu_play(self, menu = None, play = None):
        
        self.in_menu = menu if menu != None else self.in_menu
        if(play == False):
            self.play = False
            self.time_taken = 0
    
    def delete_enemies(self):
        
        self.current_level["enemies"] = []
    
    def set_level(self, level):
        
        self.won = False
        self.current_level = self.levels[level] if level != -1 else self.current_level
        self.visible_sprites = YSortCameraClass(self.current_level)
        self.player.spawn_pos = self.current_level["player_spawn"]
        self.player.finish_line_rect = self.current_level["finish_line_rect"]
        self.in_menu = False 
        self.play = False 
        self.obstacle_sprites = pygame.sprite.Group()
        self.generate_map()
        self.player.obstacles = self.obstacle_sprites
        self.player.reset_variables()
        self.visible_sprites.add(self.player)
        self.time_taken = 0
        self.last_time_taken = pygame.time.get_ticks()

# Camera Class Sorted By Y Positions
class YSortCameraClass(pygame.sprite.Group):
    def __init__(self, level):

        # Basic Declarations
        super().__init__()
        self.current_level = level
        self.settings = Settings()
        self.half_width = self.settings.WIDTH // 2
        self.half_height = self.settings.HEIGHT // 2
        self.offset = pygame.math.Vector2()

        # Map Background
        self.map_bg = pygame.image.load(self.current_level["image_path"]).convert_alpha()
        self.map_rect = self.map_bg.get_rect(topleft=(0, 0))

    # Custom Draw Func For Sprites
    def draw(self, surface, player):

        # Get Offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # Blit Background With Offset
        surface.blit(self.map_bg, self.map_rect.topleft - self.offset)

        # Blit The Sprites With The Offset
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.bottom):
            surface.blit(sprite.image, sprite.rect.topleft - self.offset)

