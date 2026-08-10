"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
Abaixo de 18.5: abaixo do peso
Entre 18.5 e 25: peso ideal
25 até 30: sobrepeso
30 até 40: obesidade
Acima de 40: obesidade mórbida"""

print ('\033[1;35m=-\033[m' * 15)
print ('\033[1;34m      Analisador de IMC\033[m')
print ('\033[1;35m=-\033[m' * 15)
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura * altura)
print ('-' * 30)
print (f'IMC: {imc:.1f}')
if imc < 18.5:
    print ('\033[1;33mVocê esta abaixo do peso recomendado!')
elif 18.5 < imc < 25:
    print ('\033[1;32mVocê esta no peso ideal!')
elif 25 < imc < 30:
    print ('\033[1;33mVocê esta com sobrepeso!')
elif 30 < imc < 40:
    print ('\033[1;33mVocê esta com obesidade!\033[m')
else:
    print ('\033[1;31mVocê esta com obesidade mórbida!!!')