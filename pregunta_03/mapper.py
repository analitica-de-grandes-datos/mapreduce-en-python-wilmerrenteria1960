#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    
    
    for line in sys.stdin:
        data = line.split(",")
        # se escribe la salida del archivo obteniendo la columna 2 separada por ,
        sys.stdout.write("{},{}\n".format(data[1],data[0].strip()))