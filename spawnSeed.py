from random import randint
import sys,pygame
screen = pygame.display.set_mode((1800,1000))
class Cseed():
	def __init__(self,rect,jpg,name):
		self.rect = rect 
		self.seed = jpg
		self.name = name
		#self.seedNum = seedNum
	
	def spawn(self):
		#global seedNum
		#if seedNum<=5:
			self.rect.x = randint(40,1720)
			self.rect.y = randint(40,920)
			screen.blit(self.seed,self.rect)
			#seedNum +=1
			print("spawning " + self.name + " at "+ str (self.rect.x))
	def move(self):
		screen.blit(self.seed,self.rect)

