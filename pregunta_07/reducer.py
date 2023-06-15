#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':
    list_of_lists = []
    for line in sys.stdin:
        line = line.strip()
        letra, fecha, numero = line.split("\t")
        new_list = [elem for elem in line.split("\t")]
        list_of_lists.append(new_list)
    
    for n in range(len(list_of_lists)):
        list_of_lists[n][2]=int(list_of_lists[n][2])
    
    for data in sorted(list_of_lists,key = lambda x: (x[0],x[2])):
        sys.stdout.write("{}   {}   {}\t\n".format(data[0], data[1],data[2]))