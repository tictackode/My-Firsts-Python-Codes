
def randList(num):
	i=0
	lista=[]
	lista.extend(range(0,num))
	while i<num:
		lista[i]=randint(0,20)
		i+=1
	return lista

def asciiBar(num):
	i=0
	lista=[]
	lista.extend(range(0,num))
	lista=randList(num)
	while i<len(lista):
		print lista[i]*"O"
		i+=1
		
		

	def rList(num):
	i=0
	lista=[]
	lista.extend(range(0,num))
	while i<num:
		lista[i]=randint(0,20)
		print lista[i]*"O"+" "+str(lista[i]).rjust(5)
		i+=1
	
	def rList(num):
	# poe um zero a esquerda e imprime o grafico
	i=0
	lista=[]
	lista.extend(range(0,num))
	while i<num:
		lista[i]=randint(0,20)
		print str(lista[i]).zfill(2)+" "+lista[i]*"O"
		i+=1

	def spList(num):
	#retorna uma lista com o treco todo
	i=0
	lista=[]
	lista.extend(range(0,num))
	l=[]
	l.extend(range(0,num))
	while i<num:
		lista[i]=randint(0,20)
		l[i]= str(lista[i]).zfill(2)+" "+lista[i]*"O"
		i+=1
	return l
	
	def gList(num):
	#repare nos dois retornos
	i=0
	lista=[]
	lista.extend(range(0,num))
	l=[]
	l.extend(range(0,num))
	x=[]
	x.extend(range(0,num))
	while i<num:
		lista[i]=randint(0,20)
		l[i]=lista[i]*"O"
		x[i]=len(l[i])
		i+=1
	return l,x