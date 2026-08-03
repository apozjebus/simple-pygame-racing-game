import pygame
import os
from settings import Settings

pygame.font.init()
settings = Settings()

roboto = os.path.join(settings.ASSETS_DIR, 'fonts', 'roboto.ttf')
poiret = os.path.join(settings.ASSETS_DIR, 'fonts', 'poiret.ttf')

Fonts = {
    "speed_label": pygame.font.Font(roboto, 50),
    "time_taken_label": pygame.font.Font(roboto, 40),
    "start_label": pygame.font.Font(poiret, 60),
    "menu_map_label": pygame.font.Font(roboto, 40),
    "home_page_start_label": pygame.font.Font(poiret, 100),
    "home_page_maps_label": pygame.font.Font(poiret, 80),
    "home_page_map_label": pygame.font.Font(poiret, 40),
    "won_time_message": pygame.font.Font(poiret, 80),
    "record_label": pygame.font.Font(roboto, 30)
}

