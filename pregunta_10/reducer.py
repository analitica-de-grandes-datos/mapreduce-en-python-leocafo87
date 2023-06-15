#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
from itertools import groupby

if __name__ == '__main__':
    list_of_lists=[]
    for line in sys.stdin:  
        line=line.replace('\n','')
        new_list = [elem for elem in line.split("\t")]
        list_of_lists.append(new_list)        
        
        for n in range(len(list_of_lists)):
            list_of_lists[n][1]=int(list_of_lists[n][1])

    list_of_lists=sorted(list_of_lists,key = lambda x: (x[0],x[1]))
    nuevalista = [(k, list([e[1] for e in g])) for k, g in groupby(list_of_lists, lambda x:x[0])]
    
    for pareja in nuevalista:
        
        sys.stdout.write("{}\t{}\n".format(str(pareja[0]), str(pareja[1]).replace('[','').replace(']','').replace(' ','')))