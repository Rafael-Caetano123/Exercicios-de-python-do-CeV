"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela
não pode exceder 30% do salário ou então o empréstimo será negado."""

casa = float(input('Qual o valor da casa a ser comprada? R$'))
salario = float(input('Qual o salário mensal do comprador da casa? R$'))
ano = int(input('Em quantos anos irá pagar a casa? '))
prest = casa / (ano * 12)
if ((30/100) * salario) > prest:
    print ('\033[36m-\033[m' * 80)
    print (f'\033[1;32mEmpréstimo aprovado!\033[m O valor a ser pago da prestação mensal será de \033[0;33mR${prest:.2f}\033[m')
    print ('\033[36m-\033[m' * 80)
if ((30/100) * salario) < prest:
    print ('\033[36m-\033[m' * 85)
    print ('\033[1;31mEmpréstimo negado!\033[m O valor de prestação é superior a 30% do salário do comprador')
    print ('\033[36m-\033[m' * 85)