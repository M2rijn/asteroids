import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # Sub-classes must override
        pass

    def update(self, dt):
        # Sub-classes must override
        pass

    def collisions_check(self, other):
        distance = pygame.math.Vector2.distance_to(self.position, other.position)
        r1 = self.radius
        r2 = other.radius

        return distance <= (r1 + r2)