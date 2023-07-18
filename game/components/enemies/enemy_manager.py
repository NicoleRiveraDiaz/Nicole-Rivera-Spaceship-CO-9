import os
import random
import pygame
from pygame.sprite import Sprite, Group

from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

LEFT = "left"
RIGHT = "right"

class Enemy(Sprite):
    X_POS_LIST = [x_pos for x_pos in range(50, SCREEN_WIDTH, 50)]
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 3

    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(Enemy_2, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS

        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y

        self.movement = random.choice([LEFT, RIGHT])
        self.move_x = random.randint(30, 100)
        self.moving_index = 0

    def update(self, enemies):
        self.rect.y += self.speed_y
        if self.movement == RIGHT:
            self.rect.x += self.speed_x
        else:
            self.rect.x -= self.speed_x

        self.update_movement()
        if self.rect.y >= SCREEN_HEIGHT:
            enemies.remove(self)

    def update_movement(self):
        self.moving_index += 1
        if self.rect.right >= SCREEN_WIDTH:
            self.movement = LEFT
        elif self.rect.left <= 0:
            self.movement = RIGHT

        if self.moving_index >= self.move_x:
            self.moving_index = 0
            self.move_x = random.randint(30, 100)
            self.movement = LEFT if self.movement == RIGHT else RIGHT

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class EnemyZigzag(Sprite):
    X_POS_LIST = [x_pos for x_pos in range(50, SCREEN_WIDTH, 50)]
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 3

    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(Enemy_2, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS

        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y

        self.movement = random.choice([LEFT, RIGHT])
        self.move_x = random.randint(30, 100)
        self.moving_index = 0

    def update(self, enemies):
        self.rect.y += self.speed_y
        if self.movement == RIGHT:
            self.rect.x += self.speed_x
        else:
            self.rect.x -= self.speed_x

        self.update_movement()
        if self.rect.y >= SCREEN_HEIGHT:
            enemies.remove(self)

    def update_movement(self):
        self.moving_index += 1
        if self.rect.right >= SCREEN_WIDTH:
            self.movement = LEFT
        elif self.rect.left <= 0:
            self.movement = RIGHT

        if self.moving_index >= self.move_x:
            self.moving_index = 0
            self.move_x = random.randint(30, 100)
            self.movement = LEFT if self.movement == RIGHT else RIGHT

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class EnemyManager:
    def __init__(self):
        self.enemies = []

    def update(self):
        if not self.enemies:
            enemy_type = random.choice([Enemy, EnemyZigzag])
            new_enemy = enemy_type()

            self.enemies.append(new_enemy)

        for enemy in self.enemies:
            enemy.update(self.enemies)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    enemy_1_image_path = os.path.join("images", "enemy_1.png")
    enemy_2_image_path = os.path.join("images", "enemy_2.png")

    enemy_manager = EnemyManager()

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
                

    def run(self):
        
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        puser_input = pygame.key.get_pressed()
        self.player.update(user_input)
        
        self.enemy.update()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

        screen.fill((0, 0, 0))
        enemy_manager.update()
        enemy_manager.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

