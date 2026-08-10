"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
Á vista dinheiro/cheque: 10% de desconto
Á vista no cartão: 5% de desconto
2x no cartão: preço normal
3x ou mais no cartão: 20% de juros"""

compras = float(input('Valor das compras: R$'))
print ('-' * 30)
print ('FORMAS DE PAGAMENTO')
print ('[ 1 ] á vista dinheiro/cheque')
print ('[ 2 ] á vista no cartão')
print ('[ 3 ] 2x no cartão')
print ('[ 4 ] 3x ou mais no cartão')
print ('-' * 30)
opção = int(input('Qual opção você escolhe? '))
if opção == 1:
    print (f'Sua compra de R${compras:.2f} irá passar a custar R${compras - ((10/100) * compras):.2f}')
elif opção == 2:
    print (f'Sua compra de R${compras:.2f} irá passar a custar R${compras - ((5/100) * compras):.2f}')
elif opção == 3:
    print (f'Sua compra de R${compras:.2f} será parcelada em 2x de R${compras/2:.2f}')
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    if parcelas > 2:
        print (f'Sua compra será parcelada em {parcelas}x de R${(((20/100) * compras) + compras) / parcelas:.2f} COM JUROS')
        print (f'Sua compra de R${compras:.2f} passará a custar R${compras + ((20/100) * compras):.2f} ')
    else:
        print('\033[1;31mQuantidades de parcelas inválida!\033[m')
elif opção != 1 or 2 or 3 or 4:
    print ('\033[1;31mopção inválida!')