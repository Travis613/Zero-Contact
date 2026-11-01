import pygame
import sys

from square import Square

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750

WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
WINDOW_BACKGROUND_COLOR = (255, 255, 255)

pygame.display.set_caption("Zero Contact")


player = Square(475, 350, 50, 50, "BLACK", 1)
player_rect = pygame.Rect(player.x, player.y, player.height, player.width)

def draw():
    WINDOW.fill(WINDOW_BACKGROUND_COLOR)
    
    pygame.draw.rect(WINDOW, player.color, player_rect)
    
    pygame.display.update()

def main():
    running = True
    
    global player_y
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        draw()
        
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w] and player_rect.y >= 0:
            player_rect[1] -= player.speed
        elif pressed_keys[pygame.K_s] and player_rect.y + player_rect.height <= SCREEN_HEIGHT:
            player_rect[1] += player.speed
        elif pressed_keys[pygame.K_d] and player_rect.x <= SCREEN_WIDTH - player_rect.width - player.speed:
            player_rect[0] += player.speed
        elif pressed_keys[pygame.K_a] and player_rect.x >= 0:
            player_rect[0] -= player.speed
                
    pygame.quit()
    sys.exit()
    
if __name__ == "__main__":
    main()