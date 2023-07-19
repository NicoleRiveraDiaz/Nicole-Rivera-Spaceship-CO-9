from ast import main
import os
import random
import pygame
from pygame.sprite import Sprite, Group

from game.utils.constants import ENEMY_1, ENEMY_2, ENEMY_TYPE, SCREEN_WIDTH, SCREEN_HEIGHT, SPACESHIP, FPS, BG, TITLE, ICON 

LEFT = "left"
RIGHT = "right"

class Enemy(Sprite):
    LEFT = "left"
    RIGHT = "right"
    X_POS_LISIT = [x_pos for x_pos in range(50, SCREEN_WIDTH,50)]
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 3

def __init__(self):
    self.type = ENEMY_TYPE
    self.image = pygame.transform.scale(ENEMY_1, (50,50))
    self.rect = self.image.get_rect()
    self.rect.x = random.choice(self.X_POS_LIST)
    self.rect.y = self.Y_POS

    self.speed_x = self.SPEED_X
    self.speed_y = self.SPEED_Y

    self.movement = random.choice([LEFT, RIGHT])
    self.move_x = random.randint(30, 100)
    self.moving_index = 0

    self.shooting_time = random.randit(30, 50)

def update(self, enemies, bullet_manager):
    self.rect.y += self.speed_y
    self.shoot(bullet_manager)
    if self.movement == RIGHT:
        self.rect.x += self.speed_x
    else:
        self.rect.x -= self.speed_x

    self.update_movement()
    if self.rect.y <= SCREEN_HEIGHT:
        enemies.remove(self)

    def update_movement(self):
        print(self.movement)
        print(self.move_x)
        self.moving_index += 1
        if self.rect.right >= SCREEN_WIDTH:
            self.movement = LEFT
        elif self.rect.left <= 0:
            self.movement = RIGHT

        if self.moving_index >= self.move_x:
                self.move_x = 0
                self.movement = LEFT if self.movement == RIGHT else RIGHT
                if self.movement == RIGHT:
                    self.movement = LEFT
                else:
                    self.mmovement = RIGHT

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet_manager.add_bullet(self)
            self.shooting_time += current_time + random.randit (30, 50)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Enemy2(Sprite):
    X_POS_LIST = [x_pos for x_pos in range(50, SCREEN_WIDTH, 50)]
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 3

    def __init__(self):
        super().__init__()
        self.type = ENEMY_TYPE
        self.image = pygame.transform.scale(ENEMY_2, (50, 50))
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

    def update(self, game):
        if not self.enemies:
            enemy_type = random.choice([Enemy, Enemy2])
            new_enemy = enemy_type()

            self.enemies.append(new_enemy)

        for enemy in self.enemies:
            enemy.update(self.enemies, game.bullet_manager)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def reset(self):
        self.enemies = []

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

class BulletManager:
    def __init__(self):
        self.bullets = []

    def update(self, game):
        for bullet in self.bullets.copy():
            bullet.update()
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    def reset(self):
        self.enemies = []

    def add_bullet(self, bullet):
        self.bullets.append(bullet)

class Game():
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
        self.player = SPACESHIP()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()

    def run(self):
        # Game loop: events - update - draw
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
        user_input = pygame.key.get_pressed()  # Corrección del nombre de la variable
        self.player.update(user_input)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)  # Pasar la instancia de "Game" al BulletManager

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)  # Llamar al método draw del EnemyManager
        self.bullet_manager.draw(self.screen)  # Llamar al método draw del BulletManager
        pygame.display.update()

    def draw_background(self, screen, clock):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

        screen.fill((0, 0, 0))
        EnemyManager.update()
        EnemyManager.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

def reset(self):
    pass