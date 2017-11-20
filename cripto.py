#!/usr/bin/env python3

import os
from sys import platform, exit

import codifica
import decodifica

if 'linux' in platform:
    os_sep = '/'

    def clear(): os.system('clear')

if 'win' in platform:
    os_sep = '\\'

    def clear(): os.system('cls')


def inicio_dir():
    clear()
    arqs = []

    dir_path = input('Entre com o caminho do diretório: ')

    if dir_path[-1] != os_sep:
        dir_path = dir_path + os_sep

    try:
        in_dir = os.listdir(dir_path)
    except FileNotFoundError:
        clear()
        print("O diretório {0} não foi encontrado".format(dir_path))
        input("Pressione qualquer tecla para continuar")

        return

    for a in in_dir:
        arq = dir_path + a

        if os.path.isfile(arq):
            arqs.append(arq)

    return arqs


def inicio_arq():
    clear()
    arqs = []

    arq = input('Entre com o nome e o caminho do arquivo: ')

    if os.path.isfile(arq):
            arqs.append(arq)
    else:
        clear()
        print("O arquivo {0} não foi encontrado".format(arq))
        s = input("Pressione qualquer tecla para continuar")
        return

    return arqs


def main():
    while True:
        clear()
        print('Entre com uma das opções abaixo\n')
        print('1 - Codificar um único arquivo')
        print('2 - Codificar um diretório')
        print('3 - Decodificar um único arquivo')
        print('4 - Decodificar um diretório')
        print('0 - Sair\n')

        op = int(input('Entre com sua opção: '))

        arquivos = []
        if op in (0, 1, 2, 3, 4):
            if op == 0:
                exit(0)
            elif op == 1 or op == 3:
                arquivos = inicio_arq()
            elif op == 2 or op == 4:
                arquivos = inicio_dir()

            if arquivos:
                if op == 1 or op == 2:
                    codifica.codifica(arquivos)
                elif op == 3 or op == 4:
                    decodifica.decodifica(arquivos)
        else:
            op = input("Opção invalida entre com zero(0) para sair ou qualquer outro valor para continuar: ")
            if op == '0':
                exit(0)


main()
