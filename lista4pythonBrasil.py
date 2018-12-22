


def numConsoantes():
	#incompleto
	vogais=['a','e','i','o','u']
	i=0
	cont=0
	aux=0
	lista=[]
	lista.extend(range(0,10))
	while i<10:
		lista[i]=raw_input("Digite uma letra: ")
		i+=1
	for x in lista:
		for y in vogais:
			if x==y:
				aux+=1
		if aux==4:
			cont+=1
			aux=0
			print x
	print "Numero de consoantes: "+str(cont)