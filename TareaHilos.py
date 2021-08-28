import multiprocessing
import time
import argparse

"""
Funciones CalcPate1 y CalcPote4 calculan la potencia
de una cantidad de números dada por el usuario y los
coloca en una lista
"""


def CalcPote1(X):
    Array = list()
    for i in range(X):
        Array.append(i**2)
    return Array


def CalcPote4(inicio, fin):
    Array2 = list()
    for i in range(inicio, fin):
        Array2.append(i**2)
    return Array2


if __name__ == '__main__':
    """
    Libreria argparse que permite la ejecución
    del programa con argumentos desde consola
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("X", help="X")
    parser.add_argument("Tipo", help="Tipo", nargs="?")
    args = parser.parse_args()
    Xint = int(args.X)
    if args.Tipo is None:
        Tipoint = 1
    else:
        Tipoint = int(args.Tipo)

    """
    Se toma el tiempo que tarda el
    calculo utilizando solo un hilo
    """
    start = time.time()
    Array = CalcPote1(Xint)
    end = time.time()
    tiempo1Hilo = end-start

    """
    Se crean variables y listas necesarias para repartir
    el prabajo entre los diferentes hilos a utilizar
    """
    nHilos = 4
    p = len(Array)//nHilos
    inicios = list()
    fines = list()
    inicio = 0
    fin = p
    for n in range(nHilos):
        inicios.append(inicio)
        fines.append(fin)
        inicio += p
        fin += p

    """
    Se toma el tiempo que tarda el calculo utilizando cuatro hilos
    Se utiliza la libreria multiprocessing para crear y utilizar
    la cantidad de hilos necesaria
    """
    start = time.time()
    hilos = list()
    for i in range(len(inicios)):
        hilo = multiprocessing.Process(target=CalcPote4,
                                       args=(inicios[i], fines[i],))
        hilos.append(hilo)
        hilo.start()
    for hilo in hilos:
        hilo.join()
    end = time.time()
    tiempo4Hilos = end - start

    """
    Si el segundo argumento dado desde consola es un 1 o no se dá,
    el tiempo obtenido se imprime en consola
    Si el segundo argumento dado desde consola es un 2, se crea un
    archivo txt donde se escriben los tiempos obtenidos
    """
    if Tipoint == 1:
        print("Tiempo con 1 hilo: " + str(tiempo1Hilo) + "s")
        print("Tiempo con 4 hilos: " + str(tiempo4Hilos) + "s")
    elif Tipoint == 2:
        archivo = open("Tiempos.txt", "w")
        archivo.write('Tiempo con 1 hilo= % ss \n' % tiempo1Hilo)
        archivo.write('Tiempo con 4 hilos= % ss' % tiempo4Hilos)
        archivo.close()
        print("Archivo generado")
    else:
        print("Tiempo con 1 hilo: " + str(tiempo1Hilo) + "s")
        print("Tiempo con 4 hilos: " + str(tiempo4Hilos) + "s")
