import random
import os
from sys import platform, exit

import listas
import senha

if 'linux' in platform:
    def clear(): os.system('clear')

if 'win' in platform:
    def clear(): os.system('cls')


def desroteia(rt, ch, lista, lista_num):
    count = 0

    num = lista_num[ch] - rt

    if num > (len(lista) - 1):
        num = count
        count += 1

    return lista[num]


def decodifica(arqs):
    pwd = senha.iniciar_senha(2)
    random.seed(pwd)

    for arquivo in arqs:

        try:
            arq = open(arquivo, 'r')
        except FileNotFoundError:
            clear()
            print('O arquivo {0} não foi encontrado\n'.format(arquivo))
            input("Pressione qualquer tecla para continuar")
            return

        try:
            frases = arq.readlines()
        except UnicodeDecodeError:
            arq.close()
            continue

        arq.close()

        arq = open(arquivo, 'w')

        for frase in frases:
            line = []
            for ch in frase:
                if ch in listas.runa_lista:
                    rota1 = random.randint(1, 116)
                    rota2 = random.randint(1, 116)
                    r = desroteia(rota2, ch, listas.runa_lista, listas.runa_num)
                    cr = listas.code_alfabeto[r]
                    c = desroteia(rota1, cr, listas.alfabeto_lista, listas.alfabeto_num)
                else:
                    c = ch

                line.append(c)

            arq.write(''.join(line))

        arq.close()

    return

