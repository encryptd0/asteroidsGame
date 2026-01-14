import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self,):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        
        # log splitting event of asteroid
        log_event("asteroid_split")

        angle = random.randint(20,50)
        #new velocities for new split asteroids
        velocity1 = self.velocity.rotate(angle)
        velocity2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        #new asteroid objects
        asteroid1 = Asteroid(self.position.x,self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x,self.position.y, new_radius)
        
        asteroid1.velocity = velocity1 * 1.2 # 1.2x faster movement (new velocities)
        asteroid2.velocity = velocity2 * 1.2
        self.kill()