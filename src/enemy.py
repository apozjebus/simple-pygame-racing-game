import pygame
import os
import math
from settings import Settings
from events import Events

class Enemy(pygame.sprite.Sprite):   
    def __init__(self, groups, pos, finish_line_rect, path = [], vel = 10):
        
        # Basic Declarations
        super().__init__(groups)
        self.settings = Settings()
        self.events = Events()
        self.finish_line_rect = finish_line_rect
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(self.settings.ASSETS_DIR, 'imgs', 'player', 'car', 'bomb.png')).convert_alpha(), (55, 110))
        self.rotated_images = []
        self.possible_rotations = 360
        
        for i in range(self.possible_rotations):
            
            # Image Has To Be Offset By 90 Degrees For The Radians, Iunno What That Means
            rotated_image = pygame.transform.rotozoom(self.image, 360 - 90 - i, 1)
            self.rotated_images.append(rotated_image)
        
        self.image = self.rotated_images[0]   
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = 270
        self.vel = vel
        self.rotation_vel = 10
        self.path = path
        self.current_point = 0
        self.x, self.y = (pos[0], pos[1])
        self.mirror_turn = 90
    
    def movement(self):
        
        radians = math.radians(self.direction)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def calculate_angle(self):
        
        target_x, target_y = self.path[self.current_point]
        x_diff = target_x - self.x
        y_diff = target_y - self.y

        if y_diff == 0:
            desired_radian_angle = math.pi / 2
        else:
            desired_radian_angle = math.atan(x_diff / y_diff)

        if target_y > self.y:
            desired_radian_angle += math.pi

        difference_in_angle = self.direction - math.degrees(desired_radian_angle)
        if difference_in_angle >= 180:
            difference_in_angle -= 360

        if difference_in_angle > 0:
            self.direction -= min(self.rotation_vel, abs(difference_in_angle))
        else:
            self.direction += min(self.rotation_vel, abs(difference_in_angle))

        self.mirror_turn = 360 - self.direction

        if(self.image != self.rotated_images[(int(self.mirror_turn) % 360) - 90]):
            self.image = self.rotated_images[(int(self.mirror_turn) % 360) - 90]
            
        self.rect = self.image.get_rect(center=self.image.get_rect(topleft=(self.x, self.y)).center)

    def update_path_point(self):
        
        target = self.path[self.current_point]
        rect = pygame.Rect(
            self.x, self.y, self.image.get_width(), self.image.get_height())
        if rect.collidepoint(*target):
            self.current_point += 1
    
    def collisions(self):
        
        # Check For Collision With Finish Line
        if self.rect.colliderect(self.finish_line_rect):
            event = pygame.event.Event(self.events.BOTWON, value = True)
            pygame.event.post(event)

    def move(self):

        self.calculate_angle()
        self.update_path_point()
        self.movement()

    def update(self):

        # Move
        self.move()

        # Calculate New Position
        new_x = self.x
        new_y = self.y
        self.rect.center = (new_x, new_y)

        # Check Collisions
        self.collisions()