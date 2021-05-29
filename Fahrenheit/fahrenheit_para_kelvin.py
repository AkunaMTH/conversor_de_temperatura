def fahrenheit_para_kelvin():
    fahrenheit = float(input("Digite a temperatura:"))
    conversao = (fahrenheit - 32) / 1.8 + 273.15
    print("{:.1f}°K".format(conversao))
