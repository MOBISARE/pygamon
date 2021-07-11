import pygame

from game import Game

if __name__ == "__main__":
    print("Launching...\n")
    pygame.init()
    game = Game()
    game._run()