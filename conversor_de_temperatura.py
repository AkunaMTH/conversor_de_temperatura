from Celsius import celsius_para_fahrenheit, celsius_para_kelvin
from Fahrenheit import fahrenheit_para_celsius, fahrenheit_para_kelvin
from Kelvin import  kelvin_para_fahrenheit, kelvin_para_celsius

#Variáveis
temp = 0
celsius = 1
fahrenheit = 2
kelvin = 3

#Inicio do programa
print("Conversor de temperatura")
escolha_do_usuario = int(input("Quer converter em qual escala? Celsius(1) Fahrenheit(2) Kelvin(3) "))

#Celsius
if escolha_do_usuario == celsius:
    temp = int(input("Para qual escala? Fahrenheit(1) Kelvin (2) "))
    if temp == 1:
        celsius_para_fahrenheit.celsius_f()
    else:
        celsius_para_kelvin.celsius_k()

#Fahrenheit
if escolha_do_usuario == fahrenheit:
    temp = int(input("Para qual escala? Celsius(1) Kelvin (2) "))
    if temp == 1:
        fahrenheit_para_celsius.celsius()
    else:
        fahrenheit_para_kelvin.fahrenheit_para_kelvin()

#Kelvin
if escolha_do_usuario == kelvin:
    temp = int(input("Para qual escala? Fahrenheit(1) Celsius (2) "))
    if temp == 1:
        kelvin_para_celsius.kelvin_para_celsius()
    else:
        kelvin_para_fahrenheit.kelvin_para_fahrenheit()
