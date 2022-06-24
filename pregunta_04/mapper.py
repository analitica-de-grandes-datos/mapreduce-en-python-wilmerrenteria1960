#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        data = line.split(' ')
        sys.stdout.write("{},1\n".format(data[0]))