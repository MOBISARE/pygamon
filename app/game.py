import pygame
import pytmx
import pyscroll
import os

import player


class Game:
    """
    Attributs

    self.screen # L'écran du jeu
    self.group  # Groupe de textures constituant les couches de la map
    self.player # Le joueur
    """

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pygamon")

        map = os.path.join("ressources", "map", "carte.tmx")

        # Charger la carte
        tmx_data = pytmx.util_pygame.load_pygame(map)
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())

        # Génération du joueur
        self.player = player.Player()

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.player)

    def _run(self):
        # Boucle du jeu
        running = True
        while running:
            self.group.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()

    def get_screen(self):
        return self.screen

    def get_group(self):
        return self.group
