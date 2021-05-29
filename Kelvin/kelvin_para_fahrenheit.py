def kelvin_para_fahrenheit():
    kelvin = float(input("Digite a temperatura:"))
    conversao = ((kelvin - 273.15) * (9 / 5)) + 32
    print("{:.1f}°K".format(conversao))
