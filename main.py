from matriz import Matriz
from pares import Pares

print("\n================================")
print("Ejercicio 01")
print("================================")
print("Generando una matriz de dimensiones 2x5 ...")
mi_matriz = Matriz.generar_matrix(2, 5)
print("\nMatríz generada:\n")
Matriz.mostrar_matriz(mi_matriz)
resultado = Matriz.inspeccionar_matrix(mi_matriz)
print(f"Resultado {resultado}")

print("\n================================")
print("Ejercicio 02")
print("================================")
print("n = 5 ...")
print(f"Resultado: {Pares.pares_que_suman_n(5)}")
