"""Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso você deve mostrar, para cada palavra, quais são suas vogais"""

tupla = ('aprender', 'programar', 'linguagem', 'python',
         'curso', 'gratis', 'estudar', 'praticar',
         'trabalhar', 'mercado', 'programador', 'futuro')
for c in range(0, len(tupla)):
    quant_a = tupla[c].count('a')
    quant_e = tupla[c].count('e')
    quant_i = tupla[c].count('i')
    quant_o = tupla[c].count('o')
    quant_u = tupla[c].count('u')
    vogais = quant_a * "a" + quant_e * "e" + quant_i * "i" + quant_o * "o" + quant_u * "u"
    print(f'Na palavra "{tupla[c]}" temos as vogais: {" ".join(vogais)}')