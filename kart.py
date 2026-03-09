def hacer_estrella():
    print("haciendo una estrella")
def hacer_rectangulo():
    print("haciendo un rectangulo")
def hacer_circulo():
    print("haciendo un circulo")
def hacer_triangulo():
    print("haciendo un triangulo")
def menu():
    print("FIGURAS GEOMÉTRICAS")
    print("1. estrella")
    print("2. Rectángulo")
    print("3. Círculo")
    print("4. Triángulo")
while True:
    menu()
    try:
        opcion = int(input("Elige una opción: \n"))
    if opcion == 1:
        print("\nHas elegido hacer un estrella")

    elif opcion == 2:
        print("\nHas elegido hacer un rectangulo")
  
    elif opcion == 3:
        print("\nHas elegido hacer un circulo")
   

    elif opcion == 4:
        print("\nHas elegido hacer un triangulo")
   

    else:
        print("Seleccione un número válido")

except ValueError:
    print("Debe ingresar un número válido")

