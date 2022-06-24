#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':

    curkey = None
    varCount = 0
    varSuma =0

    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:
            varSuma = varSuma + val
            varCount = varCount + 1
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, varSuma , varSuma/varCount))

            curkey = key
            varSuma = val
            varCount = 1

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, varSuma , varSuma/varCount))