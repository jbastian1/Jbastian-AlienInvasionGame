import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:                                                                     # A class to manage the ship.

    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal') -> None:
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)                 # Load the ship image.
        self.image = pygame.transform.scale(self.image,
            (self.settings.ship_w, self.settings.ship_h)
            )
        
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.boundaries.midbottom                         # Start each new ship at the bottom center of the screen.
        self.moving_right = False                                               # Movement flag; start with a ship that's not moving.
        self.moving_left = False                                                # Movement flag; start with a ship that's not moving.
        self.x = float(self.rect.x)                                             # Store a float for the ship's exact horizontal position.
        self.arsenal = arsenal

    def update(self) -> None:                                                   # Update the ship's position based on the movement flag. updating the position of the ship
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self) -> None:                                    # Update the ship's position based on the movement flag.
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:       # Update the ship's x value, not to react.
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:          # Update the ship's x value, not to react.
            self.x -= temp_speed

        self.rect.x = self.x                                                    # Update rect object from self.x

    def draw(self) -> None:
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)                                 # Draw the ship at its current location.

    def fire(self) -> bool:
        return self.arsenal.fire_bullet()