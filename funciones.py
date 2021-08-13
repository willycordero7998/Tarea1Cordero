import math  # Importar la librería math ya que es necesaria para realizar las operaciones solicitadas


def multiple_op(X):  # Nombre de la función y esta recibe un solo parámetro X que tiene que ser un número
    try:  # Lleva al parámetro a anaálisis para ver si cumple la condición dada
        int(X)  # Condición que se busca que el parámetro cumpla, osea que sea un número
        b = [X*X, 2**X, math.factorial(X)]  # arreglo con las operaciones que deben hacerse con el parámetro X
    except ValueError:  # Tipo Excepción que se busca a la hora de probar la condición
        print("Error,debe ser número")  # Error que se menciona al Usuario
    return b  # Devuelve el arreglo con las operaciones hechas


def verify_array_op(array):  # Nombre de la función y esta recibe un solo parámetro array que todos sus elementos tienen que ser un número
    c = []  # Array que posteriormente va a contener las operaciones relaciones realizadas a cada uno de los elementos del array inicial recibido
    b = []  # Array que posteriormente va a ser el array de arrays
    lon = len(array)  # Lee la longitud del array recibido
    a = 0  # Variable que servirá para ver si todos lo parámetros del array son números
    for i in range(0, lon):  # Recorre todos lo parámtero del array inicial
        y = array[i]  # Asigna un valor del array a la variable
    try:  # Lleva al parámetro a anaálisis para ver si cumple la condición dada
        int(y)  # Condición que se busca que el parámetro cumpla
        a = a+1  # Si la condición se cumple se suma 1
    except ValueError:  # Tipo Excepción que se busca a la hora de probar la condición, osea que sea un número
        print("Error,deben ser números")  # Error que se menciona al Usuario
    if a == lon:  # Se comprueba que el arreglo inicial cumple que todos son números si el codigo pasa por el try las mismas veces que la cantidad de parámetros del arreglo
        for i in range(0, lon):  # Recorre todos lo parámtero del array inicial
            X = array[i]  # Asigna un valor del array a la variable
            c = [X*X, 2**X, math.factorial(X)]  # arreglo con las operaciones que deben hacerse con el parámetro X
            b.append(c)  # agrega el arreglo c al arreglo de arreglos b
    else:
        print("Error,todos deben ser números")  # Error que se menciona al Usuario

    return b  # Devuelve el arreglo con las operaciones hechas
