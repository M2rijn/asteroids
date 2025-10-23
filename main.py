import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Create groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Assign groups to containers
    Player.containers = (updatables, drawables, shots)
    AsteroidField.containers = (updatables)
    Asteroid.containers = (asteroids, updatables, drawables)
    Shot.containers = (shots, updatables, drawables)

    # Create the player and asteroid field
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update the updatables group
        updatables.update(dt)

        for asteroid in asteroids:
            # Asteroid collision check with the player
            if asteroid.collisions_check(player):
                print("Game over!")
                sys.exit()
            # Asteroid collision check with bullets
            for shot in shots:
                if asteroid.collisions_check(shot):
                    asteroid.split()
                    shot.kill()

        # Fill the screen with a black/grey backround
        screen.fill((15, 15, 15))

        # Draw the drawables group on the screen
        for drawable in drawables:
            drawable.draw(screen)

        # Update the full display to the screen
        pygame.display.flip()

        # Limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()


# --- --- --- TO DO --- --- ---
# Add a scoring system
# Implement multiple lives and respawning
# Add an explosion effect for the asteroids
# Add acceleration to the player movement
# Make the objects wrap around the screen instead of disappearing
# Add a background image
# Create different weapon types
# Make the asteroids lumpy instead of perfectly round
# Make the ship have a triangular hit box instead of a circular one
# Add a shield power-up
# Add a speed power-up
# Add bombs that can be dropped