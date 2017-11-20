import os
from sys import platform, exit

import listas

if 'linux' in platform:
    def clear(): os.system('clear')

if 'win' in platform:
    def clear(): os.system('cls')


def iniciar_senha(c):
    """
    Verifica se a senha possui carcteres validos de acordo com senha_lista em listas.py

    :param pwd: a senha
    :return: a senha
    """
    count = 0
    senha = 'senha'
    while count != len(senha):
        clear()

        if c == 1:
            print('Você deve entrar com uma senha contendo letras ou números.\nEsta será a senha que você vai usar para'
                  ' decodificar seu arquivo.\n')

        senha = input("Entre com a senha: ")

        for ch in senha:
            if ch not in listas.senha_lista:
                if ch not in listas.senha_lista:
                    print('\n*****************************************************************\n')
                    print('Caractere invalido: {0}'.format(ch))
                    print('A senha só deve ter letras, números, ou os símbolos @ # $ & ! ?.')
                    print('\n*****************************************************************\n')
                    input('Tecle enter para contiuar')
                    count = 0
                    break
            count += 1

    return senha
