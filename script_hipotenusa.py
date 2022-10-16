#!/usr/bin/env python3
import sys
import math
import random

#Para que seja possível visualizar os comandos é necessário mudar as permissões de um arquivo ou pasta no terminal 
#Para isso, basta rodar o seguinte comando: chmod +x script_hipotenusa.py
#Após isso, é necessário adicionar o comando: ./script_hipotenusa.py  

#Em seguida, para calcular o inteiro da hipotenusa ao quadrado do triângulo retângulo com lado a e b, é necessário criar tais variáveis
#É importante relembrar que a e b são números inteiros, positivo e ambos menores que 500

a= random.randint(1,500) #sorteando um número para a entre 1 e 500
print(a) #visualizar os números sorteados

b= random.randint(1,500) #sorteando um número para b entre 1 e 500
print(b) #visualizar os números sorteados

#Além disso, antes de calcular a hipotenusa é necessário verificar se os dados inseridos são do tipo desejado
#Para isso, será inserido uma série de controle no código para verificar se a e b são números inteiros, positivo e ambos menores que 500

#Verificação da variável a:
if (a < 500): #Testando se a é maior ou menor que 500
 print(a, 'é um número menor que 500')
else:
 print(a, 'é um número maior que 500')
if (a > 0): #Testando se a é positivo ou negativo
 print(a, 'é positivo')
else:
 print(a,'não é positivo')
try:
    int(a)
    it_is = True
except ValueError:
    it_is = False

if (it_is == True): #Testando se a é um número inteiro
 print(a, 'é inteiro')
else:
 print('erro', a, 'não é inteiro')

#Verificação da variável b: 
if (b < 500): #Testando se b é maior ou menor que 500
 print(b, 'é um número menor que 500')
else:
 print(b, 'é um número maior que 500')
if (b > 0): #Testando se b é positivo ou negativo
 print(b, 'é positivo')
else:
 print(b,'não é positivo')
try:
    int(a)
    it_is = True
except ValueError:
    it_is = False
  
if (it_is == True): #Testando se a é um número inteiro
 print(a, 'é inteiro')
else:
 print('erro', a, 'não é inteiro')

#Apesar de não ser necessário verificar se a e b eram menores que 500 e positivo, pois no sorteio já estava delimitado isso, 
#é bom para testas se os números sorteados se enquadravam nos objetivos 
