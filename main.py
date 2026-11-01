import pygame
import sys

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750

WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
WINDOW_BACKGROUND_COLOR = (255, 255, 255)

pygame.display.set_caption("Zero Contact")

player_x = 475
player_y = 350
PLAYER_HEIGHT = 50
PLAYER_WIDTH = 50
player_rect = pygame.Rect(player_x, player_y, PLAYER_HEIGHT, PLAYER_WIDTH)
PLAYER_COLOR = (0, 0, 0)

def draw():
    WINDOW.fill(WINDOW_BACKGROUND_COLOR)
    
    pygame.draw.rect(WINDOW, PLAYER_COLOR, player_rect)
    
    pygame.display.update()

def main():
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        draw()
                
    pygame.quit()
    sys.exit()
    
if __name__ == "__main__":
    main()