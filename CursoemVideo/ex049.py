"""Refaça o desafio 009, mostrando a tabuada de um número que o usúario escolher, só que agora usando um laço for."""

print ('\033[1;36m-=\033[m' * 11)
print ('\033[1;33m     Tabuada v.2\033[m')
print ('\033[1;36m-=\033[m' * 11)
num = int(input('Digite um número: '))
print()
for m in range(1, 11):
    print (f'{num} x {m} = {num * m}')