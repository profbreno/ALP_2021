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
]

uruguai = 0
alemanha = 0
portugal = 0

for jogo in jogos:
    for i in range(2):
        if jogo[i] == 'Uruguai':
            uruguai += jogo[2][i]
        elif jogo[i] == 'Alemanha':
            alemanha += jogo[2][i]
        elif jogo[i] == 'Portugal':
            portugal += jogo[2][i]

print('Total de roubadas de bola:', uruguai + alemanha + portugal)
print('Time que fez mais roubadas:', 'Uruguai' if uruguai > alemanha and uruguai > portugal else 'Alemanha'
      if alemanha > uruguai and alemanha > portugal else 'Portugal')
print('Time que fez menos roubadas:', 'Uruguai' if uruguai < alemanha and uruguai < portugal else 'Alemanha'
      if alemanha < uruguai and alemanha < portugal else 'Portugal')
