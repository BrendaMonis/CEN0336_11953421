#!/usr/bin/env python3
import sys

#Para que seja possível visualizar os comandos é necessário mudar as permissões de um arquivo ou pasta no terminal
#Para isso, basta rodar o seguinte comando: chmod +x script_cDNA.py
#Após isso, é necessário adicionar o comando: ./script_cDNA.py

#O primeiro passo a ser feito é adicionar os argumentos na linha de comando
DNA = 'CGTCGTCGCCGCCGCCGCCATGTCGGGAGGTGGTGTGATCCGTGGCCCGACGAAAAAAAAAAAAAGCGGGGAACAACGACTGCCGCATCTACGTGTAAAAAAACGAAAAAAAAAAAAAAAAAAAA'
print('a sequência de DNA é', DNA)

N1 = DNA[0:19] 
print(N1, 'é a sequência N1')

N2 = DNA[0:49]
print(N2, 'é a sequência N2')

N3 = DNA[49:65]
print(N3, 'é a sequência N3')

N4 = DNA[49:98]
print(N4, 'é a sequência N4')

#Posteiormente, deve-se conferir se os dados estão corretos e se não há nenhum número inteiro maior que o tamanho da sequência de DNA
