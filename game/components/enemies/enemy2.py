import random
import pygame
from pygame.sprite import Sprite

from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, Enemy_2, ENEMY_TYPE

LEFT = "left"
RIGHT = "right"

class Enemy2(Sprite):
    X_POS_LIST = [x_pos for x_pos in range(50, SCREEN_WIDTH, 50)]
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 3

    def __init__(self):
        super().__init__()
        self.type = ENEMY_TYPE
        self.image = pygame.transform.scale(Enemy_2, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS

        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y

        self.movement = random.choice([LEFT, RIGHT])
        self.move_x = random.randint(30, 100)
        self.moving_index = 0

    def update(self, enemies, bulletmanager):
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


