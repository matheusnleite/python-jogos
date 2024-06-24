import forca #se importarmos uma função mas nao chamarmos ela no codigo, ela será executada no inicio.
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo?"))

    if jogo == 1:
        print("Jogando forca")
        forca.jogar()#chamando a função jogar do codigo forca
    elif jogo == 2:
        print("Jogando adivinhação")
        adivinhacao.jogar()#chamando a função jogar do codigo adivinhacao

if(__name__ == "__main__"): #se o codigo está sendo executado diretamente (sem ser chamado como função), o python seta o valor __main__ para a variavel __name__, então esse if é para executar a funcao jogar automaticamente somente se o codigo foi executado diretamente
    escolhe_jogo()