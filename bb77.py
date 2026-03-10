import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def hacer_cuadrado(lado):
    print("Haciendo un cuadrado en 3D")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = [0, lado, lado, 0, 0]
    y = [0, 0, lado, lado, 0]
    z = [0, 0, 0, 0, 0]

    ax.plot(x, y, z)

    ax.set_title("Cuadrado en 3D")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    plt.show()


def hacer_rectangulo(base, altura):
    print("Haciendo un rectángulo en 3D")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = [0, base, base, 0, 0]
    y = [0, 0, altura, altura, 0]
    z = [0, 0, 0, 0, 0]

    ax.plot(x, y, z)

    ax.set_title("Rectángulo en 3D")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    plt.show()


def hacer_circulo(radio):
    print("Haciendo un círculo en 3D")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    theta = np.linspace(0, 2*np.pi, 100)

    x = radio * np.cos(theta)
    y = radio * np.sin(theta)
    z = np.zeros(100)

    ax.plot(x, y, z)

    ax.set_title("Círculo en 3D")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    plt.show()


def hacer_triangulo(base, altura):
    print("Haciendo un triángulo en 3D")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = [0, base, base/2, 0]
    y = [0, 0, altura, 0]
    z = [0, 0, 0, 0]

    ax.plot(x, y, z)

    ax.set_title("Triángulo en 3D")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    plt.show()


print("FIGURAS GEOMÉTRICAS")
print("1. Cuadrado")
print("2. Rectángulo")
print("3. Círculo")
print("4. Triángulo")

opcion = int(input("Elige una opción: "))

if opcion == 1:
    lado = float(input("Ingrese el lado: "))
    area = lado * lado
    print("Área del cuadrado:", area)
    hacer_cuadrado(lado)

elif opcion == 2:
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))
    area = base * altura
    print("Área del rectángulo:", area)
    hacer_rectangulo(base, altura)

elif opcion == 3:
    radio = float(input("Ingrese el radio: "))
    area = 3.1416 * radio * radio
    print("Área del círculo:", area)
    hacer_circulo(radio)

elif opcion == 4:
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))
    area = (base * altura) / 2
    print("Área del triángulo:", area)
    hacer_triangulo(base, altura)

else:
    print("Opción no válida")