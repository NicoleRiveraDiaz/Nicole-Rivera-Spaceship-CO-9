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
    X_POS_LIST = [x_pos for x_pos in range(50, SCREEN_WIDTH, 50)]
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 3

    def __init__(self):
        super().__init__()
        self.type = ENEMY_TYPE
        self.image = pygame.transform.scale(ENEMY_1, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS

        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y

        self.movement = random.choice([LEFT, RIGHT])
        self.move_x = random.randint(30, 100)
        self.moving_index = 0

        self.shooting_time = random.randint(30, 50)

    def update(self, enemies, bullet_manager):
        self.rect.y += self.speed_y
        self.shoot(bullet_manager)
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

    def shoot(self, bullet_manager, bulletplayer):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet_manager.add_bullet(bulletplayer(self.rect.centerx, self.rect.bottom))
            self.shooting_time = current_time + random.randint(30, 50)

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

    if __name__ == "__main__":
        main()

def reset(self):
    pass