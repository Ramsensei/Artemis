import pygame
import glob
from os import path

pygame.init()

# Variables globales

WIDTH, HEIGHT = 600, 800
FPS = 60
VENTANA_PRINCIPAL = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (64, 64, 64)
FUENTE = pygame.font.SysFont("Times New Roman", 22)
F_TITULO = pygame.font.SysFont("Times New Roman", 28)
SCORE = 0
SPEED = 5
text_i = 'Ingrese su Nombre'
name_text = ''


# Funciones para cargar archivos

def up_img(name):
    ruta = path.join("assets", name)
    img = pygame.image.load(ruta)

    return img


# Funciones para cargar varias imágenes y animar

def cargarVariasImg(inputx, listaResultado):
    if inputx == []:

        return listaResultado

    else:

        listaResultado.append(pygame.image.load(inputx[0]).convert())
        return cargarVariasImg(inputx[1:], listaResultado)


def cargarSprites(patron):
    frames = glob.glob("assets\\sprite\\" + patron)
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


def draw_entry(screen, input_box, text, color):
    pygame.draw.rect(screen, color, input_box, 0)

    txt = FUENTE.render(text, True, BLACK)
    screen.blit(txt, (input_box.x + 5, input_box.y + 15))


def draw_text(text, color, x, y, screen=VENTANA_PRINCIPAL):
    txt = F_TITULO.render(text, True, color)
    screen.blit(txt, (x, y))


# Función de ordenamiento

def quick_sort(array):
    less = []  # Lista con números menores al pivote
    equal = []  # Lista con números iguales al pivote
    greater = []  # Lista con números mayores al pivote

    if len(array) > 1:  # Condición de Terminación
        pivot = array[0]

        # Se realizan las listas
        def do_lists(x):
            if x >= len(array):
                return
            elif array[x] < pivot:
                less.append(array[x])
            elif array[x] == pivot:
                equal.append(array[x])
            elif array[x] > pivot:
                greater.append(array[x])
            x += 1
            do_lists(x)

        do_lists(0)

        return quick_sort(less) + equal + quick_sort(greater)  # Lamada recursiva final
    else:
        return array
