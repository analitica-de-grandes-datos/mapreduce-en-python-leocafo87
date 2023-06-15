#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        list_of_lists=[]
        line=line.replace('\n','')
        line=line.replace('\r','')
        index,letras = line.split('\t')
        letras=letras.split(',')
        
        for letra in letras:
            list_of_lists.append([index,letra])

        for pareja in list_of_lists:
            sys.stdout.write("{}\t{}\n".format(str(pareja[1]), str(pareja[0])))