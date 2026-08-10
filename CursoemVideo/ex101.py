"""Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições"""

def voto(ano_nasc):
    from datetime import datetime
    idade = datetime.now().year - ano_nasc
    if idade < 16:
        return f'Com {idade} anos: Não vota!'
    elif idade >= 18 and idade <= 65:
        return f'Com {idade} anos: Voto obrigatório!'
    elif idade > 65 or idade >= 16 and idade < 18:
        return f'Com {idade} anos: Voto opcional!'


# Programa Principal
print('-=' * 16)
print(voto(int(input('Ano de nascimento: '))))
print('-=' * 16)
