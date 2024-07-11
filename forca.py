def jogar(): #definindo a funcao para chama-la no outro codigo
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")
    palavra_secreta = "banana".upper()
    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):  #not é para negar a variavel
        chute = input("Qual letra? ")
        chute = chute.strip().upper()


        if(chute in palavra_secreta):
            index=0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    
    if(acertou):
        print("Voce ganhou!")
    else:
        print("Voce perdeu!")
    print("Fim do jogo")
    
if(__name__ == "__main__"): #se o codigo está sendo executado diretamente (sem ser chamado como função), o python seta o valor __main__ para a variavel __name__, então esse if é para executar a funcao jogar automaticamente somente se o codigo foi executado diretamente
    jogar()