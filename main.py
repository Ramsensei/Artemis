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
GRAY = (64,64,64)
FUENTE = pygame.font.SysFont("Times New Roman", 22)

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
artemis_img = pygame.transform.scale(up_img("artemis.png"), (300,300))

b_play = pygame.Rect(300-125, 350, 250, 85)
b_nivel1 = pygame.Rect(50,475,150,75)
b_nivel2 = pygame.Rect(225,475,150,75)
b_nivel3 = pygame.Rect(400,475,150,75)

def draw_main_window():

    VENTANA_PRINCIPAL.blit(BACKGROUND, (0, 0))
    VENTANA_PRINCIPAL.blit(artemis_img,(150,25))
    draw_button(VENTANA_PRINCIPAL, b_play, "Iniciar Juego")
    draw_button(VENTANA_PRINCIPAL, b_nivel1, "Nivel 1")
    draw_button(VENTANA_PRINCIPAL, b_nivel2, "Nivel 2")
    draw_button(VENTANA_PRINCIPAL, b_nivel3, "Nivel 3")
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

                    print ("Play")

                if b_nivel1.collidepoint(mouse.get_pos()):

                    print ("Nivel 1")
                
                if b_nivel2.collidepoint(mouse.get_pos()):

                    print ("Nivel 2")
                
                if b_nivel3.collidepoint(mouse.get_pos()):

                    print ("Nivel 3")

        draw_main_window()

    pygame.quit()


if __name__ == "__main__":

    main()
