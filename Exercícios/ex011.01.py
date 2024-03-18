#Este exercício faz uma implementação ao "ex011.py".

usuarios = {}          #As 2 listas foram substituidas por 1 dicionário.

while True:
    nome = input("Insira um nome. Para encerrar, digite fim ")
    if nome != 'fim':
        usuarios[nome] = int(input("Insira a idade "))
    else:
        break

for i in usuarios:
    print(i, 'tem', usuarios[i], 'anos')


#Esse algoritmo funciona perfeitamente, no entanto, do jeito que está, existe o problema dos nomes iguais,
#caso haja nomes repetidos, o valor do segundo nome substitui o do primeiro.

#A segunda parte ainda não foi mexida.

