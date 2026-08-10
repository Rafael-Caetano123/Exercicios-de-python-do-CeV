def metade(n=0, opc=False):
    res_met = n / 2
    if opc == True:
        return moeda(metade(n))
    else:
        return res_met


def dobro(n=0, opc=False):
    res_dob =  n * 2
    if opc == True:
        return moeda(dobro(n))
    else:
        return res_dob


def aumentando(n=0, porc=0, opc=False):
    res_aum = n + (n * porc / 100)
    if opc == True:
        return moeda(aumentando(n, porc))
    else:
        return res_aum


def reduzindo(n=0, porc=0, opc=0):
    res_dim = n - (n * porc / 100)
    if opc == True:
        return moeda(reduzindo(n, porc))
    else:
        return res_dim


def moeda(p=0, f=0):
    return f'R${p:.2f}'.replace('.', ',')
