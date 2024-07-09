def jogar(): #definindo a funcao para chama-la no outro codigo
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")
    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):  #not é para negar a variavel
        chute = input("Qual letra? ")
        chute = chute.strip()

        index=0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(chute, index))
            index = index+1
        print("jogando...")
    

    print("Fim do jogo")
    
if(__name__ == "__main__"): #se o codigo está sendo executado diretamente (sem ser chamado como função), o python seta o valor __main__ para a variavel __name__, então esse if é para executar a funcao jogar automaticamente somente se o codigo foi executado diretamente
    jogar()