class Menu(object):
	def __init__(self):
		self.score = 0

		self.meteor_list = pygame.sprite.Group()
		self.all_sprites_list = pygame.sprite.Group()


		for i in range(50):
			meteor = Meteor()
			meteor.rect.x = random.randrange(SCREEN_WIDTH)
			meteor.rect.y = random.randrange(SCREEN_HEIGHT)

			self.meteor_list.add(meteor)
			self.all_sprites_list.add(meteor)

		self.player = Player()
		self.all_sprites_list.add(self.player)

	def process_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True

		return False

	def run_logic(self):
		self.all_sprites_list.update()

		meteor_hit_list = pygame.sprite.spritecollide(self.player, self.meteor_list, True)

		for meteor in meteor_hit_list:
			self.score += 1
			print(self.score)

	def display_frame(self, screen):
		screen.fill(WHITE)
		self.all_sprites_list.draw(screen)
		pygame.display.flip()