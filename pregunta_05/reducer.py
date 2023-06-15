#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import collections
val=1
if __name__ == '__main__':
    counter = collections.Counter()
    for line in sys.stdin:
        line = line.strip()
        año, mes, dia = line.split("-")
        counter[mes] += val
    for data in sorted(counter.items(),key = lambda x: x[0]):
        sys.stdout.write("{}\t{}\n".format(data[0], data[1]))