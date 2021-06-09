import pygame as pg
from funciones import draw_button, up_img, WIDTH, HEIGHT, play_song


class Menu(object):
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

			if event.type == pg.locals.MOUSEBUTTONDOWN and event.button == 1:

				if self.b_play.collidepoint(pg.mouse.get_pos()):
					print("Play")

				if self.b_nivel1.collidepoint(pg.mouse.get_pos()):
					print("Nivel 1")

				if self.b_nivel2.collidepoint(pg.mouse.get_pos()):
					print("Nivel 2")

				if self.b_nivel3.collidepoint(pg.mouse.get_pos()):
					print("Nivel 3")
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
