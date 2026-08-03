from tokenize import Triple
import pygame
import os
from settings import Settings
from events import Events

# Player Class

class Player(pygame.sprite.Sprite):   
    def __init__(self, groups, obstacles, pos, set_menu_play, finish_line_rect):
        
        # Basic Declarations
        super().__init__(groups)
        self.settings = Settings()
        self.events = Events()
        self.images = {
            "car": {
                "red": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'player', 'car', 'red.png')).convert_alpha(), (62, 124)),
                "blue": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'player', 'car', 'blue.png')).convert_alpha(), (62, 124)),
                "black": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'player', 'car', 'black.png')).convert_alpha(), (62, 124)),
                "green": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'player', 'car', 'green.png')).convert_alpha(), (62, 124)),
                "yellow": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'player', 'car', 'yellow.png')).convert_alpha(), (62, 124))
            },
            "motorcycle": {
                "red": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'player', 'motorcycle', 'red.png')).convert_alpha(), (42, 100)),
                "blue": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'player', 'motorcycle', 'blue.png')).convert_alpha(), (42, 100)),
                "black": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'player', 'motorcycle', 'black.png')).convert_alpha(), (42, 100)),
                "green": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'player', 'motorcycle', 'green.png')).convert_alpha(), (42, 100)),
                "yellow": pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'player', 'motorcycle', 'yellow.png')).convert_alpha(), (42, 100))

            }
        }
        self.spawn_pos = pos
        self.image = self.images["car"]["red"]
        self.vehicle_type = 'car'
        self.rotated_images = []
        self.possible_rotations = 360
        self.set_rotated_images(self.image)
        self.rect = self.image.get_rect(topleft = (self.spawn_pos))
        self.direction = 0
        self.speed = 0
        self.turn_speed = 1.8
        self.acceleration_speed = 0.1
        self.deceleration_speed = 0.3 # Only For Auto Decleration
        self.reversing = False
        self.velocity = pygame.math.Vector2((0, 0))
        self.bouncing = False
        self.obstacles = obstacles
        self.set_menu_play = set_menu_play
        self.finish_line_rect = finish_line_rect
        self.won = False
        self.enemies = []
    
    def input(self):
        
        # Handle Inputs
        keys_pressed = pygame.key.get_pressed()
        
        # Check For Turning
        if(not(self.won)):
            if (keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]) and self.speed > 0.3:
                self.turn(max(-self.speed, -self.turn_speed))
            if (keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]) and self.speed > 0.3:
                self.turn(min(self.speed, self.turn_speed))
            if (keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]) and self.speed < -0.3:
                self.turn(min(-self.speed, self.turn_speed))
            if (keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]) and self.speed < -0.3:
                self.turn(max(self.speed, -self.turn_speed))
            
        # Check For Acceleration
        if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
            self.reversing = False
            self.accelerate()
        elif keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
            self.reversing = True if(not(self.won)) else self.reversing
            if(self.speed > 0):
                self.manual_brake()
            else:
                self.accelerate()
        else:
            # Car Will Slow Down If Not Accelerating
            self.auto_brake()
    
    # Make 360 Images For Rotations
    def set_rotated_images(self, image):
        
        self.rotated_images = []
        
        for i in range(self.possible_rotations):
            
            # Image Has To Be Offset By 90 Degrees For The Radians, Iunno What That Means
            rotated_image = pygame.transform.rotozoom(image, 360 - 90 - i, 1)
            self.rotated_images.append(rotated_image.convert_alpha())
        
        self.image = self.rotated_images[0]        
        self.mask = pygame.mask.from_surface(self.image)
        self.acceleration_speed = 0.1 if self.vehicle_type == 'car' else 0.15
    
    def accelerate(self):
        
        if(self.reversing):
            self.speed -= self.acceleration_speed
        else:
            self.speed += self.acceleration_speed
    
    def auto_brake(self):
        
        if(self.reversing):
            self.speed += self.deceleration_speed
        else:
            self.speed -= self.deceleration_speed
        
        if(self.speed <= 0):
            self.reversing = True
        else:
            self.reversing = False
    
    def manual_brake(self):
        
        self.speed /= 1.05
        if (abs(self.speed) < 0.2):
            self.speed = -0.1
     
    def turn(self, degrees):
        
        # Turn Player
        self.direction += degrees
        rect_center = self.rect.center
        if(self.image != self.rotated_images[int(self.direction) % 360]):
            self.image = self.rotated_images[int(self.direction) % 360]
            self.rect = self.image.get_rect(center = (rect_center))
    
    def collisions(self):

        # Check For Collisions
        if pygame.sprite.spritecollide(self, self.obstacles, False):
            if pygame.sprite.spritecollide(self, self.obstacles, False, pygame.sprite.collide_mask):
                if not(self.bouncing):
                    self.bounce()
                    self.bouncing = True
                    
        elif self.bouncing:
            self.bouncing = False
        
        # Check For Win
        if self.rect.colliderect(self.finish_line_rect):
            self.deceleration_speed = 1.8
            self.acceleration_speed = 0
            self.speed = 0
            event = pygame.event.Event(self.events.WIN)
            pygame.event.post(event)
            self.won = True
        
        # Check For Death
        for enemy in self.enemies:
            if self.rect.colliderect(enemy.rect):
                if pygame.sprite.collide_mask(self, enemy):
                    event = pygame.event.Event(self.events.DEAD, value = True)
                    pygame.event.post(event)
                    
    def bounce(self):
        
        self.speed = -7 if self.speed > 0 else 7
        self.reversing = True
    
    def check_vehicle_change(self, pos, targets):
        
        for key, target in targets.items():
            if target["rect"].collidepoint(pos):
                type = key.split('_')[0]
                color = key.split('_')[1]
                self.vehicle_type = type
                self.image = self.images[type][color]
                self.set_rotated_images(self.images[type][color])
                self.set_menu_play(False, False)
                self.reset_variables()
    
    # Reset Variables When Changing Car Or Map
    def reset_variables(self):
        
        self.direction = 0
        self.speed = 0
        self.turn_speed = 2.8
        self.acceleration_speed = 0.2
        self.deceleration_speed = 0.3 
        self.reversing = False
        self.velocity = pygame.math.Vector2((0, 0))
        self.bouncing = False
        self.image = self.rotated_images[0]
        self.rect = self.image.get_rect(topleft = (self.spawn_pos))
        self.won = False
        self.enemies = []
    
    def update(self):
        
        # Handle Inputs
        self.input()
        
        # Set Mask
        self.mask = pygame.mask.from_surface(self.image)

        # Check For Collisions
        self.collisions()
        
        # Calculate New Position
        self.velocity.from_polar((self.speed, self.direction))
        new_x = round(self.rect.centerx + self.velocity[0])
        new_y = round(self.rect.centery + self.velocity[1])
        self.rect.center = (new_x, new_y)
        
        
        
        