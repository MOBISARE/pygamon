import os

import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        player = os.path.join("ressources", "player", "player.png")
        self.sprite_sheet = pygame.image.load(player)
        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0,0), (x, y, 32, 32))
        return image



