# faça um programa que receba o salário base de um funcionário calcule e mostre o salário a receber,
# sabendo-se que o funcionário tem gratificação de 5% sobre o salário-base
# e paga imposto de 7% também sobre o sálario base.

sal = float(input( ' digite seu salario: '))

grati = sal*0.05
imp = sal*0.07
salImposto = sal+grati-imp

print( ' o salario base de' ,sal ,'equivale ao salario final de' ,salImposto)