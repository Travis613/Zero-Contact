import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750

PLAYER_HEIGHT = 50
PLAYER_WIDTH = 50
PLAYER_X = 475
PLAYER_Y = 350
PLAYER_SPEED = 5

WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
WINDOW_BACKGROUND_COLOR = (255, 255, 255)

pygame.display.set_caption("Zero Contact")

clock = pygame.time.Clock()

enemy_x_spawn = list(range(0, 420)) + list(range(530, 950))
enemy_y_spawn = list(range(0, 340)) + list(range(410, 700))

enemy1_rect = pygame.Rect(random.choice(enemy_x_spawn), random.choice(enemy_y_spawn), 50, 50)
enemy2_rect = pygame.Rect(random.choice(enemy_x_spawn), random.choice(enemy_y_spawn), 50, 50)
enemy3_rect = pygame.Rect(random.choice(enemy_x_spawn), random.choice(enemy_y_spawn), 50, 50)
enemy4_rect = pygame.Rect(random.choice(enemy_x_spawn), random.choice(enemy_y_spawn), 50, 50)

class Player(pygame.Rect):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, height, width)
        self.color = color

class Enemy():
    def __init__(self, rect, dx, dy):
        self.rect = rect
        self.enemy_speed_dx = dx
        self.enemy_speed_dy = dy
        
    def move(self):
        self.rect.x += self.enemy_speed_dx
        self.rect.y += self.enemy_speed_dy
        
        if self.rect.x <= 0 or self.rect.x >= SCREEN_WIDTH - self.rect.width:
            self.enemy_speed_dx *= -1
                 
        if self.rect.y <= 0 or self.rect.y >= SCREEN_HEIGHT - self.rect.height:
            self.enemy_speed_dy *= -1
            
player = Player(PLAYER_X, PLAYER_Y, PLAYER_HEIGHT, PLAYER_WIDTH, "BLACK")
    
enemy1 = Enemy(enemy1_rect, random.choice([-5, 5]), random.choice([-5, 5]))
enemy2 = Enemy(enemy2_rect, random.choice([-5, 5]), random.choice([-5, 5]))
enemy3 = Enemy(enemy3_rect, random.choice([-5, 5]), random.choice([-5, 5]))
enemy4 = Enemy(enemy4_rect, random.choice([-5, 5]), random.choice([-5, 5]))

enemies_rects = [enemy1.rect, enemy2.rect, enemy3.rect, enemy4.rect]

def move():
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
        player.y -= PLAYER_SPEED
        if player.y <= 0:
            player.y = 0
    elif pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
        player.y += PLAYER_SPEED
        if player.y >= SCREEN_HEIGHT - player.height:
            player.y = SCREEN_HEIGHT - player.height
    elif pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
        player.x += PLAYER_SPEED
        if player.x >= SCREEN_WIDTH - player.width:
            player.x = SCREEN_WIDTH - player.width
    elif pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
        player.x -= PLAYER_SPEED
        if player.x <= 0:
            player.x = 0
            
    enemy1.move()
    enemy2.move()
    enemy3.move()
    enemy4.move()            


def draw():
    WINDOW.fill(WINDOW_BACKGROUND_COLOR)
    
    pygame.draw.rect(WINDOW, "black", player)
    
    pygame.draw.rect(WINDOW, "blue", enemy1)
    pygame.draw.rect(WINDOW, "red", enemy2)
    pygame.draw.rect(WINDOW, "green", enemy3)
    pygame.draw.rect(WINDOW, "purple", enemy4)
    
def runGame():
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        if player.collidelist(enemies_rects) != -1:
            running = False
        
        move()
        draw()
        
        pygame.display.update()
        clock.tick(60)
        
if __name__ == "__main__":
    runGame()

pygame.quit()
sys.exit()