import pygame
from os import path

pygame.init()

# Variables globales

WIDTH,HEIGHT = 600,800
FPS = 60
VENTANA_PRINCIPAL = pygame.display.set_mode((WIDTH,HEIGHT))
WHITE = (255,255,255)

# Funciones para cargar archivos

def up_img(name):

    ruta = path.join("media", name)
    img = pygame.image.load(ruta)

    return img

# Definiendo pantalla principal

pygame.display.set_caption("Artemis")

def draw_main_window():

    VENTANA_PRINCIPAL.fill(WHITE)
    pygame.display.update()

# Módulo principal

def main():

    clock = pygame.time.Clock()
    run = True

    while run:

        clock.tick(FPS)
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                run = False

        draw_main_window()

    pygame.quit()

if __name__ == "__main__":

    main()

