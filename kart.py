import matplotlib.pyplot as plt
from matplotlib.patches import circulo

def hacer_cuadrado(lado)
    print("haciendo cuadrado")
    x = [0, lado,lado,0,0]
    y = [0, lado,lado,0,0]
    

def hacer_rectangulo()
    print("haciendo rectangulo")
def hacer_circulo()
    print("haciendo circulo")
def hacer_triangulo()
    print("haciendo triangulo")

print("FIGURAS GEOMÉTRICAS")
print("1. cuadrado")
print("2. rectángulo")
print("3. círculo")
print("4. triángulo")

try:
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        print("\nHas elegido hacer un cuadrado")

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