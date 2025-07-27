from pathlib import Path
class Settings:

    def __init__(self) -> None:
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnowside.png'

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2side(no bg).png'                  # ship2(no bg) -> ship2side(no bg)
        self.ship_w = 60                                                                            # 40 -> 60
        self.ship_h = 40                                                                            # 60 -> 40
        self.ship_speed = 5

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlastside.png'                  # laserBlast -> laserBlastside
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'
        self.bullet_speed = 7
        self.bullet_w = 60                                                                          # (25 -> 80)
        self.bullet_h = 40                                                                          # (80 -> 25)
        self.bullet_amount = 5

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_speed = 2
        self.fleet_direction = 1
        self.fleet_drop_speed = 40



