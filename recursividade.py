


def somatorio(num,total):
#total inicia-se com 0 .. gambiarra
	if num==0:
		return total
	else:
		total+=num
		return somatorio(num-1,total)

		
def potencia(exp,base):
	if base==1:
		return exp
	else:
		return exp*potencia(exp, base-1)

def incto(inicio,fim):
	if inicio==fim:
		return fim
	else:
		print inicio
		return incto(inicio+1,fim)

def div2(num):
	if num<2:
		return 1
	else:
		print num
		return div2(num/2)

def div(numero,divisor):
	if numero<2:
		return 1
	else:
		print numero
		return div(numero/divisor,divisor)

def love(nome, num):
	if num==1:
		print nome+" te amarei em "+str(num)+" segundos:"
		print "Te Amo S2"
		return 1
	else:
		print nome+" te amarei em "+str(num)+" segundos:"
		return love(nome,num-1)