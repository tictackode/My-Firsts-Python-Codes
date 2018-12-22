def mediaAritmetica(n):
	aux=0
	soma=0
	while aux<n:
		x=float(raw_input("Entre com o numero: "))
                soma=soma+x
                aux=aux+1
        return soma/n

def mediaGeometrica(n):
	aux=0
	temp=1.0
	while aux<n:
		x=float(raw_input("Entre com o numero: "))
                temp=temp*x
                aux=aux+1
        return (temp**(1.0/n))
