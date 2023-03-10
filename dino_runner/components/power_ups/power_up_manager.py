from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.utils.constants import FONT_ARIAL, SCREEN
import random
import pygame


class PowerUpManager:
    pygame.init()

    def __init__(self):
        self.power_ups = []
        self.points = 0
        self.when_appears = 0
        self.options = list(range(1, 10))
        self.n_power = None
        self.font = pygame.font.Font(FONT_ARIAL, 25)

    def generate_power_ups(self, points):
        self.points = points

        if len(self.power_ups) == 0:
            if self.when_appears == self.points:
                print("generating power up")
                self.when_appears = random.randint(
                    self.when_appears+100, 200+self.when_appears)
                if random.randint(0,2) == 0:
                    self.power_ups.append(Shield())
                    self.n_power = 0
                    return self.n_power
                elif random.randint(0,2) == 1:
                    self.power_ups.append(Hammer())
                    self.n_power = 1
                    return self.n_power 

        return self.power_ups

    def update(self, points, game_speed, player, screen):
        self.generate_power_ups(points)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)

            if player.dino_rect.colliderect(power_up.rect):
                if self.n_power == 0:
                    player.shield = True
                elif self.n_power == 1:
                    player.hammer = True

                shield_sound = pygame.mixer.Sound('Music/shield.wav')
                shield_sound.play()

                player.type = power_up.type
                start_time = pygame.time.get_ticks()
                time_random = random.randrange(5, 8)
                player.power_time_up  = start_time + (time_random * 1000)
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power in self.power_ups:
            power.draw(screen)
