import forca #se importarmos uma função mas nao chamarmos ela no codigo, ela será executada no inicio.
import adivinhacao

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