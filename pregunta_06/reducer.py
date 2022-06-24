#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':

    curkey = None
    varMinimo = 0
    varMaximo = 0 

    for line in sys.stdin:

        key, val = line.split("\t")
        val = int(val)

        if key == curkey:
            if val > varMaximo:
                varMaximo = val
            if val < varMinimo:
                varMinimo = val

        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\n".format(curkey, total))

            curkey = key
            varMaximo = val
            varMinimo = val


    sys.stdout.write("{}\t{}\n".format(curkey, varMaximo, varMinimo))