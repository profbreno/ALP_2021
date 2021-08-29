'''
Sabe-se que a cultura de uma certa bactéria dobra seu volume a cada dia.
Dados um número de dias n (inteiro) e um volume v (ponto flutuante), qual
deve ser o volume inicial para que em n dias se obtenha, pelo menos, um volume v desta cultura?
'''


n = int(input("Digite o número de dias: "))  # número de dias
v = float(input("Digite o volume final: "))  # volume final

for i in range(n):  # loop para cada dia
    v = v / 2  # volume inicial é o volume final dividido por 2 a cada dia

# imprime o valor inicial da bactéria
print(f"O valor inicial da bactéria é {v}")
