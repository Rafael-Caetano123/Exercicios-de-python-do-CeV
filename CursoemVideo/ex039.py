"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
-> Se ele ainda vai se alistar ao serviço militar.
-> Se é a hora de se alistar.
-> Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que já passou do prazo."""

from datetime import datetime
sexo = str(input('Qual seu sexo? (masculino ou feminino)? ')).upper()
if sexo == 'MASCULINO':
    atual = datetime.now().year
    nas = int(input('Qual seu ano de nascimento? '))
    idade = atual - nas
    if idade < 18:
        print ('Futuramente você irá se alistar no serviço militar')
        print (f'Ainda faltam {18 - idade} ano(s) até o alistamento')
    elif idade == 18:
        print ('Agora já é a hora de você se alistar no serviço militar!')
    else:
        print ('O prazo de alistamento já passou!')
        print (f'Já se passaram {idade - 18} ano(s) do prazo de alistamento!')
elif sexo == 'FEMININO':
    print ('Você não precisa se alistar, por conta do seu sexo')
else:
    print ('Resposta inconrrespondente!')