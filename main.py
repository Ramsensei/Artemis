import pygame
from funciones import FPS, VENTANA_PRINCIPAL
import clases

pygame.init()

# Módulo principal


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
            screen = clases.Game1()

        screen.run_logic()
        screen.display_frame(VENTANA_PRINCIPAL)

        clock.tick(FPS)
    pygame.quit()


if __name__ == "__main__":
    main()
