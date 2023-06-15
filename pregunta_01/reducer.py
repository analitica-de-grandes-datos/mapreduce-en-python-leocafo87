#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import collections

if __name__ == '__main__':
  
    counter = collections.Counter()

    for line in sys.stdin:
        line = line.strip()
        key, val = line.split("\t")
        val=int(val)
        counter[key] += val

    for data in counter.items():
        sys.stdout.write("{}\t{}\n".format(data[0], data[1]))