import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20.0, 50.0)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        first_new_vector = self.velocity.rotate(angle)
        second_new_vector = self.velocity.rotate(angle - angle * 2)

        new1 = Asteroid(self.position[0], self.position[1], new_radius)
        new2 = Asteroid(self.position[0], self.position[1], new_radius)

        new1.velocity = first_new_vector * 1.2
        new2.velocity = second_new_vector * 1.2

        return new1, new2
