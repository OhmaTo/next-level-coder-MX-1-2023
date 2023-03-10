import pygame
import random
from dino_runner.components.obstacles.cactus import SmallCactus , LargeCactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.rock import Rock

from dino_runner.utils.constants import BIRD, SMALL_CACTUS, LARGE_CACTUS, ROCKS, HEART

class ObstacleManager():

    def __init__(self):
        self.obstacles = []
        self.death_index = 0
        self.heart = False

    def update(self, game_speed, game, screen):
        if len(self.obstacles) == 0:
            if random.randint(0, 3) == 0:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0,3) == 1:
                self.obstacles.append(Bird(BIRD))
            elif random.randint(0, 3) == 2:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 3) == 3:
                self.obstacles.append(Rock(ROCKS))

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield and not game.player.hammer:
                    game.heart_manager.reduce_heart()
                if game.heart_manager.heart_count < 1:
                    pygame.time.delay(2000)
                    game.playing = False
                    break
                else:
                    self.obstacles.remove(obstacle)


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
