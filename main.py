import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750

WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
WINDOW_BACKGROUND_COLOR = (255, 255, 255)

pygame.display.set_caption("Zero Contact")

clock = pygame.time.Clock()

running = True

player_rect = pygame.Rect(475, 350, 50, 50)
PLAYER_SPEED = 10

enemy_x_spawn = list(range(0, 420)) + list(range(530, 950))
enemy_y_spawn = list(range(0, 340)) + list(range(410, 700))

ENEMY_SPEED = 10

enemy1_rect = pygame.Rect(random.choice(enemy_x_spawn), random.choice(enemy_y_spawn), 50, 50)
enemy2_rect = pygame.Rect(random.choice(enemy_x_spawn), random.choice(enemy_y_spawn), 50, 50)
enemy3_rect = pygame.Rect(random.choice(enemy_x_spawn), random.choice(enemy_y_spawn), 50, 50)
enemy4_rect = pygame.Rect(random.choice(enemy_x_spawn), random.choice(enemy_y_spawn), 50, 50)

def draw():
    WINDOW.fill(WINDOW_BACKGROUND_COLOR)
    
    pygame.draw.rect(WINDOW, "black", player_rect)
    
    pygame.draw.rect(WINDOW, "blue", enemy1_rect)
    pygame.draw.rect(WINDOW, "red", enemy2_rect)
    pygame.draw.rect(WINDOW, "green", enemy3_rect)
    pygame.draw.rect(WINDOW, "purple", enemy4_rect)
    
    pygame.display.update()
    
while running:
    clock.tick(60)
        
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