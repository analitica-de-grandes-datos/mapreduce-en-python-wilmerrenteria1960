#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    varMaximo = 0
    varMinimo =0
    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:
            if key == curkey:
                if val > varMaximo:
                    varMaximo = val
                if val < varMinimo:
                    varMinimo = val

        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, varMaximo, varMinimo))

            curkey = key
            varMaximo = val
            varMinimo = val

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, varMaximo, varMinimo))