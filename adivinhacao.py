print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute = input("Digite o seu numero: ")

print("Voce digitou o numero ", chute)

chute = int(chute)

if(numero_secreto == chute):
    print("Voce acertou!")
else:
    print("Voce errou!")