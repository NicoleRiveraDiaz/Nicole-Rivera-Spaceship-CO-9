import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, PLAYER_TYPE, DEFAULT_TYPE, SCREEN_WIDTH, SCREEN_HEIGHT

import sys

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

score = 0
max_score = 0

class Spaceship(pygame.sprite.Sprite):
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = 500

    def init(self):
        super().init()
        self.type = PLAYER_TYPE
        self.image = pygame.transform.scale(SPACESHIP, (40, 60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.power_up_type = DEFAULT_TYPE
        self.power_up_time_up = 0
        self.bullets = pygame.sprite.Group()
        self.power_up_count = 3

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

        if user_input[pygame.K_t] and self.power_up_count > 0:
            self.activate_power_up()

        self.update_power_up()

    def draw(self, screen):
        self.bullets.draw(screen)
        if self.rect.left < 0:
            screen.blit(self.image, (SCREEN_WIDTH + self.rect.x, self.rect.y))
        elif self.rect.right > SCREEN_WIDTH:
            screen.blit(self.image, (self.rect.x - SCREEN_WIDTH, self.rect.y))
        else:
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

    def activate_power_up(self):
        self.power_up_count -= 1
        self.power_up_time_up = pygame.time.get_ticks() + 10000  # 10 segundos de duración
        self.power_up_type = "powerx2"

    def update_power_up(self):
        if self.power_up_type == "powerx2" and pygame.time.get_ticks() > self.power_up_time_up:
            self.power_up_type = DEFAULT_TYPE

    def on_pick_power(self, time_up, type, image):
        self.image = pygame.transform.scale(image, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT)) 
        self.power_up_time_up = time_up
        self.power_up_type = type 

    def draw_power_up(self, game):
        if self.power_up_type != DEFAULT_TYPE:
            time_left = round((self.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_left >= 0:
               self.menu.draw(game.screen, f"{self.power_up_type.capitalize()} is enabled for {time_left} seconds", y=50, color=(255, 255, 255))
            else:
                self.power_up_type = DEFAULT_TYPE
                self.image = pygame.transform.scale(SPACESHIP, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))

class BulletPlayer(pygame.sprite.Sprite):
    def init(self, x, y):
        super().init()
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
            if spaceship.power_up_type == "powerx2":
                score += len(hits) * 2
            else:
                score += len(hits)

        screen.fill((0, 0, 0))
        spaceship.draw(screen)
        enemy_ships.draw(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "main":
    main()


