# Importaciones
import pygame
import funciones as fc
from funciones import FPS, VENTANA_PRINCIPAL
import clases

pygame.init()


# Módulo principall
def main():

    pygame.display.set_caption("Artemis")
    clock = pygame.time.Clock()
    run = True

    # Definiendo menú principal como primera pantalla
    screen = clases.Menu()
    
    # Imprimiendo documentación
    fc.mi_auto_doc()

    # Bucle principal
    while run:
        run = screen.process_events()

        # Manejo de pantallas
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
        elif screen.change == "Top":
            screen = clases.Top()
        elif screen.change == "GameOver":
            screen = clases.GameOver()

        # Ejecutando métodos
        screen.run_logic()
        screen.display_frame(VENTANA_PRINCIPAL)

        # frames per second
        clock.tick(FPS)
        
    pygame.quit()


if __name__ == "__main__":
    main()