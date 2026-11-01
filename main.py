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
PLAYER_SPEED = 1

def draw():
    WINDOW.fill(WINDOW_BACKGROUND_COLOR)
    
    pygame.draw.rect(WINDOW, PLAYER_COLOR, player_rect)
    
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
            player_rect[1] -= PLAYER_SPEED
        elif pressed_keys[pygame.K_s] and player_rect.y + player_rect.height <= SCREEN_HEIGHT:
            player_rect[1] += PLAYER_SPEED
        elif pressed_keys[pygame.K_d] and player_rect.x <= SCREEN_WIDTH - player_rect.width - PLAYER_SPEED:
            player_rect[0] += PLAYER_SPEED
        elif pressed_keys[pygame.K_a] and player_rect.x >= 0:
            player_rect[0] -= PLAYER_SPEED
                
    pygame.quit()
    sys.exit()
    
if __name__ == "__main__":
    main()