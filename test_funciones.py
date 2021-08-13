import random  # Importar la librería random ya que es necesaria para realizar los números random
from funciones import multiple_op  # Importa la función multiple_op
from funciones import verify_array_op  # Importa la función verify_array_op


def test_funciones():  # Define una función tipo test
    z = 0  # Variable que servirá para ver si todos lo parámetros del array retornado por multiple_op son números
    x = 0  # Variable que servirá para ver si todos lo parámetros del array rebido verify_array_op en  son números
    a = random.randint(1, 6)  # Genera un número random con un intervalo de 1 a 6
    b = multiple_op(a)  # Variable que va a recibir lo que es retornado por la función
    c = verify_array_op([a, a])  # Variable que va a recibir lo que es retornado por la función
    lon = len(b)  # Lee la longitud del array b recibido
    lon1 = len(c)  # Lee la longitud del array c recibido
    for i in range(0, lon):  # Recorre el array retornado por multiple_op
        y = b[i]
    try:  # Lleva al parámetro a anaálisis para ver si cumple la condición dada
        int(y)  # Condición que se busca que el parámetro cumpla
        z = z+1  # Si la condición se cumple se suma 1
    except ValueError:  # Tipo Excepción que se busca a la hora de probar la condición, osea que sea un número
        print("Error,deben ser números")  # Error que se menciona al Usuario
    for i1 in range(0, lon1):  # Recorre el array c
        y1 = c[i1]  # Asigna un valor del array a la variable
        lon2 = len(y1)  # Lee la longitud del array y1 recibido
    for i2 in range(0, lon2):  # Recorre el array y1
        y2 = y1[i2]  # Asigna un valor del array a la variable
    try:  # Lleva al parámetro a anaálisis para ver si cumple la condición dada
        int(y2)  # Condición que se busca que el parámetro cumpla
        x = x+1  # Si la condición se cumple se suma 1
    except ValueError:  # Tipo Excepción que se busca a la hora de probar la condición, osea que sea un número
        print("Error,deben ser números")  # Error que se menciona al Usuario

    assert z == lon  # Se comprueba que el arreglo inicial cumple que todos son números si el codigo pasa por el try las mismas veces que la cantidad de parámetros del arreglo
    assert x == 6  # Se comprueba que el arreglo inicial cumple que todos son números si el codigo pasa por el try las mismas veces que la cantidad de parámetros del arreglo
