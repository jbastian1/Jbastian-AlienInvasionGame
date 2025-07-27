import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal
# from alien import Alien
from alien_fleet import AlienFleet

class AlienInvasion:

    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_w,self.settings.screen_h)
            )
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg,
            (self.settings.screen_w, self.settings.screen_h)
            )

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

    def run_game(self) -> None:
        # Game loop
        while self.running:
            self._check_events()
            self.ship.update()
            self.alien_fleet.update_fleet()
            self._check_collision()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collision(self) -> None:
        # check collisions for ship
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._reset_level()
            # subtract one life if possible





    def _reset_level(self) -> None:
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()


    def _update_screen(self) -> None:
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        self.alien_fleet.draw()
        pygame.display.flip()

    def _check_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

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
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
