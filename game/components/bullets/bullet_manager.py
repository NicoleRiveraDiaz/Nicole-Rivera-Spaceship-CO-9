from game.components.bullets.bullet import Bullet
import pygame 
from game.utils.constants import ENEMY_TYPE, SHIELD_TYPE

class BulletManager:
    def __init__(self):
        self.enemy_bullets = []

    
    def update(self, game):
        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.update(self.enemy_bullets)
            for enemy in game.enemy_manager.enemies:
                if enemy_bullet.rect.colliderect(game.player.rect):
                    game.enemy_manager.enemies.remove(enemy)
                    self.bullets.remove(Bullet)
                    game.score += 1

        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.update(self.enemy_bullets)
            if enemy_bullet.rect.colliderect(game.player.rect):
                self.enemy_bullets.remove(enemy_bullet)
                if game.player.power_up_time != SHIELD_TYPE: 
                    game.playing = False
                    game.death_count += 1
                    print(game.death_count)
                    pygame.time.delay(1000)
                    break
    
    def draw(self, screen):
        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.draw(screen)

    def add_bullet(self, spaceship):
        if spaceship.type == ENEMY_TYPE and not self.enemy_bullets:
            self.enemy_bullets.append(Bullet(spaceship))

    def reset(self):
        self.bulets = []
        self.enemy_bullets = []