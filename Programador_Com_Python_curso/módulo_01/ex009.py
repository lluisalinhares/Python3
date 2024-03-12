#Definindo funções.
#O comando "def" é usado na definição de uma função.

#Função que imprime uma mensagem de parabéns.
def parabens():
    print("Parabens pra você\nNesta data querida\nMuitas felicidades\nMuitos anos de vida!")

parabens()

#Função que procura uma letra nas frases.
def temLetraU():
    frase = input("Digite uma frase: ")
    if "u" in frase:                    #O comando "in" serve para percorrer tudo que está dentro de "frase", caracter por caracter, verificando e procurando o elemento "u".
        print("Você utilizou a letra u")
    else:
        print("Você não utilizou a letra u")

temLetraU()

#Função que faz uma operação aritmética recebendo 2 valores como parâmetro.
def somaQuadrados(a,b):
    somaQ = a**2 + b**2
    return somaQ

somaQuadrados(2,3)



#O comando "in" serve para percorrer tudo que está dentro de "frase",
# caracter por caracter, verificando e procurando o elemento "u".