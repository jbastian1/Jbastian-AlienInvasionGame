"""
Program: Alien Invasion!
Author: Jonathan Bastian
The program is a spaceship game, 'Alien Invasion', following the video resources on blackboard, as well as parts from the textbook.
Date: Sunday, July 20, 2025
"""

import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal

class AlienInvasion:                                                # Overall class to manage game assets and behavior.

    def __init__(self) -> None:                                     # Initialize the game, and create game resources.
        # from alien_fleet import AlienFleet
        pygame.init()
        self.settings = Settings()
        # self.settings.initialize_dynamic_settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_w,self.settings.screen_h)
            )
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg,
            (self.settings.screen_w, self.settings.screen_h)
            )

        self.running = True
        self.clock = pygame.time.Clock()

        # self.game_stats = GameStats(self)
        # self.HUD = HUD(self)
        self.ship = Ship(self, Arsenal(self))
        # self.aliens = AlienFleet(self)


        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)

    def run_game(self) -> None:                                     # Start the main loop for the game. Game loop
        while self.running:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _update_screen(self) -> None:                               # Update images on the screen, and flip to the new screen.
            self.screen.blit(self.bg, (0,0))
            self.ship.draw()
            pygame.display.flip()                                   # Make the most recently drawn screen visible.

    def _check_events(self) -> None:                                # Respond to keypresses and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                     self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                     self._check_keyup_events(event)

    def _check_keyup_events(self, event) -> None:                   # Respond to key releases.
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_keydown_events(self, event) -> None:                 # Respond to keypresses.
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)

        elif event.key == pygame.K_q:
             self.running = False
             pygame.quit()
             sys.exit()


if __name__ == '__main__':                                          # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()