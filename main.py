import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player 


def main():
    #Groups
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()  
    #Player class added to groups updatable and drawable 
    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)
    
    # Game loop 
    
    while True:   
        dt = clock.tick(60) / 1000
               
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        
        log_state()
        
        screen.fill("black")
        #Loop over and render all drawable objects 
        
        for obj in drawable: 
            obj.draw(screen)
            
        pygame.display.flip()
     
    
if __name__ == "__main__":
    main()
