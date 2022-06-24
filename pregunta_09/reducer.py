#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    lista = []

    for line in sys.stdin:
        key, variableUno, variableDos = line.split(",")
        variableDos = int(variableDos)

        lista.append((key, variableUno, variableDos))

        lista.sort(key=lambda x: x[2], reverse=False)

    for var in lista[:6]:
        sys.stdout.write("{}   {}   {}\n".format(var[0], var[1], var[2]))