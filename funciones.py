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
FUENTE = pygame.font.SysFont("Times New Roman", 24)
SCORE = 0
SPEED = 5
text_i = 'Ingrese su Nombre'
name_text = ''
info = ("Costa Rica\nInstituto Tecnológico de Costa Rica" +
        "\nIngeniería en computadores\nTaller de Programación\nGrupo 02\nI Semestre 2021" +
        "\nProf: Milton Villegas Lemus\nVersión: Artemis 1.0\nAutores: " +
        "\nValesska Blanco Montoya & " +
        "\nDarío Gutiérrez Rodríguez")
about = info.split('\n')

player_coords = (0,0)
player_life = 3

# Funciones para cargar archivos

def up_img(name):
    ruta = path.join("assets", name)
    img = pygame.image.load(ruta)

    return img


# Funciones para cargar varias imágenes y animar

def cargarVariasImg(inputx, listaResultado):
    if not inputx:

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

def play_fx():

    fx = pygame.mixer.Sound("assets\\explosion.wav")
    pygame.mixer.Sound.play(fx)

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
    txt = FUENTE.render(text, True, color)
    screen.blit(txt, (x, y))


def draw_text_lines(list_text, color, x, y, screen=VENTANA_PRINCIPAL):
    if not list_text:
        return
    else:
        txt = FUENTE.render(list_text[0], True, color)
        screen.blit(txt, (x, y))
        return draw_text_lines(list_text[1:], color, x, y + 40)


# Función de ordenamiento

def quick_sort(array):
    less = []  # Lista con números menores al pivote
    equal = []  # Lista con números iguales al pivote
    greater = []  # Lista con números mayores al pivote

    if len(array) > 1:  # Condición de Terminación
        pivot = array[0][0]

        # Se realizan las listas
        def do_lists(x):
            if x >= len(array):
                return
            elif array[x][0] < pivot:
                less.append(array[x])
            elif array[x][0] == pivot:
                equal.append(array[x])
            elif array[x][0] > pivot:
                greater.append(array[x])
            x += 1
            do_lists(x)

        do_lists(0)

        # Lamada recursiva final
        return quick_sort(greater) + equal + quick_sort(less)
    else:
        return array


def update_rank():
    file = open("BestScores.artemis", "rt")
    text = file.read()
    file.close()

    rank = 0

    # Create the new entry to Best Scores
    str_score = "0" * (3 - len(str(SCORE))) + str(SCORE)
    new = name_text + " " * (30 - len(name_text)) + str_score + "\n"
    text += new

    # Create the tuples (score, name)
    lines = text.split("\n")  # Split the lines in text
    score_tuples = []

    for line in lines:
        if line:
            score_tuples += [(line[30:], line[:30])]  # Do the tuples

    lines = quick_sort(score_tuples)  # Sort Scores
    text = ""  # Init to do a new text

    if len(lines) > 10:  # Limit the top to 10
        lines = lines[:10]

    # Pre-output process
    for line in lines:
        text += line[1] + line[0] + "\n"  # Transforms the tuples to text
        if line[0] == str_score:
            rank = lines.index(line) + 1  # Player Position

    print(rank)

    file = open("BestScores.artemis", "wt")
    file.write(text)
    file.close()
    return rank
