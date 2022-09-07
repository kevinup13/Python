# Entrada de numero de jogos
# Cria uma lista com 15 numeros aleatórios
import random
import time

print("======"*10)
print("==="*8, " LOTOFÁCIL ", "==="*8)
print("======"*10)

jogo = 0
""" Insere a quantidade de jogos  """
numero_jogos = input("\n>> Digite o número de jogos: ")
print()
for linha in range(int(numero_jogos)):
    jogo += 1
    numeros = random.sample(range(1, 25), 15)
    for coluna in range(1):
        numeros = random.sample(range(1, 25), 15)
        print(f'>> Jogo {jogo}: ')
        print(numeros, end='')
    print()
    print("---"*20)
    time.sleep(1)

for n in range(1):
    print("==="*8, end='')
    for num in " Boa Sorte! ":
        print(num, flush=True, end='')
        time.sleep(0.3)
    print("==="*8)
