print("FIGURAS GEOMÉTRICAS")
print("1. estrella")
print("2. Rectángulo")
print("3. Círculo")
print("4. Triángulo")

try:
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        print("\nHas elegido hacer un estrella")

    elif opcion == 2:
        print("\nHas elegido hacer un RECTÁNGULO")
  
    elif opcion == 3:
        print("\nHas elegido hacer un CÍRCULO")
   

    elif opcion == 4:
        print("\nHas elegido hacer un TRIÁNGULO")
   

    else:
        print("Seleccione un número válido")

except ValueError:
    print("Debe ingresar un número válido")