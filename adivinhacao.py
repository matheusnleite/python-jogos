print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute = input("Digite o seu numero: ")

print("Voce digitou o numero ", chute)

chute = int(chute)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if(acertou):
    print("Voce acertou!")
else:
    if(maior):
        print("Voce errou! O seu chute foi maior do que o numero secreto")
    elif(menor):
        print("Voce errou! O seu chute foi menor do que o numero secreto")


print("Fim do jogo")