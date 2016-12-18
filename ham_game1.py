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
TargetScore = 50
score = 0
NextLevel = True

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

TargetScoreFont = myfont.render('Target score:' + str(TargetScore),1,(225,225,0))

screen = pygame.display.set_mode((1800,1000))
pygame.display.set_caption('HAMTARO TIME')

dots = pygame.image.load('dance.gif').convert()
dotsrect = dots.get_rect()

last_ani = 'r'
other_ani = False
cheet_ani = False 
lose_ani = False


cheet = 0
cheet_delay = 2

speed = 5
MaxSeed = 1

M_Up = False
M_Down = False
M_Left = False
M_Right = False
dotsrect.centerx = 900
dotsrect.centery = 500

#ham d is idle
hamD = gif.GIFImage('ham_sniff.gif')
hamDrect = hamD.get_rect()

hamD2 = gif.GIFImage('ham_look.gif')
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

hamCheet = gif.GIFImage('ham_powerup.gif')
hamCheetrect = hamCheet.get_rect()
##########################################
hamLose = gif.GIFImage('hamtaro_lose_sad.gif')
hamLoserect = hamLose.get_rect()
hamLoserect.centerx = 900
hamLoserect.y = 950



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
	global level_num,Ctime,TargetScore
	if level_num <= 5:
		Ctime =  60 - level_num * 5
	else:
		Ctime = 30 
		

level_set()
level_time_delay = 10


while True:
	screen.fill((0,104,10))
	screen.blit(timer,(900,15))
	screen.blit(scoreFont,(1600,15))
	screen.blit(TargetScoreFont,(200,15))
	clock.tick(60)
	timer = myfont.render(str(Ctime),1,(225,225,0))
	scoreFont = myfont2.render(str(score),1,(225,225,0))
	TargetScoreFont = myfont.render('Target score:' + str(TargetScore),1,(225,225,0))

	Ani = class_ani.Ani(last_ani,M_Right,M_Left,M_Down,M_Up,hamRD,hamRU,hamR,hamLD,hamLU,hamL,dotsrect,hamRDrect,hamRUrect,hamRrect,hamLDrect,hamLUrect,hamLrect)
	seed1.move()
	seed2.move()
	seed3.move()
	seed4.move()
	seed5.move()
	screen.blit(Box,Boxrect)
	Ani.RunAniR()
	Ani.RunAniL()

	keys = pygame.key.get_pressed()
	

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == timeEvent:
			if game == True:
				if Ctime == 1:
					game = False
					inventory = 0
					if TargetScore <= score:
						NextLevel = True
					else:
						NextLevel = False
				Ctime -= 1

		if event.type == level_delay:
			if game == False and level_time_delay != 0:
				level_time_delay -= 1
			if game == False and NextLevel == True and level_time_delay == 0:
				level_set()
				level_time_delay = 10
				level_num += 1
				game = True
				TargetScore += 50
			elif NextLevel == False:
				lose_ani = True
				
			

		elif event.type == aniEvent:
			if cheet_ani == True and cheet_delay != 0:
				cheet_delay -= 1
			elif cheet_delay == 0:
				cheet_delay = 2
				cheet_ani = False

			
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
		#this is ware i put in key presses for cheets
			if event.key == pygame.K_i and keys[pygame.K_c]:
				cheet = 2
				cheet_ani = True
				ani_delay = 2
				other_ani = True
			if event.key == pygame.K_u:
				cheet = 1
				cheet_ani = True
				ani_delay = 2
				other_ani = True


				
				
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
	#seting what cheets do based of a variable
	if cheet == 1:
		speed = 15
	else:
		speed = 5
	if cheet == 2:
		MaxSeed = 10
	else:
		MaxSeed = 1
	

	#these lines of code deal with moving our dotsrect place holder
	if game == True and  M_Left == True and dotsrect.x <= 1780:
		dotsrect.x -= speed

	
	if  game == True and M_Right == True and dotsrect.x <= 1760:
		dotsrect.x += speed
		#if M_Left == False and M_Down == False and M_Up == False:
	if  game == True and M_Down == True and dotsrect.y <= 960:
		dotsrect.y += speed
		#if M_Right == False and M_Left == False and M_Up == False:
	if  game == True and M_Up == True and dotsrect.y >= 0:
		dotsrect.y -= speed
		
		
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
	if other_ani == True and cheet_ani == False and lose_ani == False:
		hamEAT.render(screen,(dotsrect.centerx-hamEATrect.centerx,dotsrect.centery-hamEATrect.centery))
	#other animaitions based off varaibles
	if cheet_ani == True:
		hamCheet.render(screen,(dotsrect.centerx-hamCheetrect.centerx,dotsrect.centery-hamCheetrect.centery))
	if lose_ani == True:
		hamLose.render(screen,(hamLoserect.centerx,hamLoserect.centery))


	#colide points seeds
	if dotsrect.colliderect(seed1.rect) and inventory < MaxSeed:
		other_ani = True
		seedNum -= 1
		inventory += 1
		seed1.spawn()
	if dotsrect.colliderect(seed2.rect) and inventory < MaxSeed:
		other_ani = True
		seedNum -= 1
		inventory += 1
		seed2.spawn()
	if dotsrect.colliderect(seed3.rect) and inventory < MaxSeed:
		other_ani = True
		seedNum -= 1
		inventory += 1
		seed3.spawn()
	if dotsrect.colliderect(seed4.rect) and inventory < MaxSeed:
		other_ani = True
		seedNum -= 1
		inventory += 1
		seed4.spawn()
	if dotsrect.colliderect(seed5.rect) and inventory < MaxSeed:
		other_ani = True
		seedNum -= 1
		inventory += 1
		seed5.spawn()

	if dotsrect.colliderect(Boxrect) and inventory > 0:
		other_ani = True
		score += inventory * 10 
		inventory = 0


	





	pygame.display.flip()


