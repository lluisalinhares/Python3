#Cálculo do IMC

peso = float(input("Digite o seu peso(Kg): "))
altura = float(input("Digite sua altura(m): "))
imc = peso / (altura * altura)

if imc <= 18.5:
    print("Abaixo do peso ideal.")
elif (imc >= 18.6) and (imc <= 24.9):
    print("Peso ideal")
elif (imc >= 25) and (imc <= 29.9):
    print("Acima do peso")
elif (imc >= 30) and (imc <= 34.9):
    print("Obesidade grau I")
elif (imc >= 35) and (imc <= 39.9):
    print("Obesidade grau II")
elif imc >= 40:
    print("Obesidade grau III")



