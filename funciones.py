import pygame
import sys
import glob
from os import path

pygame.init()

pygame.init()

# Variables globales

WIDTH, HEIGHT = 600, 800
FPS = 60
VENTANA_PRINCIPAL = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (64, 64, 64)
FUENTE = pygame.font.SysFont("Times New Roman", 22)
SPEED = 5


# Funciones para cargar archivos

def up_img(name):
    ruta = path.join("assets", name)
    img = pygame.image.load(ruta)

    return img

# Funciones para cargar varias imágenes y animar

def cargarVariasImg(inputx, listaResultado):

    if(inputx == []):

        return listaResultado

    else:

        listaResultado.append(pygame.image.load(inputx[0]))
        return cargarVariasImg(inputx[1:], listaResultado)


def cargarSprites(patron):

    frames = glob.glob("assets\\sprite\\"+patron)
    frames.sort()
    return cargarVariasImg(frames, [])


# Funciones de reproducción de sonido

pygame.mixer.init()


def load_MP3(nombre):
    return path.join("assets", nombre)


def play_song(MP3):
    stop_song()

    pygame.mixer.music.load(load_MP3(MP3))
    pygame.mixer.music.play(-1)


def stop_song():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()


# Función para crear botones


def draw_button(screen, button, palabra):
    if button.collidepoint(pygame.mouse.get_pos()):

        pygame.draw.rect(screen, GRAY, button, 0)

    else:

        pygame.draw.rect(screen, BLACK, button, 0)

    txt = FUENTE.render(palabra, True, WHITE)
    screen.blit(txt, (button.x + (button.width - txt.get_width()) / 2,
                      button.y + (button.height - txt.get_height()) / 2))


