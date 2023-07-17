import prandom
from pygame.sprite import Sprite

from game.utils.constants import Enemy_1





LEFT = "left"
RIGHT = "right"
Class Enemy(Sprite):
X_POS_LISIT = [x_pos for x_pos in range(50, SCREEN_WIDTH,50)]
Y_POS = 20
SPEED_X = 5
SPEED_Y = 3

def __init__(self):
    self.image = pygame.transform.scale(Enemy_1, (50,50))
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
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

