def celsius_f():
    celsius = float(input("Digite a temperatura:"))
    conversao = celsius * 1.8 + 32
    fahreneit = print("{:.1f}°F".format(conversao))
if(__name__ == "__main__"):
    celsius_f()