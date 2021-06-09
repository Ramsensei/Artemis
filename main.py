import pygame
from funciones import FPS
from clases import Menu


# Módulo principal


def main():
    pygame.init()
    pygame.display.set_caption("Artemis")
    clock = pygame.time.Clock()
    run = True

    menu = Menu()

    while run:
        run = menu.process_events()
        menu.run_logic()
        menu.display_frame()
        clock.tick(FPS)
    pygame.quit()


if __name__ == "__main__":
    main()
