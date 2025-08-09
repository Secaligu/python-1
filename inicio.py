print("Cuantas horas trabajas?")
horas_trabajadas = int(input("> "))

print("cuanto ganas por hora?")
costo_hora = int(input("> "))

ganacia_total = horas_trabajadas * costo_hora

print("tu ganacia total es de:")
print(ganacia_total)

print(f"teniendo en cuenta tus horas trabajadas:{horas_trabajadas}, y tu ganacias por hora es: {costo_hora} , tu ganacias total es de: {ganacia_total}$")

print("Eres Millonario causa" if costo_hora >= 100 else "chambea mas mi bro")