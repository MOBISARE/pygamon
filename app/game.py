import pygame
import pytmx
import pyscroll
import os



class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pygamon")

        cwd = os.getcwd()  # Get the current working directory (cwd)
        files = os.listdir(cwd)  # Get all the files in that directory
        print("Files in %r: %s" % (cwd, files))

        for f in os.listdir(r"C:\Users\mluc5\Documents\Python\pygamon"):
            print(f)

        # Charger la carte
        tmx_data = pytmx.util_pygame.load_pygame(r"C:\Users\mluc5\Documents\Python\pygamon\carte.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())

        # dessiner le groupe de calques
        default_layer = 1
        self.group = pyscroll.PyscrollGroup(map_layer, default_layer)


    def run(self):
        # Boucle du jeu
        running = True
        while running:
            self.group.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()
