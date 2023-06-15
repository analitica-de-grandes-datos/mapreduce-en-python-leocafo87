#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    cuenta=0
    suma=0.0
    
    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)
        
        if key == curkey:
         suma += val
         cuenta +=1
         promedio=suma/cuenta
        else:
            if curkey is not None:    
                sys.stdout.write("{}\t{}\t{}\n".format(curkey,float(suma),promedio))
                
            curkey = key
            suma = val
            cuenta = 1 
            promedio = suma/cuenta

    sys.stdout.write("{}\t{}\t{}\n".format(curkey,float(suma),promedio))