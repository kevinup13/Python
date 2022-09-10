'''
Tabuada 2.0
Início 03/05/2021
Finalizado 12/05/2021
Atualizado 23/09/2022
'''
from time import sleep

print()
print("="*10, "MINHA PRIMEIRA TABUADA - PYTHON 2.0.", "="*10)

option = 0
# calculo
while option != 5:
    # Escolha do tipo de operação
    print('Escolha o número do operador:')
    print('[1] Soma [2] Subtração [3] Multiplicação [4] Divisão [5] Sair\n')

    option = int(input('>> Opção: '))

    if option <= 4:
        # Escolha do valor a ser calculado
        n1 = int(input('Insira o número a ser calculado: '))
        n2 = 0
        if option == 1:
            print(f'Tabuada de {n1} : Soma.')
            for calcular in range(1, 11):
                n2 += 1
                resultado = n1 + n2
                print('{} + {} = {}'.format(n1, n2, resultado))

        elif option == 2:
            print(f'Tabuada de {n1} : Subtração.')
            for calcular in range(1, 11):
                n2 += 1
                resultado = n1 - n2
                print('{} - {} = {}'.format(n1, n2, resultado))

        elif option == 3:
            print(f'Tabuada de {n1} : Mutiplicação.')
            for calcular in range(1, 11):
                n2 += 1
                resultado = n1 * n2
                print('{} x {} = {}'.format(n1, n2, resultado))

        elif option == 4:
            print(f'Tabuada de {n1} : Divisão.')
            for calcular in range(1, 11):
                n2 += 1
                resultado = n1 / n2
                resultado = ('{:.2f}'.format(resultado))
                print('{} / {} = {}'.format(n1, n2, resultado))

    elif option == 5:
        print('Finalizando programa...')

    elif option > 5:
        print('Opção inválida! Tente novamente.')
    elif option != int():
        print('Opção inválida!.')

    print('--' * 30)
    sleep(1)

print("Fim do pragrama!\n")
