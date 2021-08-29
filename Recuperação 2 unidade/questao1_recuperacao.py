'''
Sabe-se que a cultura de uma certa bactéria dobra seu volume a cada dia.
Dados um número de dias n (inteiro) e um volume v (ponto flutuante), qual
deve ser o volume inicial para que em n dias se obtenha, pelo menos, um volume v desta cultura?
'''

# v = vi * 2 * 2 * 2 * 2
# vi = v / 2 / 2 / 2 / 2

# v = 30
# n = 2
# vi = 30 / 2 = 15

n = int(input("Digite o número de dias: "))
v = float(input("Digite o volume final: "))

for i in range(n):
    v = v / 2

print(f"O valor inicial da bactéria é {v}")
