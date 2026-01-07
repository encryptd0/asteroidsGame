import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    while True:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        log_state()
        screen.fill("black")
        pygame.display.flip()
     
     
        clock.tick(60)
    
if __name__ == "__main__":
    main()
