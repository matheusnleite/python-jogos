print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3


for rodada in range(1, total_de_tentativas + 1): #range é para definir o intervalo que o loop for vai rodar através da variavel rodada, por isso não é necessário definir um valor para ela antes, pois ela assumirá o primeiro valor do range. É necessario colocar o +1 apos a variavel pois ele o ultimo valor é exclusivo, ou seja, a variavel rodada nao assumirá o último valor.
    print("Tentativa {} de {}".format(rodada, total_de_tentativas)) #substituir valores na string, onde tem {} entra o valor das variáveis, isso se chama "String interpolation"
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