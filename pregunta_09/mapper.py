#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    for line in sys.stdin:
        data = line.strip()
        data = line.split()
        sys.stdout.write("{},{},{}\n".format(data[0], data[1], data[2]))