import pygame as pg
import time
import random
from pygame.locals import MOUSEBUTTONDOWN
import funciones as fc


# Clase del Menu Principal
class Menu(object):
    """
    ********************************************
    Instituto Tecnológico de Costa Rica
    Ing. Computadores
    Lenguaje: Python 3.9.3
    Versión 1.8
    Fecha Última Modificación: 12/06/2021
    Módulo: Menú Principal
    Descripción: Este módulo contiene las funciones
    referentes a manejo de selección de niveles, entrada
    de texto, música de fondo y acceso a otras pantallas
    Autores: Valesska Blanco M & Ramsés Gutiérrez R
    ********************************************
    """

    # Propiedades de la clase
    name = "Menu"
    change = "No"
    # Inicializando los espacios de memoria necesarios
    b_play = None
    b_nivel1 = None
    b_nivel2 = None
    b_nivel3 = None
    b_about = None
    b_top = None
    input_box = None
    Active = False

    # Módulo __init__

    def __init__(self):

        # Se escribe la variable Active como False para desactivar el entry
        self.Active = False

        # Se restaura el puntaje a 0
        fc.SCORE = 0

        # Carga de imágenes
        self.BACKGROUND = pg.transform.scale(fc.up_img("background.png"), (fc.WIDTH, fc.HEIGHT))
        self.artemis_img = pg.transform.scale(fc.up_img("artemis.png"), (300, 300))

        # Rectángulos que corresponden a los botones
        self.b_play = pg.Rect(300 - 125, 450, 250, 85)
        self.b_nivel1 = pg.Rect(50, 575, 150, 75)
        self.b_nivel2 = pg.Rect(225, 575, 150, 75)
        self.b_nivel3 = pg.Rect(400, 575, 150, 75)
        self.b_about = pg.Rect(150, 675, 150, 75)
        self.b_top = pg.Rect(325, 675, 150, 75)

        # Rectángulo de entry
        self.input_box = pg.Rect(100, 370, 400, 50)

        # Play music
        fc.play_song("Avengers.mp3")

    # Método que procesa los eventos

    def process_events(self):

        for event in pg.event.get():

            # Condición de terminación de la pantalla
            if event.type == pg.QUIT:
                return False

            # Si hace click en...
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                # Botón de iniciar juego
                if self.b_play.collidepoint(pg.mouse.get_pos()):
                    self.change = "Game1"  # Cambio de pantalla
                    if not fc.name_text:  # Si no se introdujo un nombre
                        fc.name_text = "Anonymous"  # Default name

                # Botón de nivel 1
                if self.b_nivel1.collidepoint(pg.mouse.get_pos()):
                    self.change = "Game1"
                    if not fc.name_text:
                        fc.name_text = "Anonymous"  # Default name  

                # Botón de nivel 2
                if self.b_nivel2.collidepoint(pg.mouse.get_pos()):
                    self.change = "Game2"
                    if not fc.name_text:
                        fc.name_text = "Anonymous"  # Default name

                # Botón de nivel 3
                if self.b_nivel3.collidepoint(pg.mouse.get_pos()):
                    self.change = "Game3"
                    if not fc.name_text:
                        fc.name_text = "Anonymous"  # Default name

                # Botón de Top 10
                if self.b_top.collidepoint(pg.mouse.get_pos()):
                    self.change = "Top"

                # Botón de About
                if self.b_about.collidepoint(pg.mouse.get_pos()):
                    self.change = "About"

                # Input box
                if self.input_box.collidepoint(event.pos):
                    self.Active = True  # se activa la escritura en input box

            # Detectando las presiones de teclas
            if event.type == pg.KEYDOWN:

                # Si el input box está activo
                if self.Active:

                    # Para borrar
                    if event.key == pg.K_BACKSPACE:
                        fc.name_text = fc.name_text[:-1]

                    # Escribiendo lo que el teclado envie en inputbox
                    else:
                        fc.name_text += event.unicode

        return True

    def run_logic(self):
        pass

    # Método de dibujar en pantalla
    def display_frame(self, screen):

        # Imagen de fondo y artemis
        screen.blit(self.BACKGROUND, (0, 0))
        screen.blit(self.artemis_img, (150, 25))

        # Dibujando botones
        fc.draw_button(screen, self.b_play, "Iniciar Juego")
        fc.draw_button(screen, self.b_nivel1, "Nivel 1")
        fc.draw_button(screen, self.b_nivel2, "Nivel 2")
        fc.draw_button(screen, self.b_nivel3, "Nivel 3")
        fc.draw_button(screen, self.b_about, "About")
        fc.draw_button(screen, self.b_top, "Top 10")

        # Dibujando el entry
        if self.Active:
            fc.draw_entry(screen, self.input_box, fc.name_text, fc.WHITE)

        else:
            fc.draw_entry(screen, self.input_box, fc.text_i, fc.WHITE)

        # Actualizando el display
        pg.display.update()


# Clase de Pantalla About
class About(object):
    """
    ********************************************
    Instituto Tecnológico de Costa Rica
    Ing. Computadores
    Lenguaje: Python 3.9.3
    Versión 1.8
    Fecha Última Modificación: 12/06/2021
    Módulo: Pantalla About
    Descripción: Este módulo muestra la información
    complementaria del juego, así como los créditos
    del mismo.
    Autores: Valesska Blanco M & Ramsés Gutiérrez R
    ********************************************
    """

    change = "No"
    name = "About"
    b_back = None

    def __init__(self):

        self.BACKGROUND = pg.transform.scale(fc.up_img("background.png"), (fc.WIDTH, fc.HEIGHT))
        self.VALESSKA = pg.transform.scale(fc.up_img("valesska.png"), (200, 200))
        self.RAM = pg.transform.scale(fc.up_img("ram.png"), (200, 200))
        self.b_back = pg.Rect(450, 0, 150, 75)

        fc.play_song("Avengers.mp3")

    def process_events(self):
        for event in pg.event.get():

            if event.type == pg.QUIT:
                return False

            # Botón de regreso al menú principal
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                if self.b_back.collidepoint(pg.mouse.get_pos()):
                    self.change = "Menu"

        return True

    def run_logic(self):
        pass

    def display_frame(self, screen):

        screen.blit(self.BACKGROUND, (0, 0))
        screen.blit(self.VALESSKA, (80, 550))
        screen.blit(self.RAM, (300, 550))
        fc.draw_button(screen, self.b_back, "Menu")

        # Escribiendo la información de about
        fc.draw_text_lines(fc.about, fc.WHITE, 70, 100)
        pg.display.update()


# Clase de Pantalla de Mejores Puntajes
class Top(object):
    '''
    ********************************************
    Instituto Tecnológico de Costa Rica
    Ing. Computadores
    Lenguaje: Python 3.9.3
    Versión 1.8
    Fecha Última Modificación: 12/06/2021
    Módulo: Pantalla Top 10
    Descripción: Este módulo muestra la información
    sobre los 10 mejores puntajes obtenidos de mayor a 
    menor con el nombre del jugador respectivo
    Autores: Valesska Blanco M & Ramsés Gutiérrez R
    ********************************************
    '''

    # Propiedades
    change = "No"
    name = "Top"
    b_back = None
    b_puntaje = None
    b_nombre = None

    def __init__(self):

        self.BACKGROUND = pg.transform.scale(fc.up_img("background.png"), (fc.WIDTH, fc.HEIGHT))
        self.b_back = pg.Rect(450, 0, 150, 75)
        self.b_nombre = pg.Rect(100, 650, 150, 75)
        self.b_puntaje = pg.Rect(300, 650, 150, 75)

        fc.play_song("Avengers.mp3")

    def process_events(self):
        for event in pg.event.get():

            if event.type == pg.QUIT:
                return False

            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                if self.b_back.collidepoint(pg.mouse.get_pos()):
                    self.change = "Menu"

                if self.b_nombre.collidepoint(pg.mouse.get_pos()):
                    print("Ordenando por nombre (Insertion)")

                if self.b_puntaje.collidepoint(pg.mouse.get_pos()):
                    print("Ordenando por nombre (QuickSort)")

        return True

    def run_logic(self):
        pass

    def display_frame(self, screen):

        screen.blit(self.BACKGROUND, (0, 0))
        fc.draw_button(screen, self.b_back, "Menu")
        fc.draw_button(screen, self.b_nombre, "Nombre")
        fc.draw_button(screen, self.b_puntaje, "Puntaje")

        # Abriendo y escribiendo el archivo de mejores puntajes
        with open("BestScores.artemis", "r") as file:
            lista_top10 = file.readlines()

        fc.draw_text("Top 10", fc.WHITE, 70, 50)
        fc.draw_text("Ordenar los puntajes por:", fc.WHITE, 150, 600)
        fc.draw_text_lines(lista_top10, fc.WHITE, 70, 150)
        pg.display.update()


# Clase de Pantalla de GameOver
class GameOver(object):
    """
    ********************************************
    Instituto Tecnológico de Costa Rica
    Ing. Computadores
    Lenguaje: Python 3.9.3
    Versión 1.8
    Fecha Última Modificación: 12/06/2021
    Módulo: Pantalla GameOver
    Descripción: Este módulo se muestra cuando finaliza
    el juego, en cualquier nivel, mostrando el puntaje
    obtenido, la posición en el ranking (si la hay) y
    da la opción de regresar al menú principal.
    Autores: Valesska Blanco M & Ramsés Gutiérrez R
    ********************************************
    """

    change = "No"
    name = "GameOver"
    b_back = None

    def __init__(self):

        self.BACKGROUND = pg.transform.scale(fc.up_img("background.png"), (fc.WIDTH, fc.HEIGHT))
        self.b_back = pg.Rect(450, 0, 150, 75)

        # Cada vez que se abre la pantalla se actualiza el top 10
        fc.update_rank()
        fc.play_song("Avengers.mp3")

    def process_events(self):
        for event in pg.event.get():

            if event.type == pg.QUIT:
                return False

            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                if self.b_back.collidepoint(pg.mouse.get_pos()):
                    self.change = "Menu"

        return True

    def run_logic(self):
        pass

    def display_frame(self, screen):

        screen.blit(self.BACKGROUND, (0, 0))
        fc.draw_button(screen, self.b_back, "Menu")
        fc.draw_text("Ha finalizado el juego", fc.WHITE, 190, 350)

        # Escribiendo el puntaje y posición obtenida (en caso de existir)
        fc.draw_text("Su puntaje es de: {x}".format(x=fc.SCORE), fc.WHITE, 190, 400)
        if fc.posicion != 0:
            fc.draw_text("Obtuvo la posición #" + str(fc.posicion) +
                         " en el Top 10", fc.WHITE, 140, 450)
        else:
            fc.draw_text("No entró en el top 10", fc.WHITE, 195, 450)
        pg.display.update()


# Clase de Pantalla de Juego
class Game(object):
    """
    ********************************************
    Instituto Tecnológico de Costa Rica
    Ing. Computadores
    Lenguaje: Python 3.9.3
    Versión 1.8
    Fecha Última Modificación: 12/06/2021
    Módulo: Pantalla de Juego
    Descripción: Este módulo maneja el comportamiento
    de cada uno de los niveles, desde su música de fondo
    y background hasta el puntaje obtenido en cada nivel por
    tiempo transcurrido. Además, muestra la información
    relevante al desarrollo del juego y controla las condiciones
    de cambio de pantalla entre niveles, pérdida y gane del juego.
    Autores: Valesska Blanco M & Ramsés Gutiérrez R
    ********************************************
    """

    # Propiedades
    change = "No"
    name = "Game"

    # Espacios de memoria
    b_back = None
    player = None
    meteorito = None
    level = 0
    time_init = 0
    time_score = 0
    timer = 0
    background = ["nebula1.png", "nebula2.png", "nebula3.png"]
    songs = ["susp1.mp3", "susp2.mp3", "susp3.mp3"]
    sprites = []
    plySpeed = 0
    key_pressed = [False, False, False, False]

    def __init__(self, level):
        self.BACKGROUND = pg.transform.scale(fc.up_img(self.background[level - 1]), (fc.WIDTH, fc.HEIGHT))

        self.b_back = pg.Rect(450, 0, 150, 75)

        # Asignando valores a las variables
        self.time_init = time.time()  # tiempo inicial
        self.level = level  # nivel que se va a desplegar
        self.player = Player()
        self.plySpeed = 5
        self.player.speedx = 0
        self.player.speedy = 0
        self.key_pressed = [False, False, False, False]

        # Grupos de Sprites
        self.sprites = pg.sprite.Group()
        self.sprites.add(self.player)
        self.meteoritos = pg.sprite.Group()

        # Cantidad de meteoritos por nivel
        for x in range(level + 3):
            self.meteorito = Meteoritos()
            self.meteoritos.add(self.meteorito)

        fc.play_song(self.songs[level - 1])

        # Restaurando la vida del jugador
        fc.player_life = 3

    def process_events(self):
        for event in pg.event.get():

            if event.type == pg.QUIT:
                return False

            # Movimiento del jugador
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.player.speedx -= self.plySpeed
                    self.key_pressed[0] = True
                if event.key == pg.K_RIGHT:
                    self.player.speedx += self.plySpeed
                    self.key_pressed[1] = True
                if event.key == pg.K_UP:
                    self.player.speedy -= self.plySpeed
                    self.key_pressed[2] = True
                if event.key == pg.K_DOWN:
                    self.player.speedy += self.plySpeed
                    self.key_pressed[3] = True

            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT and self.key_pressed[0]:
                    self.player.speedx += self.plySpeed
                if event.key == pg.K_RIGHT and self.key_pressed[1]:
                    self.player.speedx -= self.plySpeed
                if event.key == pg.K_UP and self.key_pressed[2]:
                    self.player.speedy += self.plySpeed
                if event.key == pg.K_DOWN and self.key_pressed[3]:
                    self.player.speedy -= self.plySpeed

            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                if self.b_back.collidepoint(pg.mouse.get_pos()):
                    self.change = "Menu"
                    # Actualizando el ranking
                    fc.update_rank()
        return True

    def run_logic(self):

        # Actualizando los sprites a 60FPS
        self.sprites.update()
        self.meteoritos.update()
        self.timer = time.time()  # toma de tiempo

        # Puntaje por nivel
        if self.timer - self.time_score >= 1:
            self.time_score = time.time()
            if self.level == 1:
                fc.SCORE += 1
            if self.level == 2:
                fc.SCORE += 3
            if self.level == 3:
                fc.SCORE += 5

        # Finalización del nivel a los 60s
        if self.timer - self.time_init >= 30:
            if self.level == 1:
                self.change = "Game2"
            if self.level == 2:
                self.change = "Game3"
            if self.level == 3:
                fc.update_rank()
                self.change = "GameOver"

        # Finalizando el juego cuando el jugador pierde todas sus vidas
        elif fc.player_life <= 0 and self.level == 3:
            fc.update_rank()
            self.change = "GameOver"

        elif fc.player_life <= 0 and (self.level == 1 or self.level == 2):
            self.change = "GameOver"

    def display_frame(self, screen):

        screen.blit(self.BACKGROUND, (0, 0))
        fc.draw_button(screen, self.b_back, "Menu")

        # Informacón en pantalla
        fc.draw_text("Score: " + str(fc.SCORE), fc.WHITE, 10, 30)
        fc.draw_text("Jugador: " + fc.name_text, fc.WHITE, 140, 30)
        fc.draw_text("Vida: " + str(fc.player_life), fc.WHITE, 350, 30)
        elapsed_time = int(time.time() - self.time_init)
        fc.draw_text("Tiempo: " + str(elapsed_time), fc.WHITE, 10, 750)

        # Dibujando los sprites
        self.player.next_frame()
        self.sprites.draw(screen)
        self.meteoritos.draw(screen)
        pg.display.update()


# Clase del
class Player(pg.sprite.Sprite):
    '''
    ********************************************
    Instituto Tecnológico de Costa Rica
    Ing. Computadores
    Lenguaje: Python 3.9.3
    Versión 1.8
    Fecha Última Modificación: 12/06/2021
    Módulo: Pantalla de Juego
    Descripción: Este módulo maneja el comportamiento
    completo del jugador, desde su movimiento con las flechas
    así como su animación mediante sprites.
    Autores: Valesska Blanco M & Ramsés Gutiérrez R
    ********************************************
    '''

    frame = [0, True]
    rect = None
    image_list = []
    speedx = 0
    speedy = 0

    def __init__(self):
        super().__init__()

        # Cargando las imágenes del sprite
        self.image_list = fc.cargarSprites("tile*.png")
        self.image = self.image_list[self.frame[0]]
        self.image.set_colorkey(fc.BLACK)
        self.rect = self.image.get_rect()
        self.speedx, self.speedy = 0, 0
        self.rect.x, self.rect.y = 240, 500

    # Método de actualización del jugador y su movimiento
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 600 - self.rect.width:
            self.rect.x = 600 - self.rect.width
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 800 - self.rect.height:
            self.rect.y = 800 - self.rect.height
        fc.player_coords = (self.rect.x, self.rect.y)

    # Recorrido de los frames del sprite para animar
    def next_frame(self):
        if self.frame[1]:
            self.frame[0] += 1
        else:
            self.frame[0] -= 1
        if self.frame[0] > 29:
            self.frame[0] = 29
            self.frame[1] = False
        if self.frame[0] < 0:
            self.frame[0] = 0
            self.frame[1] = True
        self.image = self.image_list[self.frame[0]]
        self.image.set_colorkey(fc.BLACK)


# Clase de Meteoritos
class Meteoritos(pg.sprite.Sprite):
    """
    ********************************************
    Instituto Tecnológico de Costa Rica
    Ing. Computadores
    Lenguaje: Python 3.9.3
    Versión 1.8
    Fecha Última Modificación: 12/06/2021
    Módulo: Pantalla de Juego
    Descripción: Este módulo maneja el comportamiento
    completo de los meteoritos, cada vez que se llama
    genera un meteorito nuevo con un movimiento relativamente
    aleatorio y velocidades aleatorias. También detecta
    las colisiones entre él mismo y el jugador, baja la
    vida del jugador y se autodestruye.
    Autores: Valesska Blanco M & Ramsés Gutiérrez R
    ********************************************
    """

    speed = (4, 4)
    speedrange = (1, 7)
    medium = 50
    movx = True
    movy = True

    def __init__(self):

        super().__init__()

        self.image = pg.transform.scale(fc.up_img("meteorito.png"), (self.medium, self.medium))
        self.image.set_colorkey(fc.BLACK)
        self.radius = 25
        self.rect = self.image.get_rect()

        # Componentes vertical y horizontal
        self.rect.x = random.choice([-100, 700])
        self.rect.y = random.randrange(600)

        # Velocidad variable
        self.speed = random.randrange(self.speedrange[0], self.speedrange[1]), random.randrange(self.speedrange[0],
                                                                                                self.speedrange[1])

    def update(self):

        # Detección de la colisión entre el jugador y el meteorito
        if (self.rect.x < fc.player_coords[0] + 85
                and self.rect.x + self.rect.width > fc.player_coords[0]
                and self.rect.y < fc.player_coords[1] + 80
                and self.rect.y + self.rect.height > fc.player_coords[1]):
            fc.player_life -= 1
            fc.play_fx()
            self.kill()  # desaparece el meteorito
            return

        if self.movx and (self.rect.x + (2 * self.radius) >= fc.WIDTH):
            self.movx = False
            self.speed = random.randrange(self.speedrange[0], self.speedrange[1]), random.randrange(self.speedrange[0],
                                                                                                    self.speedrange[1])
            fc.play_fx()

        if not self.movx and (self.rect.x <= 0):
            self.movx = True
            self.speed = random.randrange(self.speedrange[0], self.speedrange[1]), random.randrange(self.speedrange[0],
                                                                                                    self.speedrange[1])
            fc.play_fx()

        if self.movy and (self.rect.y + (2 * self.radius) >= fc.HEIGHT):
            self.movy = False
            self.speed = random.randrange(self.speedrange[0], self.speedrange[1]), random.randrange(self.speedrange[0],
                                                                                                    self.speedrange[1])
            fc.play_fx()

        if not self.movy and (self.rect.y <= 0):
            self.movy = True
            self.speed = random.randrange(self.speedrange[0], self.speedrange[1]), random.randrange(self.speedrange[0],
                                                                                                    self.speedrange[1])
            fc.play_fx()

        # Movimiento de los meteoritos
        if self.movx:
            self.rect.x += self.speed[0]

        elif not self.movx:
            self.rect.x -= self.speed[0]

        if self.movy:
            self.rect.y += self.speed[1]

        elif not self.movy:
            self.rect.y -= self.speed[1]
