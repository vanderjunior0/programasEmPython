# faça um programa que receba três notas e os respectivos pesos calcule e mostre a média ponderada.

nota1 = int(input( ' Digite sua nota: '))
nota2 = int(input( ' Digite sua outra nota: '))
nota3 = int(input( ' Digite sua ultima nota: '))
peso1 = int(input( ' Digite o peso da nota 1: '))
peso2 = int(input( ' Digite o peso da nota 2: '))
peso3 = int(input( ' Digite o peso da nota 3: '))

soma1 = nota1+nota2+nota3+peso1+peso2+peso3
soma2 = peso1+peso2+peso3
media = soma1/soma2

print( ' Sua media ponderada e: ' , media)
