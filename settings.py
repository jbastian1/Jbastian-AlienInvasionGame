from pathlib import Path
class Settings:

    def __init__(self) -> None:                                                 # Initializing the game's settings.
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'  # Ship settings
        self.ship_w = 40                                                        # Ship settings
        self.ship_h = 60                                                        # Ship settings
        self.ship_speed = 5                                                     # Ship settings

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'  # Bullet settings
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'        # Bullet settings
        self.bullet_speed = 7                                                   # Bullet settings
        self.bullet_w = 25                                                      # Bullet settings
        self.bullet_h = 80                                                      # Bullet settings
        self.bullet_amount = 5                                                  # Bullet settings

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_speed = 2
        self.fleet_direction = 1
        self.fleet_drop_speed = 40