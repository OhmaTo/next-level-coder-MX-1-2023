from dino_runner.components.obstacles.obstacles import Obstacle
import random

class Rock(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 400