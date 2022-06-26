# Importing all the essential python libraries

import pygame
pygame.init()
from pygame import *
import time
import random
init()
pygame.font.init()
import pygame.freetype
pygame.freetype.init()

# Parent Bird Class

class GameSprite(sprite.Sprite):

	# Getting all the changable variables link to the bird

	def __init__(self,player_image,player_x,player_y,player_size,player_speed,player_jump):
		sprite.Sprite.__init__(self)
		self.image = transform.scale(image.load(player_image),(player_size,player_size))
		self.player_size = player_size

		self.player_speed = player_speed
		self.rect = self.image.get_rect()
		self.rect.y = player_y
		self.rect.x = player_x
		self.velocity_x = 0
		self.velocity_y = 13
		self.player_jump = player_jump
		self.image_copy = transform.scale(image.load(player_image),(player_size,player_size))

	# Printing the Bird to the screen

	def reset(self):
		window.blit(self.image_copy, (self.rect.x - int(self.image_copy.get_width() / 2), self.rect.y - int(self.image_copy.get_height() / 2)))

# Sub Bird Class

class Player(GameSprite):

	# Player movement function

	def update(self):

		# Bring in all the global varibles we would like to change

		global event

		# Checking if a button has been pressed

		for event in pygame.event.get():
			if(event.type == KEYDOWN):

				# If space is pushed down

				if(event.key == K_SPACE):
					self.velocity_y = self.player_jump

		self.velocity_y += self.player_speed
		self.rect.y -= self.velocity_y
		self.image_copy = transform.rotate(self.image, self.velocity_y * 2)

	def hit_box_location(self):
		self.rect.x = bird_sprite.rect.x - int(self.image_copy.get_width() / 2)
		self.rect.y = bird_sprite.rect.y - int(self.image_copy.get_height() / 2)


# Green Pipe Class

class Green_Pipe():

	def __init__(self,pipe_image,pipe_x,pipe_y,pipe_speed,pipe_width,pipe_length,pipe_top,gap):

		sprite.Sprite.__init__(self)
		self.image = transform.scale(image.load(pipe_image),(pipe_width,pipe_length))

		self.rect = self.image.get_rect()
		self.rect.y = pipe_y
		self.rect.x = pipe_x
		self.pipe_speed = pipe_speed
		self.pipe_length = pipe_length
		self.pipe_top = pipe_top
		self.gap = gap

	def reset(self):
		window.blit(self.image,(self.rect.x,self.rect.y))

	def update(self):
		global random_location
		global game_score
		self.rect.x -= self.pipe_speed
		if self.rect.x <= -150:
			self.rect.x = 800
			if self.pipe_top == True:
				random_location = random.randint(250,450)
				self.rect.y = random_location - self.gap - self.pipe_length
			else:
				self.rect.y = random_location
		
		if self.rect.x <= 400 and self.rect.x >= 397:
			game_score += 0.5

# Creates an image

class Image():

	# Initializing all the important stuff

	def __init__(self,background_image,background_x,background_y,background_width,background_height):

		sprite.Sprite.__init__(self)
		self.image = transform.scale(image.load(background_image),(background_width,background_height))

		self.rect = self.image.get_rect()
		self.rect.y = background_x
		self.rect.x = background_y

		self.background_x = background_x
		self.background_y = background_y

	# Printing the image onto the screen

	def create_image(self):
		window.blit(self.image,(self.background_x,self.background_y))

# Creates an image

class Moving_Image():

	# Initializing all the important stuff

	def __init__(self,background_image,background_x,background_y,background_width,background_height, movement_speed, reset_distance):

		sprite.Sprite.__init__(self)
		self.image = transform.scale(image.load(background_image),(background_width,background_height))

		self.rect = self.image.get_rect()
		self.rect.y = background_x
		self.rect.x = background_y
		self.movement_speed = movement_speed
		self.reset_distance = reset_distance

		self.background_x = background_x
		self.background_y = background_y

	# Printing the image onto the screen

	def create_image(self):
		window.blit(self.image,(self.background_x,self.background_y))

	def update(self):
		self.background_x -= self.movement_speed
		if self.reset_distance >= self.background_x:
			self.background_x = 0

# Class for text

class Phrase():

	# Initializing all the important stuff

	def __init__(self,color1,color2,color3,font_type,text,x_pos,y_pos,font_size):
		self.color1 = color1
		self.color2 = color2
		self.color3 = color3
		self.font_type = font_type
		self.text = text
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.font_size = font_size

		self.final_font = pygame.freetype.Font(self.font_type,self.font_size)

	# Drawing the text to the screen

	def draw_text(self):

		self.final_font.render_to(window, (self.x_pos,self.y_pos),self.text,(self.color1,self.color2,self.color3))

# Button Class

class Button():

	# Initializing all the important stuff

	def __init__(self,picture,xLoc,yLoc,width,length):

		self.picture = picture
		self.image = transform.scale(image.load(picture),(width,length))
		self.xLoc = xLoc
		self.yLoc = yLoc
		self.width = width
		self.length = length

	# Checking if the button has been pressed

	def button_press(self,e):

		# If the cordinates of the button press is inside of the area of the button

		if e.button == 1 and self.xLoc <= e.pos[0] and self.yLoc <= e.pos[1] and self.xLoc + self.width >= e.pos[0] and self.yLoc + self.length >= e.pos[1]:
			return True

	def create_image(self):
		window.blit(self.image,(self.xLoc,self.yLoc))


	

# Alpha Rectangles

def draw_rect_alpha(surface, color, rect, border, corners):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect(),border,corners)
    surface.blit(shape_surf, rect)


# ------------------------------------- main game loop -------------------------------------------

# Pregame Preperation

window = display.set_mode((800, 600))
display.set_caption("Flappy Bird")
high_score = 0
game_score = 0

bird_sprite = Player("assets/flappy bird test.png",400,150,50,-1,13)
bird_sprite_hit_box = Player("assets/flappy bird test.png",400,150,50,-1,13)
bird_picture = "assets/flappy bird test.png"
previous_score = 0
coins_counter = 0

bird_ownership = {1:True,2:False,3:False,4:False,5:False,6:False,7:False,8:False,9:False,10:False}
bird_costs = [0,1,2,3,4,5,10,20,50,100]

while True:

	bird_sprite = Player(bird_picture,400,150,50,-1,13)
	bird_sprite_hit_box = Player("assets/flappy bird test.png",400,150,50,-1,13)

	background_image = Image("assets/flappy bird background.png",0,-90,800,600)
	ground_image = Moving_Image("assets/flappy bird ground.png",0,500,1231,100,4,-400)
	pipe_1_top = Green_Pipe("assets/double sided green pipe.png",1100,-300,4,100,500,True,200)
	pipe_1_bottom = Green_Pipe("assets/double sided green pipe.png",1100,400,4,100,500,False,200)
	pipe_2_top = Green_Pipe("assets/double sided green pipe.png",1100 + 475,-250,4,100,500,True,200)
	pipe_2_bottom = Green_Pipe("assets/double sided green pipe.png",1100 + 475,450,4,100,500,False,200)
	random_location = 300

	sprite_collider_list = []
	sprite_collider_list.append(pipe_1_top)
	sprite_collider_list.append(pipe_1_bottom)
	sprite_collider_list.append(pipe_2_top)
	sprite_collider_list.append(pipe_2_bottom)

	button_list = []
	button_list.append(Button("assets/shopping_png.png",675,475,50,50))
	button_list.append(Button("assets/flappy bird test.png",175,250,50,50))
	button_list.append(Button("assets/flappy bird image 2.png",275,250,50,50))
	button_list.append(Button("assets/flappy bird image 3.png",375,250,50,50))
	button_list.append(Button("assets/flappy bird image 4.png",475,250,50,50))
	button_list.append(Button("assets/flappy bird image 5.png",575,250,50,50))
	button_list.append(Button("assets/flappy bird image 6.png",175,400,50,50))
	button_list.append(Button("assets/flappy bird image 7.png",275,400,50,50))
	button_list.append(Button("assets/flappy bird image 8.png",375,400,50,50))
	button_list.append(Button("assets/flappy bird image 9.png",475,400,50,50))
	button_list.append(Button("assets/flappy bird image 10.png",575,400,50,50))


	previous_score_text = Phrase(0,0,0,"assets/ARCADECLASSIC.TTF","Score    " + str(int(previous_score)),100,440,50)
	if game_score >= high_score:
		high_score = game_score
		high_score_text = Phrase(0,0,0,"assets/ARCADECLASSIC.TTF","High    Score    " + str(int(high_score)),100,490,50)

	game_score = 0

	starting_text = Phrase(0,0,0,"assets/ARCADECLASSIC.TTF","Press   SPACE!",200,70,65)

	# ---------------------------- starting screen -------------------------------------

	start_game = False
	shopping_screen = False
	while start_game == False:
		
		background_image.create_image()
		pipe_1_top.reset()
		pipe_1_bottom.reset()
		pipe_2_top.reset()
		pipe_2_bottom.reset()
		ground_image.create_image()

		bird_sprite = Player(bird_picture,400,150,50,-1,13)
		bird_sprite.reset()

		draw_rect_alpha(window, (150, 75, 0, 200),(50, 50, 700, 500),0,50)
		draw_rect_alpha(window, (0, 0, 0, 255),(50, 50, 700, 500),10,50)

		if shopping_screen == False:
			starting_text.draw_text()
			high_score_text.draw_text()
			previous_score_text.draw_text()
			button_list[0].create_image()
			coins_text = Phrase(0,0,0,"assets/ARCADECLASSIC.TTF","Coins    " + str(int(coins_counter)),100,390,50)
			coins_text.draw_text()

		else:
			bird_sprite.reset()
			coins_text = Phrase(0,0,0,"assets/ARCADECLASSIC.TTF","Coins    " + str(int(coins_counter)),100,70,50)
			coins_text.draw_text()
			for i in range(len(button_list)):
				button_list[i].create_image()

			for i in range(2):
				for j in range(5):
					temp_text = "null"
					if bird_ownership[int(i * 5 + j) + 1] == True:
						temp_text = "Owned"
					else:
						temp_text = "        " + str(bird_costs[int(i * 5 + j)])
						temp_coin = Image("assets/coin clip art.png",100 * j + 170,i * 150 + 315,20,20)
						temp_coin.create_image()

					temp_text = Phrase(0,0,0,"assets/ARCADECLASSIC.TTF",temp_text,100 * j + 175,i * 150 + 320,20)
					temp_text.draw_text()
		
		# Checking if a button has been pressed

		for event in pygame.event.get():
			if(event.type == KEYDOWN):

				# If space is pushed down

				if(event.key == K_SPACE):
					start_game = True
			if (event.type == MOUSEBUTTONDOWN):
				for i in range(len(button_list)):
					if button_list[i].button_press(event) == True:
						if i == 0:
							if shopping_screen == False:
								shopping_screen = True
							else:
								shopping_screen = False
						else:
							if shopping_screen == True:
								if bird_ownership[i] == True:
									bird_picture = button_list[i].picture
								else:
									if coins_counter >= bird_costs[i - 1]:
										bird_ownership[i] = True
										coins_counter -= bird_costs[i - 1]
									else:
										print("Not enough money for", i)


		display.update()

	# ---------------------------------- in the game ----------------------------------

	fps_counter = 0
	time_passed = pygame.time.get_ticks()
	fps_text = Phrase(0,0,0,"assets/ARCADECLASSIC.TTF","fps    " + str(int(fps_counter)),10,10,25)
	game_loop = True
	while game_loop == True:

		# Creating the home screen
		time.sleep(0.025)

		background_image.create_image()

		pipe_1_top.update()
		pipe_1_top.reset()
		pipe_1_bottom.update()
		pipe_1_bottom.reset()

		pipe_2_top.update()
		pipe_2_top.reset()
		pipe_2_bottom.update()
		pipe_2_bottom.reset()

		ground_image.update()
		ground_image.create_image()

		bird_sprite.update()
		bird_sprite_hit_box.hit_box_location()
		bird_sprite.reset()

		fps_counter += 1
		fps_text.draw_text()
		if pygame.time.get_ticks() - 1000 >= time_passed:
			fps_text = Phrase(0,0,0,"assets/ARCADECLASSIC.TTF","fps    " + str(int(fps_counter)),10,10,25)
			fps_counter = 0
			time_passed = pygame.time.get_ticks()

		game_score_text = Phrase(0,0,0,"assets/ARCADECLASSIC.TTF",str(int(game_score)),700,50,100)
		game_score_text.draw_text()

		for i in range(len(sprite_collider_list)):
			if sprite.collide_rect(sprite_collider_list[i],bird_sprite_hit_box) or bird_sprite.rect.y >= 475 or bird_sprite.rect.y <= -100:
				previous_score = int(game_score)
				coins_counter += game_score
				game_loop = False
				break
				

		display.update()