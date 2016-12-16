import sys,pygame
import gif
from random import randint
import time
import spawnSeed

pygame.init()

idle_A = 0

level_num = 1


ani_delay = 1
delay = 1000
timeEvent = pygame.USEREVENT +1
pygame.time.set_timer(timeEvent,delay)

aniEvent = pygame.USEREVENT +2
pygame.time.set_timer(aniEvent,500)


#pygame.time.set_timer(1000)


Ctime = 60
game = True 
myfont = pygame.font.SysFont('monospace',15)
timer = myfont.render(str(Ctime),1,(225,225,0))


screen = pygame.display.set_mode((1800,1000))
pygame.display.set_caption('dots')

dots = pygame.image.load('dance.gif').convert()
dotsrect = dots.get_rect()

last_ani = 'r'
other_ani = False


M_Up = False
M_Down = False
M_Left = False
M_Right = False
dotsrect.centerx = 900
dotsrect.centery = 500

#ham d is idle
hamD = gif.GIFImage('ham_sniff.gif')
hamDrect = hamD.get_rect()

hamD2 = gif.GIFImage('ham_small_win.gif')
hamD2rect = hamD2.get_rect()

hamR = gif.GIFImage('hamtaro_running_small.gif')
hamRrect = hamR.get_rect()

hamL = gif.GIFImage('ham_running_small_left.gif')
hamLrect = hamL.get_rect()

hamRD = gif.GIFImage('TEST.gif')
hamRDrect = hamRD.get_rect()

hamLD = gif.GIFImage('ham_running_left_down.gif')
hamLDrect = hamLD.get_rect()

hamLU = gif.GIFImage('ham_running_up_left.gif')
hamLUrect = hamLU.get_rect()

hamRU = gif.GIFImage('ham_running_right_up.gif')
hamRUrect = hamRU.get_rect()

hamEAT = gif.GIFImage('ham_eat_seed.gif')
hamEATrect = hamEAT.get_rect()

idle_G = [hamD,hamD2]
idle_XY = [hamDrect,hamD2rect]


Box = pygame.image.load('seedBox.png').convert()
Boxrect = Box.get_rect()
Boxrect.centerx = 900
Boxrect.centery = 100


seed = pygame.image.load('seed.jpg').convert()
seed2 = pygame.image.load('seed.jpg').convert()
seed3 = pygame.image.load('seed.jpg').convert()
seed4 = pygame.image.load('seed.jpg').convert()
seed5 = pygame.image.load('seed.jpg').convert()


seedrect = seed.get_rect()
seedrect2 = seed2.get_rect()
seedrect3 = seed3.get_rect()
seedrect4 = seed4.get_rect()
seedrect5 = seed5.get_rect()


clock = pygame.time.Clock()
seedNum = 0
inventory = 0
	

seed1 = spawnSeed.Cseed(seedrect,seed,'1')
seed2 = spawnSeed.Cseed(seedrect2,seed2,'2')
seed3 = spawnSeed.Cseed(seedrect3,seed3,'3')
seed4 = spawnSeed.Cseed(seedrect4,seed4,'4')
seed5 = spawnSeed.Cseed(seedrect5,seed5,'5')

seed1.spawn()
seed2.spawn()
seed3.spawn()
seed4.spawn()
seed5.spawn()

while True:
	screen.fill((0,104,10))
	screen.blit(timer,(900,15))
	clock.tick(60)
	timer = myfont.render(str(Ctime),1,(225,225,0))


	seed1.move()
	seed2.move()
	seed3.move()
	seed4.move()
	seed5.move()
	screen.blit(Box,Boxrect)

	

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == timeEvent:
			if game == True:
				if Ctime == 1:
					game = False
				Ctime -= 1
		elif event.type == aniEvent:
			if other_ani == True and ani_delay != 0:
				ani_delay -= 1
				print(ani_delay)
			elif other_ani == True:
				ani_delay = 1
				other_ani = False
				

				
		#while key down/movment/last ani
		elif event.type == pygame.KEYDOWN and other_ani == False:
			if event.key == pygame.K_d:
				M_Right = True
				last_ani = 'r'
			if event.key == pygame.K_a:
				M_Left = True
				last_ani = 'l'
			if event.key == pygame.K_s:
				M_Down = True
			if event.key == pygame.K_w:
				M_Up = True
				
		#while key up/movement
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_d:
				M_Right = False
			if event.key == pygame.K_a:
				M_Left = False
			if event.key == pygame.K_s:
				M_Down = False
			if event.key == pygame.K_w:
				M_Up = False

		#clicking with mouse
		elif event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			posX = pos[0]
			posY = pos[1]
			
			if posY >= dotsrect.y and posY <= dotsrect.bottom and posX >= dotsrect.x and posX <= dotsrect.right : 
				if idle_A == 0:
					idle_A += 1
				else:
					idle_A -= 1


	#set speed/movment
	if M_Left == True and dotsrect.x <= 1780:
		dotsrect.x -= 5

	
	if M_Right == True and dotsrect.x <= 1760:
		dotsrect.x += 5
		#if M_Left == False and M_Down == False and M_Up == False:
	if M_Down == True and dotsrect.y <= 960:
		dotsrect.y += 5
		#if M_Right == False and M_Left == False and M_Up == False:
	if M_Up == True and dotsrect.y >= 0:
		dotsrect.y -= 5
		
		

	if other_ani == True:
		M_Right = False
		M_Left = False
		M_Down = False
		M_Up = False




	#sets idle animotion
	if other_ani == False and M_Right == False and M_Left == False and M_Down == False and M_Up == False:
		idle_G[idle_A].render(screen, (dotsrect.centerx-idle_XY[idle_A].centerx,dotsrect.centery-idle_XY[idle_A].centery))
	if other_ani == True:
		hamEAT.render(screen,(dotsrect.centerx-hamEATrect.centerx,dotsrect.centery-hamEATrect.centery))

	#running animation
	if last_ani == 'r':
		if M_Right or M_Left or M_Down or M_Up:
			if M_Right and M_Down:
				hamRD.render(screen, (dotsrect.centerx-hamRDrect.centerx,dotsrect.centery-hamRDrect.centery))
			elif M_Right and M_Up:
				hamRU.render(screen, (dotsrect.centerx-hamRUrect.centerx,dotsrect.centery-hamRUrect.centery))

			else:
				hamR.render(screen, (dotsrect.centerx-hamRrect.centerx,dotsrect.centery-hamRrect.centery))

	if last_ani == 'l': 
		if M_Right != False or M_Left != False or M_Down != False or M_Up != False:
			if M_Left and M_Down:
				hamLD.render(screen, (dotsrect.centerx-hamLDrect.centerx,dotsrect.centery-hamLDrect.centery))
			elif M_Left and M_Up:
				hamLU.render(screen, (dotsrect.centerx-hamLUrect.centerx,dotsrect.centery-hamLUrect.centery))

			else:
				hamL.render(screen, (dotsrect.centerx-hamLrect.centerx,dotsrect.centery-hamLrect.centery))
	#colide points seeds
	if dotsrect.colliderect(seed1.rect) and inventory < 1:
		other_ani = True
		seedNum -= 1
		inventory += 1
		seed1.spawn()
	if dotsrect.colliderect(seed2.rect) and inventory < 1:
		other_ani = True
		seedNum -= 1
		inventory += 1
		seed2.spawn()
	if dotsrect.colliderect(seed3.rect) and inventory < 1:
		other_ani = True
		seedNum -= 1
		inventory += 1
		seed3.spawn()
	if dotsrect.colliderect(seed4.rect) and inventory < 1:
		other_ani = True
		seedNum -= 1
		inventory += 1
		seed4.spawn()
	if dotsrect.colliderect(seed5.rect) and inventory < 1:
		other_ani = True
		seedNum -= 1
		inventory += 1
		seed5.spawn()

	if dotsrect.colliderect(Boxrect) and inventory > 0:
		other_ani = True
		inventory = 0

	





	pygame.display.flip()


