def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRRO: "{entrada}" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)
