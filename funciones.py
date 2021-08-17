import math
# ERR3x2 -3 : EL error se debe RETORNAR, ustedes solo lo estan imprimiendo
#         a su vez el codigo de verify no pone el try except dentro del
#         ciclo for


def multiple_op(X):
    """
    Nombre de la función y esta recibe un solo parámetro
    X que tiene que ser un número y a su vez retorna
    una arrays con las operaciones realizadas
    """
    try:
        int(X)
        b = [X*X, 2**X, math.factorial(X)]  # Operaciones con parámetro X
    except ValueError:
        print("Error,debe ser número")
    return b


def verify_array_op(array):
    """
    Nombre de la función y esta recibe un solo parámetro array
    que todos sus elementos tienen que ser un número y a su vez
    retorna una arrays de arrays con las operaciones realizadas
    """
    c = []  # Array secundario
    b = []  # Array de arrays
    lon = len(array)  # Longitud del array recibido
    a = 0  # Servirá para comparar si los parámetros del array son números
    for i in range(0, lon):
        y = array[i]  # Asigna un valor del array a la variable
    try:
        int(y)
        a = a+1  # Si la condición se cumple se suma 1
    except ValueError:
        print("Error,deben ser números")
    if a == lon:
        for i in range(0, lon):
            X = array[i]  # Asigna un valor del array a la variable
            c = [X*X, 2**X, math.factorial(X)]  # Operaciones el parámetro X
            b.append(c)  # Agrega el arreglo c al arreglo de arreglos b
    else:
        print("Error,todos deben ser números")

    return b
