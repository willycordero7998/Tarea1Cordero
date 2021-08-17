import random
from funciones import multiple_op
from funciones import verify_array_op
# ERR4 -10
# ERR2x2 -5: Los test nunca prueban que los métodos den el resutlado correcto
# a su vez tienen los mismos problemas que en el codigo en cuanto al uso de
# try except
# Nota 72.72

def test_funciones():
    """
    Define una función tipo test que comprueba que en las funciones
    multiple_op y verify_array_op, que se reciben como entradas,
    los parametros de salida sean todos números
    """
    z = 0  # Servirá para verificar multiple_op
    x = 0  # Servirá para verificar verify_array_op
    a = random.randint(1, 6)
    b = multiple_op(a)  # Recibe lo retornado por la función
    c = verify_array_op([a, a])  # Recibe lo retornado por la función
    lon = len(b)  # Longitud del array b
    lon1 = len(c)  # Longitud del array c
    for i in range(0, lon):
        y = b[i]
    try:
        int(y)
        z = z+1  # Si la condición se cumple se suma 1
    except ValueError:
        print("Error,deben ser números")
    for i1 in range(0, lon1):
        y1 = c[i1]  # Asigna un valor del array a la variable
        lon2 = len(y1)  # Longitud del array y1
    for i2 in range(0, lon2):
        y2 = y1[i2]  # Asigna un valor del array a la variable
    try:
        int(y2)
        x = x+1  # Si la condición se cumple se suma 1
    except ValueError:
        print("Error,deben ser números")

    assert z == lon
    assert x == 6
    """
    Se comprueba que el arreglo inicial cumple que todos son
    números si el codigo pasa por el try las mismas veces que
    la cantidad de parámetros del arreglo
    Se comprueba que el arreglo inicial cumple que todos son
    números si el codigo pasa por el try las mismas veces que
    la cantidad de parámetros del arreglo
    """
