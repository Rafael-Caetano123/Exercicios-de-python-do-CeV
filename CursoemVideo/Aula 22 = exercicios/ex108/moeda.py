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
