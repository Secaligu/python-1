print("primer numero")
numero1 = float(input("> "))

print("segundo numero")
numero2 = float(input("> "))

suma = numero1 + numero2

resta = numero1 - numero2

multiplicacion = numero1 * numero2

if numero2 != 0:
 division = numero1 / numero2
 modulo = numero1 % numero2
else:
 division = "esta indefinido"
 modulo = "esta indefinido"
    

potenciacion = numero1 ** numero2




    

print(f"""
      suma {suma}
      resta {resta}
      multiplicacion {multiplicacion}
      division {division}
      potenciacion {potenciacion}
      modulo {modulo}
      """)