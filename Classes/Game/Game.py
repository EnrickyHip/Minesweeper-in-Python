# main Game class
import pygame

from Classes.Objects.Table import Table


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        self.icon = pygame.image.load('images/icon.png')
        self.table = Table(self.screen)

        pygame.display.set_caption("Minesweeper in Python")
        pygame.display.set_icon(self.icon)

        self.loop()

    def reset(self):
        self.table = Table(self.screen)

    def loop(self):
        clock = pygame.time.Clock()
        window = True

        while window:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    window = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.reset()

                if self.table.alive and not self.table.won:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        action = False
                        if event.button == 3:
                            action = "add-flag"
                        elif event.button == 1:
                            action = "open-square"

                        if action:
                            self.table.actions(action, event)

            pygame.display.update()
        pygame.quit()
