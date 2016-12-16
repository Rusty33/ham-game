import sys,pygame
import gif
from random import randint
import time
import spawnSeed
from threading import Timer
import class_ani

pygame.init()

idle_A = 0

level_num = 1
score = 0

ani_delay = 1
delay = 1000



timeEvent = pygame.USEREVENT +1
pygame.time.set_timer(timeEvent,delay)

aniEvent = pygame.USEREVENT +2
pygame.time.set_timer(aniEvent,500)

level_delay = pygame.USEREVENT +3
pygame.time.set_timer(level_delay,delay)


#pygame.time.set_timer(1000)


Ctime = 60
game = True 
myfont = pygame.font.SysFont('monospace',15)
timer = myfont.render(str(Ctime),1,(225,225,0))

myfont2 = pygame.font.SysFont('monospace',15)
scoreFont = myfont2.render(str(score),1,(225,225,0))


screen = pygame.display.set_mode((1800,1000))
pygame.display.set_caption('HAMTARO TIME')

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

def level_set():
	global level_num,Ctime
	if level_num <= 5:
		Ctime =  60 - level_num * 5

level_set()
level_time_delay = 10


while True:
	screen.fill((0,104,10))
	screen.blit(timer,(900,15))
	screen.blit(scoreFont,(1600,15))
	clock.tick(60)
	timer = myfont.render(str(Ctime),1,(225,225,0))
	scoreFont = myfont2.render(str(score),1,(225,225,0))

	Ani = class_ani.Ani(last_ani,M_Right,M_Left,M_Down,M_Up,hamRD,hamRU,hamR,hamLD,hamLU,hamL,dotsrect,hamRDrect,hamRUrect,hamRrect,hamLDrect,hamLUrect,hamLrect)
	seed1.move()
	seed2.move()
	seed3.move()
	seed4.move()
	seed5.move()
	screen.blit(Box,Boxrect)
	Ani.RunAniR()
	Ani.RunAniL()
	

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == timeEvent:
			if game == True:
				if Ctime == 1:
					game = False
					inventory = 0
				Ctime -= 1

		if event.type == level_delay:
			if game == False and level_time_delay != 0:
				level_time_delay -= 1
			if game == False and level_time_delay == 0:
				level_set()
				level_time_delay = 10
				level_num += 1
				game = True
			

		elif event.type == aniEvent:
			if other_ani == True and ani_delay != 0:
				ani_delay -= 1
				print(ani_delay)
			elif other_ani == True:
				ani_delay = 1
				other_ani = False
				

				
		#while key down/movment/last ani
		elif event.type == pygame.KEYDOWN and other_ani == False and game == True:
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

		#if you click on the hamster it will change its idle animation. this deals with the colistion of the mouse and changing the idle animation.
		elif event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			posX = pos[0]
			posY = pos[1]
			
			if posY >= dotsrect.y and posY <= dotsrect.bottom and posX >= dotsrect.x and posX <= dotsrect.right : 
				if idle_A == 0:
					idle_A += 1
				else:
					idle_A -= 1


	#these lines of code deal with moving our dotsrect place holder
	if game == True and  M_Left == True and dotsrect.x <= 1780:
		dotsrect.x -= 5

	
	if  game == True and M_Right == True and dotsrect.x <= 1760:
		dotsrect.x += 5
		#if M_Left == False and M_Down == False and M_Up == False:
	if  game == True and M_Down == True and dotsrect.y <= 960:
		dotsrect.y += 5
		#if M_Right == False and M_Left == False and M_Up == False:
	if  game == True and M_Up == True and dotsrect.y >= 0:
		dotsrect.y -= 5
		
		
	# this block of code will set all movemint to false if the game is false(in between levels) or if any other none runing or idle related movement is cerintly happaning.
	if other_ani == True or game == False:
		M_Right = False
		M_Left = False
		M_Down = False
		M_Up = False




	#sets idle animotion based off idle_G list by useing a varable to choose what animation in list to use.
	if other_ani == False and M_Right == False and M_Left == False and M_Down == False and M_Up == False:
		idle_G[idle_A].render(screen, (dotsrect.centerx-idle_XY[idle_A].centerx,dotsrect.centery-idle_XY[idle_A].centery))

	#if other_ani varable = true then it will play a eating animation	
	if other_ani == True:
		hamEAT.render(screen,(dotsrect.centerx-hamEATrect.centerx,dotsrect.centery-hamEATrect.centery))

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
		score += 10

	





	pygame.display.flip()


