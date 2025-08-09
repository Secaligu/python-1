"""
escribir un programa que pregunte por el nombre del usuario y por un numero entero. luego imprime en la pantalla el nombre del usuario tantas veces como el numero introducido.

Input:
 juan
 5
    
output:
    juanjuanjuanjuanjuan
    
"""

print("ingresa tu nombre")
nombre = str(input("> "))

print("numeros que se repita")
n_repitan = int(input(">"))

print(nombre * n_repitan)