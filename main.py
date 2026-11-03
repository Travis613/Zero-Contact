import pygame
import sys
import random

from square import Square

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750

WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
WINDOW_BACKGROUND_COLOR = (255, 255, 255)

pygame.display.set_caption("Zero Contact")

clock = pygame.time.Clock()


player = Square(475, 350, 50, 50, "BLACK", 10)
player_rect = pygame.Rect(player.x, player.y, player.height, player.width)

enemy_x_spawn = list(range(0, 420)) + list(range(530, 950))
enemy_y_spawn = list(range(0, 340)) + list(range(410, 700))

enemy1 = Square(random.choice(enemy_x_spawn), random.choice(enemy_y_spawn), 50, 50, "BLUE", 1)
enemy1_rect = pygame.Rect(enemy1.x, enemy1.y, enemy1.height, enemy1.width)

enemy2 = Square(random.choice(enemy_x_spawn), random.choice(enemy_y_spawn), 50, 50, "RED", 1)
enemy2_rect = pygame.Rect(enemy2.x, enemy2.y, enemy2.height, enemy2.width)

enemy3 = Square(random.choice(enemy_x_spawn), random.choice(enemy_y_spawn), 50, 50, "GREEN", 1)
enemy3_rect = pygame.Rect(enemy3.x, enemy3.y, enemy3.height, enemy3.width)

enemy4 = Square(random.choice(enemy_x_spawn), random.choice(enemy_y_spawn), 50, 50, "PURPLE", 1)
enemy4_rect = pygame.Rect(enemy4.x, enemy4.y, enemy4.height, enemy4.width)

def draw():
    WINDOW.fill(WINDOW_BACKGROUND_COLOR)
    
    pygame.draw.rect(WINDOW, player.color, player_rect)
    
    pygame.draw.rect(WINDOW, enemy1.color, enemy1_rect)
    pygame.draw.rect(WINDOW, enemy2.color, enemy2_rect)
    pygame.draw.rect(WINDOW, enemy3.color, enemy3_rect)
    pygame.draw.rect(WINDOW, enemy4.color, enemy4_rect)
    
    pygame.display.update()

def main():
    running = True
    
    global player_y
    
    while running:
        clock.tick(60)
        
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