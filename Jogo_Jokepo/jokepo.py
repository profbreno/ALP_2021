import random
'''
Desafio para próxima semana:
Modificar o jogo para o clássico "Pedra-papel-tesoura-lagarto-Spock", do premiado
seriado "The Big Bang Theory"
Referência: https://pt.wikipedia.org/wiki/Pedra-papel-tesoura-lagarto-Spock
'''


def escolhaTipoDeJogo():
    print("=-" * 30)
    print("Bem-vindos ao JO KE PO!")
    print("=-" * 30)
    print("Escolha sua opção: 1. Campeonato / 2. Jogo Avulso")
    escolha = int(input())
    if escolha == 1:
        campeonato()
    elif escolha == 2:
        avulsa()


def campeonato():
    print("=-" * 30)
    print("Bem-vindos ao campeonato!")
    print("=-" * 30)
    partidas = []
    user = 0
    pc = 0
    for i in range(0, 3):
        ganhador = jogo()
        partidas.append(ganhador)
    for partida in partidas:
        if partida == 'win':
            user = user + 1
        elif partida == 'lose':
            pc = pc + 1
    print("=" * 30)
    print("PLACAR FINAL")
    print("=" * 30)
    print(f"Usuário {user} x {pc} Computador")
    print("-" * 30)


def avulsa():
    print("=-" * 30)
    print("Bem-vindos a partida avulsa!")
    print("=-" * 30)
    jogo()


def jogo():
    print("Escolha sua opção")
    print("1: Pedra, 2: Tesoura 3: Papel")
    pc = random.randint(1, 3)
    user = int(input())
    # win = user Ganhou / lose = PC ganhou / empate
    print("+-" * 30)
    print("JO", end=" ")
    for i in range(1, 1000000):
        print("", end="")
    print("KE", end=" ")
    for i in range(1, 1000000):
        print("", end="")
    print("PO", end=" ")
    for i in range(1, 1000000):
        print("", end="")
    print()
    print("+-" * 30)
    ganhador = compara(user, pc)
    print()
    winner(ganhador)
    return ganhador


def winner(ganhador):
    if ganhador == "win":
        print("O usuário ganhou!")
    elif ganhador == "lose":
        print("O compudador ganhou!")
    else:
        print("Houve um empate!")


def compara(opUser, opPc):
    if opUser == 1:
        print("O usuário digitou Pedra!")
        if opPc == 1:
            print("O PC digitou Pedra!")
            return "empate"
        elif opPc == 2:
            print("O PC digitou Tesoura!")
            return "win"
        else:
            print("O PC digitou Papel!")
            return "lose"
    elif opUser == 2:
        print("O usuário digitou Tesoura!")
        if opPc == 1:
            print("O PC digitou Pedra!")
            return "lose"
        elif opPc == 2:
            print("O PC digitou Tesoura!")
            return "empate"
        else:
            print("O PC digitou Papel!")
            return "win"
    elif opUser == 3:
        print("O usuário digitou Papel!")
        if opPc == 1:
            print("O PC digitou Pedra!")
            return "win"
        elif opPc == 2:
            print("O PC digitou Tesoura!")
            return "lose"
        else:
            print("O PC digitou Papel!")
            return "empate"
    else:
        return "errado"


def main():
    jogar = True
    while(jogar):
        escolhaTipoDeJogo()
        ent = int(input("Digite 1 para jogar de novo ou qualquer "
                        "outro número para encerrar."))
        if ent != 1:
            jogar = False
    print("Fim de jogo!")


main()
