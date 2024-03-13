#Contagem de letras e palavras na frase.

frase = input("Digite uma frase: ")
while frase == ' ':                                          #Em tese, este while implementa a melhoria do programa não interpretar como palavra quando o usuário
    frase = input("Por favor, insira ao menos uma letra: ")  #apenas apertar o enter, sem escrever nada. Ou seja, contaria como espaço(" "), atendendo a condição da linha 12,
                                                             #no entanto não seria uma palavra...

letras = 0
palavras = 1

for i in frase:
    if i == " ":
        palavras = palavras + 1 #recebe "+ 1" pois a cada espaço que a variável i encontra, significa que tem mais de uma palavra na frase.
    else:
        letras = letras + 1 #e então, se não é espaço, significa que é letra, então "+ 1" tbm.

print("Letras na frase: {}" .format(letras))
print("Palavras na frase: {}" .format(palavras))



#Este script tem ainda alguns "bugs" que, parando pra pensar, é possível encontrar;
#Mas, deixo aqui para futuras melhorias.

