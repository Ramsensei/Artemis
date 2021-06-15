import pygame
import glob
from os import path

# Inicializando pygame

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

# Variables para almacenar el nombre del jugador

text_i = 'Ingrese Su Nombre'
name_text = ''

# Variables que contienen el texto de  about

info = ("Costa Rica\nInstituto Tecnológico de Costa Rica" +
        "\nIngeniería en computadores\nTaller de Programación\nGrupo 02\nI Semestre 2021" +
        "\nProf: Milton Villegas Lemus\nVersión: Artemis 1.0\nAutores: " +
        "\nValesska Blanco Montoya & " +
        "\nDarío Gutiérrez Rodríguez")
about = info.split('\n') # Línea para hacer saltos de línea cada que haya un '\n'

# Información relacionada al jugador

player_coords = (240, 500)
player_life = 3
posicion = 0


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

    # Cambiando de color si el mouse está encima del botón

    if button.collidepoint(pygame.mouse.get_pos()):

        pygame.draw.rect(screen, GRAY, button, 0)

    else: # Color por default del botón

        pygame.draw.rect(screen, BLACK, button, 0)

    txt = FUENTE.render(palabra, True, WHITE)
    screen.blit(txt, (button.x + (button.width - txt.get_width()) / 2,
                      button.y + (button.height - txt.get_height()) / 2))


#Función para crear la entrada de texto

def draw_entry(screen, input_box, text, color):
    pygame.draw.rect(screen, color, input_box, 0)

    txt = FUENTE.render(text, True, BLACK)
    screen.blit(txt, (input_box.x + 5, input_box.y + 15))

# Función para escribir texto en pantalla, cuando sea necesario

def draw_text(text, color, x, y, screen=VENTANA_PRINCIPAL):
    txt = FUENTE.render(text, True, color)
    screen.blit(txt, (x, y))

# Función para imprimir una lista que contiene strings separados por línea

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

# Función para actualizar los scores

def update_rank():

    global posicion

    file = open("BestScores.artemis", "rt")
    text = file.read()
    file.close()

    rank = 0

    # Creando la nueva entrada de mejores puntajes
    str_score = "0" * (3 - len(str(SCORE))) + str(SCORE)
    new = name_text + " " * (30 - len(name_text)) + str_score + "\n"
    text += new

    # Creando las tuplas (score, name)
    lines = text.split("\n")  # Dividiendo las líneas
    score_tuples = []

    for line in lines:
        if line:
            score_tuples += [(line[30:], line[:30])]  

    lines = quick_sort(score_tuples)  # Ordenamiento de los puntajes
    text = ""  # Creando un nuevo texto

    if len(lines) > 10:  # Límite de 1 líneas
        lines = lines[:10]

    # Pre-output process
    for line in lines:
        text += line[1] + line[0] + "\n"  # Transformando las tuplas a texto
        if line[0] == str_score:
            rank = lines.index(line) + 1  # Posición del jugador

    posicion = rank

    file = open("BestScores.artemis", "wt")
    file.write(text)
    file.close()
    return rank
