import random
import os
from sys import platform, exit

import listas
import senha

if 'linux' in platform:
    def clear(): os.system('clear')

if 'win' in platform:
    def clear(): os.system('cls')


def roteia(rt, lista, lista_num):
    count = 0
    convertido = dict()

    for c in lista:
        num = lista_num[c] + rt

        if num > (len(lista) - 1):
            num = count
            count += 1

        convertido[c] = num

    return convertido


def codifica(arqs):
    arqs_problem = []
    pwd = senha.iniciar_senha(1)
    random.seed(pwd)

    for arquivo in arqs:
        arq = open(arquivo, 'r')

        try:
            frases = arq.readlines()
        except UnicodeDecodeError:
            arqs_problem.append(arquivo)
            arq.close()
            continue

        arq.close()

        arq = open(arquivo, 'w')
        print(arquivo)
        for frase in frases:
            line = []
            for ch in frase:
                if ch in listas.alfabeto_lista:
                    rota = random.randint(1, 116)
                    convert_lista = roteia(rota, listas.alfabeto_lista, listas.alfabeto_num)
                    num = convert_lista[ch]
                    c = listas.alfabeto_lista[num]

                    rota = random.randint(1, 116)
                    runa = listas.alfabeto_runa[c]
                    convert_runa = roteia(rota, listas.runa_lista, listas.runa_num)
                    num = convert_runa[runa]
                    c = listas.runa_lista[num]
                else:
                    c = ch

                line.append(c)

            arq.write(''.join(line))

        arq.close()

        if arqs_problem:
            s = ' '

            for a in arqs_problem:
                s += a

            clear()
            print('Os arquivos {0} não foram convertidos.'.format(s))
            print('Provavelmente por estarem em uma codificação de caracteres diferente da utf-8\n')
            input('Pressione enter para continuar.')

    return
