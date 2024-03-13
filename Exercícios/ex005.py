#Conversão de Temperaturas

#Entrada do valor(temperatura) inicial
temp_c = float(input("Digite a temperatura em Celsius: "))

#Converte o valor de Celsius para Fahrenheit
temp_f = 1.8 * temp_c + 32
#Converte de Celsius para Kevin
temp_k = temp_c + 273.15

#Imprime o resultado
print("Temperatura em Celsius: {:.2f}" .format(temp_c))
print("Temperatura em Fahrenheit:  {:.2f}" .format(temp_f))
print("Temperatura em Kevin: {:.2f}" .format(temp_k))