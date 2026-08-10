"""Crie um código em Python que teste se o site pudim está acessível pelo computador usado."""

import requests

try:
    requests.get('https://pudim.com.br/')
    print('\033[1;32mConsegui acessar o site pudim com sucesso!\033[m')

except requests.exceptions.RequestException:
    print('\033[1;31mO site pudim não está acessível no momento!')
