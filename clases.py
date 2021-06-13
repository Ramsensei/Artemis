import pygame as pg
import time
from pygame.locals import MOUSEBUTTONDOWN
import funciones as fc


class Menu(object):
    name = "Menu"
    change = "No"
    b_play = None
    b_nivel1 = None
    b_nivel2 = None
    b_nivel3 = None
    Active = False

    def __init__(self):
        self.Active = False

        self.BACKGROUND = pg.transform.scale(fc.up_img("background.png"), (fc.WIDTH, fc.HEIGHT))
        self.artemis_img = pg.transform.scale(fc.up_img("artemis.png"), (300, 300))

        self.b_play = pg.Rect(300 - 125, 450, 250, 85)
        self.b_nivel1 = pg.Rect(50, 575, 150, 75)
        self.b_nivel2 = pg.Rect(225, 575, 150, 75)
        self.b_nivel3 = pg.Rect(400, 575, 150, 75)

        self.input_box = pg.Rect(100, 370, 400, 50)

        fc.play_song("Avengers.mp3")

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
                    self.Active = True

            if event.type == pg.KEYDOWN:

                if self.Active:

                    if event.key == pg.K_BACKSPACE:
                        fc.name_text = fc.name_text[:-1]

                    else:
                        fc.name_text += event.unicode

        return True

    def run_logic(self):
        pass

    def display_frame(self, screen):
        screen.blit(self.BACKGROUND, (0, 0))
        screen.blit(self.artemis_img, (150, 25))
        fc.draw_button(screen, self.b_play, "Iniciar Juego")
        fc.draw_button(screen, self.b_nivel1, "Nivel 1")
        fc.draw_button(screen, self.b_nivel2, "Nivel 2")
        fc.draw_button(screen, self.b_nivel3, "Nivel 3")

        if self.Active:
            fc.draw_entry(screen, self.input_box, fc.name_text, fc.WHITE)

        else:
            fc.draw_entry(screen, self.input_box, fc.text_i, fc.WHITE)

        pg.display.update()


class Game(object):
    change = "No"
    name = "Game1"
    b_back = None
    player = None
    level = 0
    time_init = 0
    time_end = 0
    background = ["nebula1.png", "nebula2.png", "nebula3.png"]
    songs = ["susp1.mp3", "susp2.mp3", "susp3.mp3"]
    sprite = []

    def __init__(self, level):
        self.BACKGROUND = pg.transform.scale(fc.up_img(self.background[level - 1]), (fc.WIDTH, fc.HEIGHT))

        self.b_back = pg.Rect(450, 0, 150, 75)

        self.time_init = time.time()
        self.level = level
        self.player = Player()

        self.sprites = pg.sprite.Group()
        self.sprites.add(self.player)

        fc.play_song(self.songs[level - 1])

    def process_events(self):
        for event in pg.event.get():

            if event.type == pg.QUIT:
                return False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.player.speedx -= 3
                if event.key == pg.K_RIGHT:
                    self.player.speedx += 3
                if event.key == pg.K_UP:
                    self.player.speedy -= 3
                if event.key == pg.K_DOWN:
                    self.player.speedy += 3

            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    self.player.speedx += 3
                if event.key == pg.K_RIGHT:
                    self.player.speedx -= 3
                if event.key == pg.K_UP:
                    self.player.speedy += 3
                if event.key == pg.K_DOWN:
                    self.player.speedy -= 3

            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                if self.b_back.collidepoint(pg.mouse.get_pos()):
                    self.change = "Menu"
        return True

    def run_logic(self):
        self.sprites.update()
        self.time_end = time.time()
        if self.time_end - self.time_init >= 1:
            self.time_init = time.time()
            fc.SCORE += 1

    def display_frame(self, screen):
        screen.blit(self.BACKGROUND, (0, 0))
        fc.draw_button(screen, self.b_back, "Menu")
        self.player.next_frame()
        self.sprites.draw(screen)
        pg.display.update()


class Player(pg.sprite.Sprite):
    frame = [0, True]
    image_list = []
    speedx = 0
    speedy = 0

    def __init__(self):
        super().__init__()
        self.image_list = fc.cargarSprites("tile*.png")
        self.image = self.image_list[self.frame[0]]
        self.image.set_colorkey(fc.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 240
        self.rect.y = 500

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 461:
            self.rect.x = 461
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 684:
            self.rect.y = 684

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
