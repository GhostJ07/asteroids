import pygame

# asteroid class for the game

from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt 

    def split(self):
        self.kill()#it kills the big or small one with a hit

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20,50)  # randomize the angle of the split

        dir1 = self.velocity.rotate(random_angle)
        dir2 = self.velocity.rotate(-random_angle)
        
        smaller_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid = Asteroid(self.position.x,self.position.y,smaller_radius)
        asteroid.velocity = dir1 * 1.2
        asteroid = Asteroid(self.position.x,self.position.y,smaller_radius)
        asteroid.velocity = dir2 * 1.2


