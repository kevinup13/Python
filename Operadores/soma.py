# My test in python
# entrada de dois numeros inteiros menores que dez
# repeticao de entrada de numero, caso o numero seja maior que dez
# soma dos numeros e impressao de resultado

print("\n=== Seja Bem vindo! ===\n")

while True:
    x = int(input("Digite o primeiro numero: "))
    y = int(input("Digite o segundo numero: "))
    soma = x + y
    if x > 10:
        print("⚠️  Digite um numero menor ou igual a 10 (dez)!\n")
    elif y > 10:
        print("⚠️  Digite um numero menor ou igual a 10 (dez)!\n")
    else:
        print(f'\nA soma de {x} e {y} é {soma}.')
        break
    print(">> Tente novamente! <<") 
print("---"*10)  
print('>> Fim da operação! <<\n')
