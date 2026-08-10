"""Crie um programa onde o usuário possa digitar cinco valores numéricos em cadastre-os em uma lista, já na posição correta de inserção
(sem usar o .sort()). No final mostre a lista ordenada na tela."""

valores = list()
# numero 0
num = int(input('Digite um valor: '))
valores.append(num)
print('Adicionado ao final da lista...')

#numero 1
num = int(input('Digite um valor: '))
if num > valores[0]:
    valores.append(num)
    print('Adicionado ao final da lista...')
elif num == valores[0]:
    valores.append(num)
    print('Adicionado ao final da lista...')
else:
    if num < valores[0]:
        valores.insert(0,num)
        print('Adicionado na posição 0 da lista...')

# numero 2
num = int(input('Digite um valor: '))
if num <= valores[0]:
    valores.insert(0,num)
    print('Adicionado na posição 0 da lista...')
elif num >= valores[1]:
    valores.append(num)
    print('Adicionado ao final da lista...')
else:
    if num > valores[0] and num < valores[1]:
        valores.insert(1,num)
        print('Adicionado na posição 1 da lista...')

#numero 3
num = int(input('Digite um valor: '))
if num <= valores[0]:
    valores.insert(0,num)
    print('Adicionado na posição 0 da lista...')
elif num > valores[0] and num <= valores[1]:
    valores.insert(1,num)
    print('Adicionado na posição 1 da lista...')
elif num > valores[1] and num < valores[2]:
    valores.insert(2,num)
    print('Adicionado na posição 2 da lista...')
else:
    if num > valores[2]:
        valores.append(num)
        print('Adicionado ao final da lista...')

#numero 4
num = int(input('Digite um valor: '))
if num <= valores[0]:
    valores.insert(0,num)
    print('Adicionado na posição 0 da lista...')
elif num > valores[0] and num <= valores[1]:
    valores.insert(1,num)
    print('Adicionado na posição 1 da lista...')
elif num > valores[1] and num <= valores[2]:
    valores.insert(2,num)
    print('Adicionado na posição 2 da lista...')
elif num > valores[2] and num < valores[3]:
    valores.insert(3,num)
    print('Adicionado na posição 3 da lista...')
else:
    if num > valores[3]:
        valores.append(num)
        print('Adicionado ao final da lista...')
print('=-' * 30)
print(f'Os valores digitados em ordem foram {valores}')
