import random #importando a biblioteca random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101) #gerando um numero aleatorio entre 1 e 100
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nivel: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1, total_de_tentativas + 1): #range é para definir o intervalo que o loop for vai rodar através da variavel rodada, por isso não é necessário definir um valor para ela antes, pois ela assumirá o primeiro valor do range. É necessario colocar o +1 apos a variavel pois o ultimo valor é exclusivo, ou seja, a variavel rodada nao assumirá o último valor.
        print("Tentativa {} de {}".format(rodada, total_de_tentativas)) #substituir valores na string, onde tem {} entra o valor das variáveis, isso se chama "String interpolation"
        chute = input("Digite um numero entre 1 e 100: ")
        print("Voce digitou o numero ", chute)
        chute = int(chute)

        if(chute < 1 or chute > 100):
            print("Voce deve digitar um numero entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Voce acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Voce errou! O seu chute foi maior do que o numero secreto")
            elif(menor):
                print("Voce errou! O seu chute foi menor do que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute) #função ABS torna o número absoluto, se a subtração der -20, por exemplo, o valor da variavel será 20 apenas
            pontos = pontos-pontos_perdidos

    print("Fim do jogo")