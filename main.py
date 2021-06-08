import pygame
from os import path
from pygame import mouse

from pygame.constants import MOUSEBUTTONDOWN

pygame.init()

# Variables globales

WIDTH, HEIGHT = 600, 800
FPS = 60
VENTANA_PRINCIPAL = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (64, 64, 64)
FUENTE = pygame.font.SysFont("Times New Roman", 25)

# Funciones para cargar archivos


def up_img(name):

    ruta = path.join("assets", name)
    img = pygame.image.load(ruta)

    return img

# Función para crear botones


def draw_button(screen, button, palabra):

    if button.collidepoint(pygame.mouse.get_pos()):

        pygame.draw.rect(screen, GRAY, button, 0)

    else:

        pygame.draw.rect(screen, BLACK, button, 0)

    txt = FUENTE.render(palabra, True, WHITE)
    screen.blit(txt, (button.x+(button.width-txt.get_width())/2,
                button.y+(button.height-txt.get_height())/2))

# Definiendo pantalla principal


pygame.display.set_caption("Artemis")

BACKGROUND = pygame.transform.scale(up_img("background.png"), (WIDTH, HEIGHT))

b_play = pygame.Rect(300-125, 300, 250, 100)


def draw_main_window():

    VENTANA_PRINCIPAL.blit(BACKGROUND, (0, 0))
    draw_button(VENTANA_PRINCIPAL, b_play, "Iniciar Juego")
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

            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                if b_play.collidepoint(mouse.get_pos()):

                    print ("Click")

        draw_main_window()

    pygame.quit()


if __name__ == "__main__":

    main()
