import random

## Matriz 3x3
# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

class Matriz():
    VALOR_MINIMO = 1
    VALOR_MAXIMO = 10

    @staticmethod
    def generar_matrix(num_filas, num_columnas):
        matriz = [[random.randint(Matriz.VALOR_MINIMO, Matriz.VALOR_MAXIMO) for _ in range(num_columnas)] for _ in range(num_filas)]
        return matriz

    @staticmethod
    def inspeccionar_matrix(matriz):
        conteo = {}
        for fila in matriz:
            for numero in fila:
                if numero in conteo:
                    conteo[numero] += 1
                else:
                    conteo[numero] = 1
        
        unicos = sum(1 for count in conteo.values() if count == 1)
        repetidos = sum(1 for count in conteo.values() if count > 1)

        return [unicos, repetidos]

    @staticmethod
    def mostrar_matriz(matriz):
        for fila in matriz:
            print(fila)