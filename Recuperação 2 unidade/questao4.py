'''
Escreva um programa que possui a seguinte lista: [['Uruguai', 'Alemanha', [20, 19]], ['Uruguai', 
'Portugal', [15, 17]], ['Alemanha', 'Portugal', [17, 18]]]. Essa lista indica o número de roubadas
de bola que cada time fez em cada jogo. Na lista acima, no jogo entre Uruguai e Alemanha, o Uruguai
fez 20 roubadas e a Alemanha fez 19. O programa deve apresentar na tela:

a) o total de roubadas de bola do campeonato
b) o time que fez mais roubadas
c) o time que fez menos roubadas
'''

jogos = [
    ['Uruguai', 'Alemanha', [20, 19]],
    ['Uruguai', 'Portugal', [15, 17]],
    ['Alemanha', 'Portugal', [17, 18]]
]  # lista de jogos

# valores iniciais
uruguai = 0
alemanha = 0
portugal = 0

# loop para verificar o total de roubadas de bola
for jogo in jogos:
    for i in range(2):
        if jogo[i] == 'Uruguai':  # verifica se o time da primeira posição é o uruguai
            uruguai += jogo[2][i]  # soma o valor da roubada
        elif jogo[i] == 'Alemanha':  # verifica se o time da segunda posição é a alemanha
            alemanha += jogo[2][i]  # soma o valor da roubada
        elif jogo[i] == 'Portugal':  # verifica se o time da terceira posição é o português
            portugal += jogo[2][i]  # soma o valor da roubada

print('Total de roubadas de bola:', uruguai +
      alemanha + portugal)  # soma as roubadas de bola

print('Time que fez mais roubadas:', 'Uruguai' if uruguai > alemanha and uruguai > portugal else 'Alemanha'
      if alemanha > uruguai and alemanha > portugal else 'Portugal')  # verifica quem fez mais roubadas
print('Time que fez menos roubadas:', 'Uruguai' if uruguai < alemanha and uruguai < portugal else 'Alemanha'
      if alemanha < uruguai and alemanha < portugal else 'Portugal')  # verifica quem fez menos roubadas
