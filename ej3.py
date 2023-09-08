#tener en cuenta
#todos los elems diferentes
#todos son positivos
#hay al menos 3 elementos pero la ultima posicion es el voto en blanco
#algun partido pasa el 3% y siempre hay forma de que se ocupen todos los cargos
def obtenerSenadoresEnProvincia(escrutinio:list[int]):
    id:int = 0
    firstValor: int = 0 #en la posición cero va el valor, en la 1 la posición
    firstPosicion: int = 0
    secondValor: int = 0
    secondPosicion: int = 0
    while id < len(escrutinio)-1:
        if firstValor < escrutinio[id]:
            secondValor = firstValor
            secondPosicion = firstPosicion
            firstValor = escrutinio[id]
            firstPosicion = id
        else:
            pass
        
        if secondValor < escrutinio[id] and escrutinio[id] < firstValor:
            secondValor = escrutinio[id]
            secondPosicion = id
            
        else:
            pass
        id = id + 1
    res = (firstPosicion,secondPosicion)
    return res

#pruebas TODAS PASARON
#ej3.obtenerSenadoresEnProvincia([123,44523,43,23456734]) == (1,0)
#ej3.obtenerSenadoresEnProvincia([10,9,1,1000])  == (0,1) 
#ej3.obtenerSenadoresEnProvincia([10,11,9,12,0]) == (3,1)
#ej3.obtenerSenadoresEnProvincia([1,17,100,120,105,10000,1000000000000]) == (5,3)
#ej3.obtenerSenadoresEnProvincia([901,17,100,1500,105,100,1000]) == (3,0)
#ej3.obtenerSenadoresEnProvincia([901,8011,1000,150,10500,100,1000]) == (4,1)
#ej3.obtenerSenadoresEnProvincia([10000,8011,1000,150,9500,100,1000,121,213,222,21]) == (0,4)
#ej3.obtenerSenadoresEnProvincia([1000,8011,1000,150,9500,100,1000,121222,213,222,21]) == (7,4)
#ej3.obtenerSenadoresEnProvincia([1000,2011,9100,43,100,1000,2500,233,21]) == (2,6)