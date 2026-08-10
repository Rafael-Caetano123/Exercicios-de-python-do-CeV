"""Escreva um programa que pergunte o sálario de um funcionário e calcule o valor do seu aumento.
Para sálarios superiores a R$1.250,00 calcule o aumento de 10%
Para os inferiores ou iguais, o aumento é de 15%."""

salario = float(input('Qual o sálario do funcionário? R$'))
a1 = ((10/100) * salario) + salario
a2 = ((15/100) * salario) + salario
if salario <= 1250:
    print (f'O sálario do funcioário com aumento de \033[0;32m15%\033[m será de \033[0;36mR${a2:.2f}')
else:
    print (f'O sálario do funcionário com aumento de \033[0;32m10%\033[m será de \033[0;36mR${a1:.2f}')