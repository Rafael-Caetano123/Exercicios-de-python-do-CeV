"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
-> Até 9 anos: INFANTIL
-> Até 14 anos: MIRIM
-> Até 19 anos: JUNIOR
-> Até 20 anos: SÊNIOR
-> Acima: MASTÊR"""

from datetime import datetime
nas = int(input('Digite o ano de nascimento do atleta: '))
ano_atual = datetime.now().year
idade = ano_atual - nas
print (f'O atleta tem {idade} anos')
if idade <= 9:
    print ('Categoria: INFANTIL')
elif idade > 9 and idade <= 14:
    print ('Categoria: MIRIM')
elif idade > 14 and idade <= 19:
    print ('Categoria: JUNIOR')
elif idade == 20:
    print ('Categoria: SÊNIOR')
elif idade > 20:
    print ('Categoria: MASTÊR')