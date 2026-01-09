import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player 
from shot import Shot 
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()  
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    #Player class added to groups updatable and drawable 
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    
    #Objects
    player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    # Game loop 
    while True:   
        dt = clock.tick(60) / 1000
               
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        
        #Check if player collides with asteroid
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        
        #Check if shot collides with asteroid        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                      
        log_state()
        screen.fill("black")
        #Loop over and render all drawable objects 
        
        for obj in drawable: 
            obj.draw(screen)
             
        pygame.display.flip()
        
if __name__ == "__main__":
    main()
