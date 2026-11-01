import pygame
import sys

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750

WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Zero Contact")

def main():
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
    pygame.quit()
    sys.exit()
    
if __name__ == "__main__":
    main()