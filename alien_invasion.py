import sys
import pygame
from settings import Settings
from ship import Ship
from game_stats import GameStats
from arsenal import Arsenal
# from alien import Alien
from alien_fleet import AlienFleet
from time import sleep
from button import Button
from hud import HUD

class AlienInvasion:            # last two videos unit 13 & short question

    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()
        self.settings.initialize_dynamic_settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_w,self.settings.screen_h)
            )
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg,
            (self.settings.screen_w, self.settings.screen_h)
            )

        self.game_stats = GameStats(self)
        self.HUD = HUD(self)
        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)

        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(0.7)


        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()

        self.play_button = Button(self, 'Play')
        self.game_active = False

    def run_game(self) -> None:
        # Game loop
        while self.running:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collision()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collision(self) -> None:
        # check collisions for ship
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._check_game_status()
            # subtract one life if possible

        # check collisions for aliens and bottom of screen
        if self.alien_fleet.check_fleet_left():                                                 # check_fleet_bottom -> check_fleet_left
            self._check_game_status()
        # check collisions of projectiles and aliens
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)
            self.game_stats.update(collisions)
            self.HUD.update_scores()

        if self.alien_fleet.check_destroyed_status():
           self._reset_level()
           self.settings.increase_difficulty()
           # update game stats level
           self.game_stats.update_level()
           # update HUD view


    def _check_game_status(self) -> None:

        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False

        print(self.game_stats.ships_left)


    def _reset_level(self) -> None:
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

    def restart_game(self):
        self.settings.initialize_dynamic_settings()
        self.game_stats.reset_stats()
        self.HUD.update_scores()
        self._reset_level()
        self.ship._center_ship()
        self.game_active = True
        pygame.mouse.set_visible(False)

    def _update_screen(self) -> None:
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        self.alien_fleet.draw()
        self.HUD.draw()

        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)

        pygame.display.flip()

    def _check_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.game_stats.save_scores()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and self.game_active == True:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def _check_button_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self.restart_game()

    def _check_keyup_events(self, event) -> None:
        if event.key == pygame.K_UP:                                                            # K_RIGHT -> K_UP
            self.ship.moving_up = False                                                         # moving_right -> moving_up
        elif event.key == pygame.K_DOWN:                                                        # K_LEFT -> K_DOWN
            self.ship.moving_down = False                                                       # moving_right -> moving_down


    def _check_keydown_events(self, event) -> None:
        if event.key == pygame.K_UP:                                                            # K_RIGHT -> K_UP
            self.ship.moving_up = True                                                          # moving_right -> moving_up
        elif event.key == pygame.K_DOWN:                                                        # K_LEFT -> K_DOWN
            self.ship.moving_down = True                                                        # moving_left -> moving_down
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)

        elif event.key == pygame.K_q:
            self.running = False
            self.game_stats.save_scores()
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
