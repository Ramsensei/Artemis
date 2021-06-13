import pygame as pg
from pygame.locals import MOUSEBUTTONDOWN
from funciones import *

text_i = 'Ingrese su Nombre'
name_text = ''

ACTIVE = False


class Menu(object):
    name = "Menu"
    change = "No"
    b_play = None
    b_nivel1 = None
    b_nivel2 = None
    b_nivel3 = None

    def __init__(self):
        global ACTIVE, name_text
        ACTIVE = False
        name_text = ''

        self.BACKGROUND = pg.transform.scale(up_img("background.png"), (WIDTH, HEIGHT))
        self.artemis_img = pg.transform.scale(up_img("artemis.png"), (300, 300))

        self.b_play = pg.Rect(300 - 125, 450, 250, 85)
        self.b_nivel1 = pg.Rect(50, 575, 150, 75)
        self.b_nivel2 = pg.Rect(225, 575, 150, 75)
        self.b_nivel3 = pg.Rect(400, 575, 150, 75)

        self.input_box = pg.Rect(100, 370, 400, 50)

        play_song("Avengers.mp3")

    def process_events(self):

        for event in pg.event.get():

            if event.type == pg.QUIT:
                return False

            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                if self.b_play.collidepoint(pg.mouse.get_pos()):
                    self.change = "Game1"

                if self.b_nivel1.collidepoint(pg.mouse.get_pos()):
                    self.change = "Game1"

                if self.b_nivel2.collidepoint(pg.mouse.get_pos()):
                    self.change = "Game2"

                if self.b_nivel3.collidepoint(pg.mouse.get_pos()):
                    self.change = "Game3"

                if self.input_box.collidepoint(event.pos):
                    ACTIVE = True

            if event.type == pg.KEYDOWN:

                if ACTIVE:

                    if event.key == pg.K_BACKSPACE:
                        name_text = name_text[:-1]

                    else:
                        name_text += event.unicode

        return True

    def run_logic(self):
        pass

    def display_frame(self, screen):
        screen.blit(self.BACKGROUND, (0, 0))
        screen.blit(self.artemis_img, (150, 25))
        draw_button(screen, self.b_play, "Iniciar Juego")
        draw_button(screen, self.b_nivel1, "Nivel 1")
        draw_button(screen, self.b_nivel2, "Nivel 2")
        draw_button(screen, self.b_nivel3, "Nivel 3")

        if ACTIVE:
            draw_entry(screen, self.input_box, name_text, WHITE)

        else:
            draw_entry(screen, self.input_box, text_i, WHITE)

        pg.display.update()


class Game(object):
    change = "No"
    name = "Game1"
    b_back = None
    player = None
    background = ["nebula1.png", "nebula2.png", "nebula3.png"]
    songs = ["susp1.mp3", "susp2.mp3", "susp3.mp3"]
    sprite = []

    def __init__(self, level):
        self.BACKGROUND = pg.transform.scale(up_img(self.background[level - 1]), (WIDTH, HEIGHT))
        self.sprites = pygame.sprite.Group()
        self.b_back = pg.Rect(450, 0, 150, 75)
        self.player = Player()
        self.sprites.add(self.player)
        play_song(self.songs[level - 1])

    def process_events(self):
        for event in pg.event.get():

            if event.type == pg.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.speed = -3
                if event.key == pygame.K_RIGHT:
                    self.player.speed = 3

            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                if self.b_back.collidepoint(pg.mouse.get_pos()):
                    self.change = "Menu"
        return True

    def run_logic(self):
        self.sprites.update()

    def display_frame(self, screen):
        screen.blit(self.BACKGROUND, (0, 0))
        draw_button(screen, self.b_back, "Menu")
        self.player.next_frame()
        self.sprites.draw(screen)
        pg.display.update()


class Player(pygame.sprite.Sprite):
    frame = [0, True]
    image_list = []
    speed = 0

    def __init__(self):
        super().__init__()
        self.image_list = cargarSprites("tile*.png")
        self.image = self.image_list[self.frame[0]]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 240
        self.rect.y = 500

    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 461:
            self.rect.x = 461

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
        self.image.set_colorkey(BLACK)
