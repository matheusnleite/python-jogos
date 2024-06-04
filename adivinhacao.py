print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <=2 total_de_tentativas):
    print("Tentativa", rodada,"de", total_de_tentativas)
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
  
    rodada = rodada + 1

print("Fim do jogo")