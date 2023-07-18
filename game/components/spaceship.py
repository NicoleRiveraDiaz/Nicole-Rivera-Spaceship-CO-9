import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT

class Spaceship(Sprite):
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = 500

    def __init__(self):
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
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.bullets.add(bullet)

class Bulletplayer(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((4, 10))
        self.image = pygame.image.load("bullet_1.png")
        self.rect.centerx = x
        self.rect.bottom = y

    def update(self):
        self.rect.y -= 8
        
        if self.rect.bottom < 0:
            self.kill()

