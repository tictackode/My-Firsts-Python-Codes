import random, sys


romance=["coração", "pensamento","sentimento"]
frases=["O pulsar de um ","Não conhecia um ","No fundo de um "]
 
def rfrase():
	print frases[randint(0,2)]+romance[randint(0,2)]
	
	
def falsePoetry(num):
	i=0
	while i<num:
		rfrase()
		i+=1