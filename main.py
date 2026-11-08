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
PLAYER_SPEED = 5

enemy_x_spawn = list(range(0, 420)) + list(range(530, 950))
enemy_y_spawn = list(range(0, 340)) + list(range(410, 700))

class Enemy(pygame.Rect):
    def __init__(self, dx, dy):
        self.rect = pygame.Rect.__init__(self, random.choice(enemy_x_spawn), random.choice(enemy_y_spawn), 50, 50)
        self.enemy_speed_dx = dx
        self.enemy_speed_dy = dy
        
enemy1 = Enemy(random.choice([-5, 5]), random.choice([-5, 5]))
enemy2 = Enemy(random.choice([-5, 5]), random.choice([-5, 5]))
enemy3 = Enemy(random.choice([-5, 5]), random.choice([-5, 5]))
enemy4 = Enemy(random.choice([-5, 5]), random.choice([-5, 5]))

def draw():
    WINDOW.fill(WINDOW_BACKGROUND_COLOR)
    
    pygame.draw.rect(WINDOW, "black", player_rect)
    
    pygame.draw.rect(WINDOW, "blue", enemy1)
    pygame.draw.rect(WINDOW, "red", enemy2)
    pygame.draw.rect(WINDOW, "green", enemy3)
    pygame.draw.rect(WINDOW, "purple", enemy4)
    
    pygame.display.update()
    
while running:
    clock.tick(60)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                
    draw()
        
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
        player_rect.y -= PLAYER_SPEED
        if player_rect.y <= 0:
            player_rect.y = 0
    elif pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
        player_rect.y += PLAYER_SPEED
        if player_rect.y >= SCREEN_HEIGHT - player_rect.height:
            player_rect.y = SCREEN_HEIGHT - player_rect.height
    elif pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
        player_rect.x += PLAYER_SPEED
        if player_rect.x >= SCREEN_WIDTH - player_rect.width:
            player_rect.x = SCREEN_WIDTH - player_rect.width
    elif pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
        player_rect.x -= PLAYER_SPEED
        if player_rect.x <= 0:
            player_rect.x = 0
            
    enemy1.x += enemy1.enemy_speed_dx
    enemy1.y += enemy1.enemy_speed_dy
    
    if enemy1.x <= 0 or enemy1.x >= SCREEN_WIDTH - enemy1.width:
        enemy1.enemy_speed_dx *= -1
         
    if enemy1.y <= 0 or enemy1.y >= SCREEN_HEIGHT - enemy1.height:
        enemy1.enemy_speed_dy *= -1
        
    enemy2.x += enemy2.enemy_speed_dx
    enemy2.y += enemy2.enemy_speed_dy
        
    if enemy2.x <= 0 or enemy2.x >= SCREEN_WIDTH - enemy2.width:
        enemy2.enemy_speed_dx *= -1
             
    if enemy2.y <= 0 or enemy2.y >= SCREEN_HEIGHT - enemy2.height:
        enemy2.enemy_speed_dy *= -1
        
    enemy3.x += enemy3.enemy_speed_dx
    enemy3.y += enemy3.enemy_speed_dy
        
    if enemy3.x <= 0 or enemy3.x >= SCREEN_WIDTH - enemy3.width:
        enemy3.enemy_speed_dx *= -1
             
    if enemy3.y <= 0 or enemy3.y >= SCREEN_HEIGHT - enemy3.height:
        enemy3.enemy_speed_dy *= -1
        
    enemy4.x += enemy4.enemy_speed_dx
    enemy4.y += enemy4.enemy_speed_dy
        
    if enemy4.x <= 0 or enemy4.x >= SCREEN_WIDTH - enemy4.width:
        enemy4.enemy_speed_dx *= -1
             
    if enemy4.y <= 0 or enemy4.y >= SCREEN_HEIGHT - enemy4.height:
        enemy4.enemy_speed_dy *= -1

pygame.quit()
sys.exit()