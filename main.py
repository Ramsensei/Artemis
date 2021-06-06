import pygame

pygame.init()

# Variables globales

WIDTH,HEIGHT = 600,800
FPS = 60
VENTANA_PRINCIPAL = pygame.display.set_mode((WIDTH,HEIGHT))

# Definiendo pantalla principal

def main():

    run = True

    while run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                run = False

if __name__ == "__main__":
    
    main()

