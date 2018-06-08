#!/usr/bin/python3.5
#coding: utf-8

class Interp_Newton():

	def __init__(self,lista_x,lista_y):

		self.lista_y = lista_y
		self.lista_x = lista_x

	#ACHA O PRIMEIRO K
	def Delta(self,i,j,lista_y,lista_x):

		answer = (lista_y[i] - lista_y[i-j])/(lista_x[i] - lista_x[i-j])
		return answer
	#AS DUAS FUNÇÕES A SEGUIR FAZEM A SEPARADAMENTE O QUE A PRIMEIRA FAZ
	def Delta_up(self,k,i,j):

		answer = (k[i] - k[i-j])
		return answer

	def Delta_down(self,lista_x,i,j):

		answer = (lista_x[i+j] - lista_x[i])
		return answer

	def Interpolation(self,x,x_value,n):

		if n < 1:
			return (x_value-x[n])
		else:
			answ = (x_value-x[n])*self.Interpolation(x,x_value,(n-1))
			return answ


### MAIN ###
x = [1,3,4,5]
y = [0,6,24,60]
k = []
K_final = []
IN = Interp_Newton(x,y)
UP = []
DOWN = []
precision = 5
X_value = 3

#PRIMEIRO K
for i in range(1,len(IN.lista_x)):
	
	k.append(IN.Delta(i,1,IN.lista_y, IN.lista_x))
	
#LISTA QUE ARMAZENA OS K[i] QUE SERÃO USADOS NO P(x)
K_final.append(round(k[0],precision))
j = 2

#K's RESTANTES
while j != (len(IN.lista_x)):
	UP = []
	DOWN = []
	for i in range(1,len(k),1):
		UP.append(IN.Delta_up(k,i,1))

	for i in range(len(k)-1):
		DOWN.append(IN.Delta_down(IN.lista_x,i,j))
	
	k = []
	for i in range(len(UP)):
		k.append(round(UP[i]/DOWN[i],precision))
		print("******RESPOSTA: ",round(UP[i]/DOWN[i],precision))
	K_final.append(k[0])
	j += 1
	print(K_final)

i = 0
parcela_2 = []

while i <= len(K_final)-1:
	parcela_2.append(IN.Interpolation(IN.lista_x, X_value, i))
	print("IND ",parcela_2[i])
	i += 1

print(parcela_2)

parcela_semi = 0
i = 0
while i < len(K_final):
	print(i)
	parcela_semi += (parcela_2[i]*K_final[i])
	i += 1

RESPOSTA_FINAL = IN.lista_y[0] + parcela_semi

print(RESPOSTA_FINAL)