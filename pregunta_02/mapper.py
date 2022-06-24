#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

import sys
if __name__ == "__main__":
    #Se lee el archivo linea a linea
    for line in sys.stdin:
        data =line.split(',')
        sys.stdout.write("{}\t{}\n".format(data[3],data[4]))