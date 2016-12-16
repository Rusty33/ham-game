import sys,pygame
import gif
from random import randint
import time
import spawnSeed
screen = pygame.display.set_mode((1800,1000))






class Ani():
		def __init__(self,last_ani,M_Right,M_Left,M_Down,M_Up,hamRD,hamRU,hamR,hamLD,hamLU,hamL,dotsrect,hamRDrect,hamRUrect,hamRrect,hamLDrect,hamLUrect,hamLrect):
			self.last_ani = last_ani
			self.M_Right = M_Right
			self.M_Left = M_Left
			self.M_Down = M_Down
			self.M_Up = M_Up
			self.hamRD = hamRD
			self.hamRU = hamRU
			self.hamR = hamR
			self.hamLD = hamLD
			self.hamLU = hamLU
			self.hamL = hamL
			self.dotsrect = dotsrect
			self.hamRDrect = hamRDrect
			self.hamRUrect = hamRUrect
			self.hamRrect = hamRrect
			self.hamLDrect = hamLDrect
			self.hamLUrect = hamLUrect
			self.hamLrect = hamLrect


		def RunAniR(self):
			if self.last_ani == 'r':
				if self.M_Right or self.M_Left or self.M_Down or self.M_Up:
					if self.M_Right and self.M_Down:
						self.hamRD.render(screen, (self.dotsrect.centerx-self.hamRDrect.centerx,self.dotsrect.centery-self.hamRDrect.centery))
					elif self.M_Right and self.M_Up:
						self.hamRU.render(screen, (self.dotsrect.centerx-self.hamRUrect.centerx,self.dotsrect.centery-self.hamRUrect.centery))

					else:
						self.hamR.render(screen, (self.dotsrect.centerx-self.hamRrect.centerx,self.dotsrect.centery-self.hamRrect.centery))
		def RunAniL(self):
			if self.last_ani == 'l': 
				if self.M_Right != False or self.M_Left != False or self.M_Down != False or self.M_Up != False:
					if self.M_Left and self.M_Down:
						self.hamLD.render(screen, (self.dotsrect.centerx-self.hamLDrect.centerx,self.dotsrect.centery-self.hamLDrect.centery))
					elif self.M_Left and self.M_Up:
						self.hamLU.render(screen, (self.dotsrect.centerx-self.hamLUrect.centerx,self.dotsrect.centery-self.hamLUrect.centery))
	
					else:
						self.hamL.render(screen, (self.dotsrect.centerx-self.hamLrect.centerx,self.dotsrect.centery-self.hamLrect.centery))

