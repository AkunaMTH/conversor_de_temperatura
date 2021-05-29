def celsius():
    #Fahrenheit para Celsius
    fahrenheit = float(input("Digite a temperatura:"))
    conversao = (fahrenheit - 32) / 1.8
    print("{:.1f}°C".format(conversao))