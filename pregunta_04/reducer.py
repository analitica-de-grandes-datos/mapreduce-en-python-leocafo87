#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import collections
if __name__ == '__main__':
    counter = collections.Counter()
    for line in sys.stdin:
        key, val = line.split("\t")
        val=int(val)
        counter[key] += val
    for data in sorted(counter.items(),key = lambda x: x[0]):
        sys.stdout.write("{},{}\n".format(data[0], data[1]))