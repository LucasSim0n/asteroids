import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x, y, PLAYER_RADIUS)
    astrofield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60.0) / 1000

        screen.fill((0, 0, 0))

        updatable.update(dt)

        for aster in asteroids:
            if aster.collision_detection(player):
                raise SystemExit("Game Over!")
            for shot in shots:
                if shot.collision_detection(aster):
                    aster.split()
                    shot.kill()

        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
