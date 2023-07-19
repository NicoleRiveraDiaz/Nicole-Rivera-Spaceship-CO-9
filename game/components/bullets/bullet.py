import pygame
from pygame.locals import *
from game.utils.constants import BULLET_ENEMY, ENEMY_TYPE, SCREEN_HEIGHT

class Bullet(pygame.sprite.Sprite):
    SPEED = 20
    BULLETS = {
        ENEMY_TYPE: BULLET_ENEMY,
        'PLAYER': 'bullet_1'  
    }

    def __init__(self, spaceship):
        super().__init__()
        self.owner = spaceship.type
        self.image = pygame.transform.scale(self.BULLETS[self.owner], (10, 30))
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center

    def update(self, bullets, enemies):
        if self.owner == ENEMY_TYPE:
            self.rect.y += self.SPEED
            if self.rect.y >= SCREEN_HEIGHT:
                self.kill()
                return

            collisions = pygame.sprite.spritecollide(self, enemies, True)
            for enemy in collisions:
                self.kill()

        else:  
            self.rect.y -= self.SPEED
            if self.rect.y <= 0:
                self.kill()
                return

            collisions = pygame.sprite.spritecollide(self, enemies, True)
            for enemy in collisions:
                self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
