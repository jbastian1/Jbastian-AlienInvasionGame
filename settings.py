from pathlib import Path
class Settings:

    def __init__(self) -> None:
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200                                                                        # (1200, no need to change)
        self.screen_h = 800                                                                         # (800, no need to change)
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnowside.png'
        self.difficulty_scale = 1.1

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2side(no bg).png'                  # ship2(no bg) -> ship2side(no bg)
        self.ship_w = 60                                                                            # 40 -> 60
        self.ship_h = 40                                                                            # 60 -> 40

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlastside.png'                  # laserBlast -> laserBlastside
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4_side.png'                     # enemy_4 -> enemy_4_side
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_direction = 1

        self.button_w = 200
        self.button_h = 50
        self.button_color = (0,135,50)

        self.text_color = (255,255,255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'Silkscreen-Bold.ttf'

    def initialize_dynamic_settings(self) -> None:
        self.ship_speed = 5
        self.starting_ship_count = 3

        self.bullet_w = 80                                                                          # (25 -> 80; 60)
        self.bullet_h = 25                                                                          # (80 -> 25; 40)
        self.bullet_speed = 7
        self.bullet_amount = 5

        self.fleet_speed = 2
        self.fleet_drop_speed = 40

    def increase_difficulty(self) -> None:
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale






