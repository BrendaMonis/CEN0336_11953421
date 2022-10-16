#!/usr/bin/env python3
import sys

#Para que seja possível visualizar os comandos é necessário mudar as permissões de um arquivo ou pasta no terminal
#Para isso, basta rodar o seguinte comando: chmod +x script_cDNA.py
#Após isso, é necessário adicionar o comando: ./script_cDNA.py

#O primeiro passo a ser feito é adicionar os argumentos na linha de comando
DNA = 'CGTCGTCGCCGCCGCCGCCATGTCGGGAGGTGGTGTGATCCGTGGCCCGACGAAAAAAAAAAAAAGCGGGGAACAACGACTGCCGCATCTACGTGTAAAAAAACGAAAAAAAAAAAAAAAAAAAA'
print('a sequência de DNA é', DNA)

N1 = 20
print(N1, 'é a coordenada N1')

N2 = 49
print(N2, 'é a coordenada N2')

N3 = 66
print(N3, 'é a coordenada N3')

N4 = 98
print(N4, 'é a coordenada N4')

#Posteiormente, deve-se conferir se os dados estão corretos e se não há nenhum número inteiro maior que o tamanho da sequência de DNA
len(DNA)
if (N1 and N2 and N3 and N4 < len(DNA)): #Testando se as coordenadas não são maiores que o tamanho da sequência
 print('as coordenadas são menores que o tamanho da sequência de DNA')
else:
 print('as coordenadas são maiores que o tamanho da sequência de DNA')

tudo_certo = True

try:
 N1 = int(N1)
except:
    tudo_certo = False
try:
 N2 = int(N2)
except:
    tudo_certo = False
try:
 N3 = int(N3)
except:
    tudo_certo = False
try:
 N4 = int(N4)
except:
    tudo_certo = False

if (tudo_certo == True): #Testando se as coordenadas são um número inteiro
 print('as coordenadas são um número inteiro')

#Em seguida, deseja-se extrair a sequência CDS1 e, após isso, conferir se a mesma inicia com ATG
CDS1 = DNA[(N1-1):N2] #Extraindo a sequência CDS1
print('A sequência de CDS1 é', CDS1)

CDS1.find('ATG') #Conferindo se inicia com o códon de início ATG
print(CDS1.find('ATG'), 'é a posição do index ATG')
if (CDS1.find('ATG') == 0):
 print('A sequência começa com ATG')
else:
 print('A sequência não começa com ATG')

#Também deseja-se extrair a sequência CDS2 e, após isso, conferir se a mesma termina com TAG, TAA OU TGA
CDS2 = DNA[(N3-1):N4]
print('A sequência de CDS2 é', CDS2)

#Conferindo se termina com um dos códons de parada
#TAG:
CDS2.find('TAG')
print(CDS2.find('TAG'), 'é a posição do index do códon de parada TAG')
if (CDS2.find('TAG') == 30):
 print('A sequência termina com TAG')
else:
 print('A sequência não termina com TAG')

#TAA:
CDS2.find('TAA')
print(CDS2.find('TAA'), 'é a posição do index do códon de parada TAA')
if (CDS2.find('TAA') == 30):
 print('A sequência termina com TAA')
else:
 print('A sequência não termina com TAA')

#TGA:
CDS2.find('TGA')
print(CDS2.find('TGA'), 'é a posição do index do códon de parada TGA')
if (CDS2.find('TGA') == 30):
 print('A sequência termina com TGA')
else:
 print('A sequência não termina com TGA')

#Por último, como a sequência CDS1 inicia com ATG e a CDS2 termina com TAA, deve-se concatenar CDS1 e CDS2
print('A sequência CDS1 e CDS2 concatenadas é:')
print(CDS1, CDS2, sep = '')
