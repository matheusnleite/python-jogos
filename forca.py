def jogar(): #definindo a funcao para chama-la no outro codigo
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")



    print("Fim do jogo")
    
if(__name__ == "__main__"): #se o codigo está sendo executado diretamente (sem ser chamado como função), o python seta o valor __main__ para a variavel __name__, então esse if é para executar a funcao jogar automaticamente somente se o codigo foi executado diretamente
    jogar()