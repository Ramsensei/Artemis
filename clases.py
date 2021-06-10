import pygame as pg
from pygame.locals import MOUSEBUTTONDOWN
from funciones import draw_button, up_img, WIDTH, HEIGHT, play_song


class Menu(object):
    name = "Menu"
    change = "No"
    b_play = None
    b_nivel1 = None
    b_nivel2 = None
    b_nivel3 = None

    def __init__(self):
        self.BACKGROUND = pg.transform.scale(up_img("background.png"), (WIDTH, HEIGHT))
        self.artemis_img = pg.transform.scale(up_img("artemis.png"), (300, 300))

        self.b_play = pg.Rect(300 - 125, 350, 250, 85)
        self.b_nivel1 = pg.Rect(50, 475, 150, 75)
        self.b_nivel2 = pg.Rect(225, 475, 150, 75)
        self.b_nivel3 = pg.Rect(400, 475, 150, 75)

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
        pg.display.update()


class Game1(object):
    change = "No"
    name = "Game1"
    b_back = None

    def __init__(self):
        self.BACKGROUND = pg.transform.scale(up_img("nebula1.png"), (WIDTH, HEIGHT))

        self.b_back = pg.Rect(450, 0, 150, 75)

        play_song("Avengers.mp3")

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
        draw_button(screen, self.b_back, "Menu")
        pg.display.update()

class Game2(object):
    change = "No"
    name = "Game2"
    b_back = None

    def __init__(self):
        self.BACKGROUND = pg.transform.scale(up_img("nebula2.png"), (WIDTH, HEIGHT))

        self.b_back = pg.Rect(450, 0, 150, 75)

        play_song("Avengers.mp3")

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
        draw_button(screen, self.b_back, "Menu")
        pg.display.update()


class Game3(object):
    change = "No"
    name = "Game3"
    b_back = None

    def __init__(self):
        self.BACKGROUND = pg.transform.scale(up_img("nebula3.png"), (WIDTH, HEIGHT))

        self.b_back = pg.Rect(450, 0, 150, 75)

        play_song("Avengers.mp3")

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
        draw_button(screen, self.b_back, "Menu")
        pg.display.update()