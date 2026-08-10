def metade(n):
    res_met = n / 2
    return res_met


def dobro(n):
    res_dob =  n * 2
    return res_dob


def aumentando(n, porc):
    res_aum = n + (n * porc / 100)
    return res_aum


def reduzindo(n, porc):
    res_dim = n - (n * porc / 100)
    return res_dim


def moeda(p=0, f=0):
    return f'R${p:.2f}'.replace('.', ',')



def resumo(p=0, porc_aum=0, porc_red=0):
    print('-=' * 15)
    print('       RESUMO DO VALOR')
    print('-=' * 15)
    print(f'Preço analisado:{moeda(p):>12}')
    print(f'Dobro do preço:{moeda(dobro(p)):>14}')
    print(f'Metade do preço:{moeda(metade(p)):>12}')
    print(f'{porc_aum:.0f}% de aumento:{moeda(aumentando(p, porc_aum)):>13}')
    print(f'{porc_red:.0f}% de redução:{moeda(reduzindo(p, porc_red)):>13}')
    print('-=' * 15)
