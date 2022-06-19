# Entrada de numero de jogos
# Cria uma lista com 15 numeros aleatórios

import random

print("======"*10)
print("==="*8, " LOTOFÁCIL ", "==="*8)
print("======"*10)

jogo = 0
numero_jogos = input("\n>> Digite o número de jogos: ")
print()
for l in range(int(numero_jogos)):
    jogo += 1
    numeros = random.sample(range(1,25),15)
    for c in range(1):
        numeros = random.sample(range(1,25),15)
        print(f'>> Jogo {jogo}: ')
        print(numeros, end='')    
    print()
    print("---"*20)   
print("==="*8,"Boa sorte!","==="*8)


