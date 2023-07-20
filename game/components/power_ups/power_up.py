import random
from pygame.sprite import Sprite

from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class PowerUp(Sprite):
    def _init_(self, image, type):
        super()._init_()
        self.type = type
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, SCREEN_WIDTH - 100)
        self.rect.y = 0

    def update(self, game_speed, power_ups):
        self.rect.y += game_speed
        if self.rect.y > SCREEN_HEIGHT:
            power_ups.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
            