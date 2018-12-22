
# iniciar pygame
import pygame, sys
from pygame.locals import *
pygame.init()

screen=pygame.display.set_mode((600,400),0,32)

def manyLines():
#com erro
	i=20
	x=10
	p1=(50+x,50+x)
	p2=(10+x*2,10+x*2)
	while i>0:
		pygame.draw.lines(screen,(0,255,0),False,[(100+x,100+x),p1])
		x+=10
		i-=1
pygame.display.flip()



