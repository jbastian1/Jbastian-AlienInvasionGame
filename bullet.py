import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):                                               # A class to manage bullets fired from the ship.
    def __init__(self, game: 'AlienInvasion') -> None:              # Create a bullet object at the ship's current position.
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.bullet_w, self.settings.bullet_h)
            )

        self.rect = self.image.get_rect()                           # Create a bullet rect and then set correct position.
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)                                 # Store the bullet's position as a float.

    def update(self) -> None:                                       # Move the bullet up the screen.
        self.y -= self.settings.bullet_speed                        # Update the exact position of the bullet.
        self.rect.y = self.y                                        # Update the rect position.

    def draw_bullet(self) -> None:                                  # Draw the bullet to the screen.
        self.screen.blit(self.image, self.rect)
