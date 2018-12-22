

doces=["chocolate","brigadeiro","musse","pudim","pave","torta"]

def fgosta(frase):
	if frase.find('gosta')>0:
		return True
	else:
		return False
		
		
def fquer(frase):
	if frase.find('quer')>0:
		return True
	else:
		return False

def findDoces(frase):
#falta corrigir
	aux=False
	for x in doces:
		if frase.find(x)>0:
			aux= True
		else:
			aux= False
	return aux