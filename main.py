import pygame
from funciones import FPS, VENTANA_PRINCIPAL
from clases import Menu

pygame.init()

# Módulo principal


def main():

    pygame.display.set_caption("Artemis")
    clock = pygame.time.Clock()
    run = True

    menu = Menu()

    while run:
        run = menu.process_events()
        menu.run_logic()
        menu.display_frame(VENTANA_PRINCIPAL)
        clock.tick(FPS)
    pygame.quit()


if __name__ == "__main__":
    main()
