def celsius_k():
    celsius = float(input("Digite a temperatura:"))
    conversao = celsius + 273.15
    print("{:.1f}°K".format(conversao))
if(__name__ == "__main__"):
    celsius_k()