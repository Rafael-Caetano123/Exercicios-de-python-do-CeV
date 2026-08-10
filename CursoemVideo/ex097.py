"""Faça um programa que tenha uma funcção chamada escreva(), que recebe um texto qualquer como parâmetro
e mostre uma mensagem com tamanho adaptável.
Ex:                             Saida:
                                ~~~~~~~~~~~~~~
escreva('Olá Mundo!')             Olá Mundo!
                                ~~~~~~~~~~~~~~          """

def escreva(txt):
    tam_lin = '~' * (len(txt) + 4)
    print(tam_lin)
    print(f'  {txt}')
    print(tam_lin)


#Programa principal
escreva(txt = str(input(f'{"Escreva algo: "}')))