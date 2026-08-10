"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
-> Média abaixo de 5.0: REPROVADO
-> Média entre 5.0 e 6.9: RECUPERAÇÃO
-> Média 7.0 ou superior: APROVADO"""

n1 = float(input('Digite a primeia nota do aluno: '))
n2 = float(input('Agora digite a segunda nota: '))
m = (n1 + n2) / 2
if m < 5.0 :
    print (f'\033[1;31mALUNO REPROVADO! a média foi {m}\033[m')
elif 5.0 <= m <= 6.9:
    print (f'\033[1;33mALUNO DE RECUPERAÇÃO! a média foi {m}\033[m')
else:
    print (f'\033[1;32mALUNO APROVADO! a média foi {m}')