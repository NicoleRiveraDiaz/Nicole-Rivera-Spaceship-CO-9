from game.components.power_ups.power_up import PowerUp
from game.utils.constants import SHIELD_TYPE, SHIELD, SPACESHIP


class Shield(PowerUp):
    def _init_(self):
        super()._init_(SHIELD, SHIELD_TYPE)
        self.spaceship_image = SPACESHIP
