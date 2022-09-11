# faça um programa que receba o salário de um funcionário
# percentual de aumento calcule e mostre o valor do aumento e o novo salário.

sal = int(input(' digite seu salario: '))
pAumento = float(input(' digite o percentual de aumento do seu salrio: '))

novoSal = sal*pAumento+sal

print( ' Seu novo salario sera: ' , novoSal)