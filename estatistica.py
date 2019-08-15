# coding=utf-8
# Python v3.5
import math
n = int(input("Digite a quantidade de números: "))
x = []
soma = 0
var = 0
a = 0
c = 0
for i in range(1,n+1):
	m = int(input("Digite o número: "))
	soma = soma + m
	x.append(m)
media = soma/n
while c<n:
	var = var + (x[a]-media)**2
	a = a + 1
	c = c + 1
var2 = var/n
desvio = math.sqrt(var2)
print ("Média: ",media)
print ("Variância: ",var2)
print ("Desvio Padrão: ",desvio)
