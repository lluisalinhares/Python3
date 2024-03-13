#Calculadora simples

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
operacao = input("Digite a operação (+, -, *, /): ")

resultado = num1

if operacao == "+":
    resultado += num2
elif operacao == "-":
    resultado -= num2
elif operacao == "*":
    resultado *= num2
elif operacao == "/":
    resultado /= num2
else:
    print("Operação não reconhecida")

print("O resultado da operação é: {:.1f}" .format(resultado))