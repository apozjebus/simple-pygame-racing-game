from os import path

class Settings():
    def __init__(self):
        self.WIDTH, self.HEIGHT = 1920, 1080
        self.TILESIZE = 128  
        self.GAME_DIR = path.dirname(__file__)
        self.ASSETS_DIR = path.join(self.GAME_DIR, 'assets')
        self.FPS = 60

    def set_FPS(self, fps):
        try:
            if(fps >= 30 and fps <= 165):
                self.FPS = fps
        except:
            pass

