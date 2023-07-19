import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT

import sys

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

score = 0
max_score = 0

class Spaceship(pygame.sprite.Sprite):
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = 500

    def __init__(self):
        super().__init__()
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.bullets = pygame.sprite.Group()

    def update(self, user_input):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()

        if user_input[pygame.K_x]:
            self.shoot_bullet()

        self.bullets.update()

    def draw(self, screen):
        self.bullets.draw(screen)
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= 10
        else:
            self.rect.x = SCREEN_WIDTH - self.rect.width

    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10
        else:
            self.rect.x = 0

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= 10

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y += 10

    def shoot_bullet(self):
        bullet = BulletPlayer(self.rect.centerx, self.rect.top)
        self.bullets.add(bullet)

class BulletPlayer(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("bullet_1.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

    def update(self):
        self.rect.y -= 8
        
        if self.rect.bottom < 0:
            self.kill()

def show_score_screen(screen, score, max_score):
    font = pygame.font.Font(None, 36)
    text_surface = font.render("Score: " + str(score), True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20))

    max_score_surface = font.render("Max score: " + str(max_score), True, (255, 255, 255))
    max_score_rect = max_score_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))

    screen.blit(text_surface, text_rect)
    screen.blit(max_score_surface, max_score_rect)
    pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Spaceship Game")

    spaceship = Spaceship()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(spaceship)

    enemy_ships = pygame.sprite.Group()

    clock = pygame.time.Clock()
    global score, max_score

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        spaceship.update(keys)

        hits = pygame.sprite.groupcollide(enemy_ships, spaceship.bullets, True, True)
        if hits:
            score += len(hits)

        screen.fill((0, 0, 0))
        spaceship.draw(screen)
        enemy_ships.draw(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()



