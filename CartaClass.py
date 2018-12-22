
import random, sys
from random import randint

class Carta:
	valores=["JOKER","DOIS","TRES","QUATRO","CINCO","SEIS","SETE","OITO","NOVE","DEZ","VALETE","DAMA","REI","AS"]
	naipes=["JOKER","COPAS","ESPADAS","OUROS","PAUS"]
	naipe=None
	valor=None
	def __init__(self):
		self.naipe=self.naipes[0]
		self.valor=self.valores[0]
	def show(self):
		print self.valor+" de "+self.naipe
	def randomCard(self):
	    self.valor=valores[randint(0,13)]
	    self.naipe=naipes[randint(0,4)]
