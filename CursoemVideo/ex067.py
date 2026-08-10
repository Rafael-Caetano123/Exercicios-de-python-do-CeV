"""Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo."""

print('\033[1;33m=-\033[m' * 15)
print('\033[1;36m       Tabuada V.3.0\033[m')
print('\033[1;33m=-\033[m' * 15)
while True:
    print('( Para encerrar digite um número negativo )')
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    print('-' * 40)
print('\033[1;32mPrograma encerrado com sucesso!\033[m')