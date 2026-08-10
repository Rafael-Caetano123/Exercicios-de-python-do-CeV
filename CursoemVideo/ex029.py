"""Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada KM acima do limite."""

v = int(input('Digite a velocidade do carro: '))
multa =  (v - 80) * 7.00
if v >80:
    print ('\033[1;31mVocê foi multado por excesso de velocidade!\033[m')
    print (f'O valor da multa foi de \033[4;33mR${multa:.2f}')
else:
    print ('\033[0;32mVocê esta dentro dos limites de velocidade :]\033[m')