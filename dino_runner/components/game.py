import pygame

from dino_runner.utils.constants import (
    BG,
    ICON,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TITLE,
    FPS,
    FONT_ARIAL,
    RUNNING,
    SCREEN,
    POINTS,
)

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.player_hearts.heart_manager import HeartManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager


class Game:
    pygame.init()

    def __init__(self):
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.points = POINTS
        pygame.mixer.music.load('Music/bg_sound.mp3')
        pygame.mixer.music.play(-1)

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.heart_manager = HeartManager()
        self.power_up_manager = PowerUpManager()

    def increase_score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        self.player.check_invincibility()

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self.game_speed, self, SCREEN)
        self.power_up_manager.update(self.points, self.game_speed, self.player, SCREEN)
        self.increase_score()

    def draw(self):
        self.clock.tick(FPS)
        SCREEN.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(SCREEN)
        self.obstacle_manager.draw(SCREEN)
        self.draw_score()
        self.power_up_manager.draw(SCREEN)
        self.heart_manager.draw(SCREEN)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        SCREEN.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        SCREEN.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        font = pygame.font.Font(FONT_ARIAL, 25)
        surface = font.render(
            f"Current score: {str(self.points)}", True, (255, 255, 255))
        rect = surface.get_rect()
        rect.x = 800
        rect.y = 30
        SCREEN.blit(surface, rect)
