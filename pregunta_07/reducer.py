#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    for line in sys.stdin:
        data = line.split(",")
        sys.stdout.write("{}   {}   {}\n".format(data[0].strip(),data[2].strip(), int(data[1].strip())))