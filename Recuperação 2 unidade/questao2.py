'''
Um estacionamento cobra uma taxa mínima de R$2,00 para estacionar por três horas. Um adicional de
R$0,50 por hora não necessariamente inteira é cobrado após as três primeiras horas. O valor máximo
para qualquer dado período de 24 horas é R$10,00. Suponha que nenhum carro fica estacionado por
mais de 24 horas por vez. Escreva um aplicativo que calcule e exiba as taxas do estacionamento para
cada cliente que estacionou nessa garagem ontem. Você deve inserir as horas de estacionamento para
cada cliente. O programa deve exibir a cobrança para o cliente atual e calcular e exibir o total
recebido no final do dia. O programa deve usar uma função valorAPagar para determinar a cobrança
para cada cliente.
'''


def valorAPagar(horas):
    '''
    Calcula o valor a ser pago por hora
    '''
    if horas <= 3:  # Valor minimo de 2,00
        return 2
    elif horas > 3 and horas < 20:  # Valor adicional de 0,50 por hora
        return 2 + (horas - 3) * 0.5  # Valor minimo de 2,00 + 0,50
    else:  # Valor maximo de 10,00
        return 10


total = 0  # Inicializa o total a ser pago
clientes = True  # Inicializa o loop de entrada de dados

# Loop para receber os dados
while clientes:
    # Recebe a quantidade de horas
    horas = int(input('Horas de estacionamento: '))
    if horas == 0:  # Se o cliente desejar parar o programa
        clientes = False  # Sair do loop
    else:  # Se não, calcular o valor a ser pago
        print('Valor da cobrança: R$ {:.2f}'.format(
            valorAPagar(horas)))  # Imprimir o valor
        total += valorAPagar(horas)  # Acumular o valor

print("Total recebido: R$ {:.2f}".format(total))  # Imprimir o total
