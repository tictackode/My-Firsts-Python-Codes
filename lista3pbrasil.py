

#1-Faça um programa que peça uma nota, entre zero e dez. 
#Mostre uma mensagem caso o valor seja inválido e continue 
#pedindo até que o usuário informe um valor válido.

def lenota():
	nota=-1
	while nota<0 or nota>10:
		nota=float(raw_input("Digite uma nota entre 0 e 10:"))
	print nota
	
#2-Faça um programa que leia um nome de usuário e a sua senha
# e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

def login():
	nome=raw_input("Digite seu nome: ")
	senha=raw_input("Digite sua senha: ")
	while nome==senha:
		senha=raw_input("Digite sua senha: ")

#3-Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';		

def leitura():
      nome=raw_input("Digite o nome: ")
      idade=-1
      salario=-1
      sexo='d'
      estado_civil='x'
      while len(nome)<3:
	    nome=raw_input("Digite o nome: ")
      while idade<0 or idade>150:
	    idade=int(raw_input("Digite a idade: "))
      while sexo!='m' and sexo!='f':
	    sexo=raw_input("Digite m para masculino e f para feminino: ")
      while estado_civil!='c' and estado_civil!='s' and estado_civil!='v' and estado_civil!='d':
	    estado_civil=(raw_input("Digite s=solteiro, v=viuvo, d=divorciado, c=casado"))
      print "Nome "+nome+" - Idade: "+str(idade)+" sexo: "+str(sexo)+" Estado civil: "+str(estado_civil)

def ex_04():
	pais_A=80000
	taxa_A=0.03
	pais_B=200000
	taxa_B=0.015
	while pais_A<pais_B:
		pais_A+=(pais_A*taxa_A)
		pais_B+=(pais_B*taxa_B)
	print "População do pais A ultrapassou a de B! Pais A: "+str(pais_A)+" Pais B: "+str(pais_B)
	
#5-Altere o programa anterior permitindo ao usuário informar as populações
#e as taxas de crescimento iniciais. 
#Valide a entrada e permita repetir a operação.	
def ex_05():
	resposta='s'
	pais_A=-1
	pais_B=-1
	taxa_A=-1
	taxa_B=-1
	while resposta=='s':
	    while pais_A<0:
	        pais_A=float(raw_input("Digite a população do pais A"))
	    while taxa_A<=0:
	        taxa_A=float(raw_input("Digite a taxa de crescimento do Pais A"))
	    while pais_B<0:
	        pais_B=float(raw_input("Digite a população do pais B"))
	    while taxa_B<=0:
	        taxa_B=float(raw_input("Digite a taxa de crescimento do Pais B"))
            if pais_A<pais_B:
	        while pais_A<pais_B:
	             pais_A+=(pais_A*taxa_A)
	             pais_B+=(pais_B*taxa_B)
	    if pais_A>pais_B:
	        while pais_A>pais_B:
	             pais_A+=(pais_A*taxa_A)
	             pais_B+=(pais_B*taxa_B)
	    print "Ultrapassagem: Pais A: "+str(pais_A)+" Pais B: "+str(pais_B)
	    resposta=raw_input("Deseja repetir a operacao? s/n")
	    pais_A=-1
	    pais_B=-1
	    taxa_A=-1
	    taxa_B=-1

#6-Faça um programa que imprima na tela os números de 1 a 20, um abaixo
# do outro. Depois modifique o programa para que ele mostre os números
# um ao lado do outro.
def ex_06():
	i=1
	string=" "
	while i<=20:
		print i
		string+=str(i)+", "
		i+=1
        print string

#7-Faça um programa que leia 5 números e informe o maior número.
def ex_07():
	um=raw_input("Digite um numero: ")
	dois=raw_input("Digite um numero: ")
	tres=raw_input("Digite um numero: ")
	quatro=raw_input("Digite um numero: ")
	cinco=raw_input("Digite um numero: ")
	maior=-999
	lista=[um, dois,tres,quatro,cinco]
	for x in lista:
		if x>maior:
			maior=x
	print " O maior numero é "+str(maior)

#8-Faça um programa que leia 5 números e informe a soma e a média dos números.
def ex_08():
	um=int(raw_input("Digite um numero: "))
	dois=int(raw_input("Digite um numero: "))
	tres=int(raw_input("Digite um numero: "))
	quatro=int(raw_input("Digite um numero: "))
	cinco=int(raw_input("Digite um numero: "))
	lista=[um, dois,tres,quatro,cinco]
	soma=0
	media=0
	for x in lista:
		soma+=x
	print "A soma é: "+str(soma)
	print "A média é: "+str(soma/5.0)

#9-Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
def ex_09():
	for x in range(1,50):
		if x%2!=0:
			print x

#10-Faça um programa que receba dois números inteiros e gere os 
#números inteiros que estão no intervalo compreendido por eles.		
def ex_10():
	num1=int(raw_input("Digite o primeiro numero: "))
	num2=int(raw_input("Digite o segundo numero: "))
	for x in range(num1,num2):
		print x

#11-Altere o programa anterior para mostrar no final a soma dos números.

def ex_11():
	num1=int(raw_input("Digite o primeiro numero: "))
	num2=int(raw_input("Digite o segundo numero: "))
	soma=0
	for x in range(num1+1,num2):
		print x
		soma+=x
	print "A soma dos numeros do intervalo e: "+str(soma)	

#12-Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

def ex_12(num):
	for x in range(0,10):
		print str(num)+" X "+str(x)+"="+str(num*x)

#13-Faça um programa que peça dois números, base e expoente,
# calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

def ex_13():
	base=int(raw_input("Digite a base: "))
	expoente=int(raw_input("Digite o expoente: "))
	total=base
	i=1
	while i<expoente:
		total*=base
		i+=1
	print total

#14-Faça um programa que peça 10 números inteiros, 
#calcule e mostre a quantidade de números pares e a quantidade de números impares.

def ex_14():
	pares=0
	impares=0
	for x in range(0,10):
		aux=int(raw_input("Digite um numero: "))
		if aux%2==0:
			pares+=1
		else:
			impares+=1
	print "quantidade de numeros pares: "+str(pares)
	print "quantidade de numeros impares: "+str(impares)

	#15-A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
	# Faça um programa capaz de gerar a série até o n−ésimo termo.

	def fib(n):
	if n==1:
		return 1
	elif n==2:
		return 1
	else:
		return fib(n-1)+fib(n-2)

     #16-A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
     # Faça um programa que gere a série até que o valor seja maior que 500.

     def ex16():
     	i=1
     	aux=0
     	while aux<=500:
     		aux=fib(i)
     		print aux
     		i+=1
    #17-Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120 
    def fact(num):
	if num==1:
		return 1
	else:
		return num*(fact(num-1))

	#18-Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

	def ex18(n):
	import random
	from random import randint
	def randArray(n):
		lista=[]
		lista.extend(range(0,n))
		i=0
		while i<n:
			lista[i]=randint(0,200)
			i+=1
		return lista
	array=randArray(n)
	maior=0
	menor=201
	soma=0
	for x in array:
		if x>maior:
			maior=x
		if x<menor:
			menor=x
		soma+=x
	print array
	print "O maior numero é "+str(maior)
	print "O menor numero é "+str(menor)
	print "O soma dos numeros e "+str(soma)
   
   #-19Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
   #apenas substituir no randint  desta forma que fiz sem entrada do teclado

   #20-Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o 
   #fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

   def ex20():
  	aux=-1
  	while aux>=16 or aux<0:
	    aux=int(raw_input("Digite um numero entre 1 e 15: "))
	repeat='s'
	while repeat=='s':
	    while aux>=16 or aux<0:
		    aux=int(raw_input("Digite um numero entre 1 e 15: "))
	    print fact(aux)
	    repeat=raw_input("Repetir? s=sim   outra coisa=não ")
	    aux=-1

	#21- Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
	# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

	def ex21(num):
	lista=[1,2,3,4,5,6,7,8,9,10]
	aux=0
	if num%num==0:
		aux+=1
	for x in lista:
		if num%x==0:
			aux+=1
	if aux<4:
		print str(num)+" é um numero primo"
	else:
		print str(num)+" não é um numero primo"

	"""22-Altere o programa de cálculo dos números primos, 
	informando, caso o número não seja primo, por quais número ele é divisível."""

	def ex22(num):
	lista=[1,2,3,4,5,6,7,8,9,10]
	aux=0

	if num%num==0:
		aux+=1
		print str(num)+" é divisivel por "+str(num)
	for x in lista:
		if num%x==0:
			aux+=1
			print str(num)+" é divisivel por "+str(x)
	if aux<4:
		print str(num)+" é um numero primo"
	else:
		print str(num)+" não é um numero primo"

	"""23-Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
	O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
	 Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados."""