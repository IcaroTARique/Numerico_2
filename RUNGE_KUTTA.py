#!/usr/bin/python3.6
#coding: utf-8
import sys

class Runge_Kutta():

    def __init__(self,inicial,final,passo):

        self.inicial = inicial
        self.final = final
        self.passo = passo

    def ajuste_x(self,x0,xn,h,lista_valores_x):

        for i in range(int((xn-x0)/h)):

            lista_valores_x[i+1] = round(lista_valores_x[i] + h,5)


    def EDO(self,x,y):

        d_y = (-(y**2)+24*x)/5

        return d_y

### MAIN ### ___ SET 0 - 2 - 1 - 5
#X[0]
x0 = float(sys.argv[1])
#X[n]
xn = float(sys.argv[2])
#PASSO
h = float(sys.argv[3])
#Y0 = Y[X0]
Y0 = float(sys.argv[4])


#OBJETO RK
RK = Runge_Kutta(x0,xn,h)

#Inicia valores de X com o primeiro valor X[0]
lista_valores_x = [x0]*int(((xn-x0)/h)+1)


#Ajusta a lista de x com os valores
RK.ajuste_x(x0,xn,h,lista_valores_x)

#Cria lista para Y com ZEROS
lista_valores_y = [0]*int(((xn-x0)/h)+1)
#Define o valor inicial de Y0
lista_valores_y[0] = Y0

print("X[k] = ",lista_valores_x, "e Y[k] = ",lista_valores_y)

for k in range (len(lista_valores_x)-1):

    lista_valores_y[k+1] = round(lista_valores_y[k] +((h/2) * (RK.EDO(lista_valores_x[k],lista_valores_y[k]) + RK.EDO(lista_valores_x[k]+h,lista_valores_y[k]+h*(RK.EDO(lista_valores_x[k],lista_valores_y[k]))))),5)

print(lista_valores_y)

print("RESPOSTA Y[",len(lista_valores_x)-1,"] = ",lista_valores_y[len(lista_valores_x)-1])