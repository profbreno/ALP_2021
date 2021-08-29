'''
Vamos jogar dados? Supondo que um dado é jogado 65 vezes, e o seu valor é armazenado em uma
lista. Faça um programa que simule o lançamento do dado e determine o percentual de ocorrências
de cada face do dado dentre esses 65 lançamentos.
'''

import random


def ramdom_dado():
    '''
    Função que retorna um valor aleatório entre 1 e 6
    '''
    return random.randint(1, 6)


dados = [0] * 6  # Cria uma lista com 6 posições

# Vamos jogar o dado
for i in range(65):
    # Acessa a posição da lista e incrementa o valor
    dados[ramdom_dado() - 1] += 1

# Imprimimos o resultado
for i in range(6):
    # porcentagem de cada face
    print(f'Face {i + 1} - {dados[i] / 65 * 100:.2f}%')
