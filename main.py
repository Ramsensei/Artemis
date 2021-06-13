import pygame
from funciones import FPS, VENTANA_PRINCIPAL
import clases

pygame.init()

# Módulo principall


def main():

    pygame.display.set_caption("Artemis")
    clock = pygame.time.Clock()
    run = True

    screen = clases.Menu()

    while run:
        run = screen.process_events()

        if screen.change == "Menu":
            screen = clases.Menu()
        elif screen.change == "Game1":
            screen = clases.Game(1)
        elif screen.change == "Game2":
            screen = clases.Game(2)
        elif screen.change == "Game3":
            screen = clases.Game(3)
        elif screen.change == "About":
            screen = clases.About()

        screen.run_logic()
        screen.display_frame(VENTANA_PRINCIPAL)

        clock.tick(FPS)
    pygame.quit()


if __name__ == "__main__":
    main()
