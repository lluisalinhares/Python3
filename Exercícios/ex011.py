#Armazenando nomes e idades.

print("Armazenamento de nomes e idades de pessoas. ")

nomes = []
idades = []

while True:
    nome = input("Insira um nome. Para encerrar, digite fim ")
    if nome != 'fim':
        nomes.append(nome)
        idades.append(int(input("Insira a idade: ")))
    else:
        break

for i in range(len(nomes)):
    print(nomes[i], 'tem', idades[i], 'anos')


#Nesta segunda parte do script, vamos implementar uma pesquisa nos nomes e idades.

pesquisa = input("Insira um nome ou idade para pesquisar: ")

if pesquisa in nomes:
    for i in range(len(nomes)):
        if nomes[i] == pesquisa:
            print(idades[i])
elif pesquisa.isnumeric() and int(pesquisa) in idades:
    for i in range(len(idades)):
        if idades[i] == int(pesquisa):
            print(nomes[i])
else:
    print("Nenhum resultado encontrado")