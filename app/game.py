import pygame
import pytmx
import pyscroll
import os

from player import Player

from pygame.time import Clock


class Game:
    """
    Attributs

    self.screen # L'écran du jeu
    self.group  # Groupe de textures constituant les couches de la map
    self.player # Le joueur
    """

    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pygamon")

        map = os.path.join("ressources", "map", "carte.tmx")

        # Charger la carte
        tmx_data = pytmx.util_pygame.load_pygame(map)
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Génération du joueur
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)

        # Liste cintenant tous les murs provoquant une collision
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))



        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.add(self.player)

    def handle_input(self) -> None:
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation('up')

        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation('down')

        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation('left')

        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation('right')

    def update(self) -> None:
        self.group.update()
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()



    def run(self) -> None:

        clock = Clock()

        # Boucle du jeu
        running = True
        while running:
            self.player.save_location()
            self.handle_input()
            self.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)
        pygame.quit()

    def get_screen(self):
        return self.screen

    def get_group(self):
        return self.group
