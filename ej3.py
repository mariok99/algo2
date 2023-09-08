#tener en cuenta
#todos los elems diferentes
#todos son positivos
#hay al menos 3 elementos pero la ultima posicion es el voto en blanco
#algun partido pasa el 3% y siempre hay forma de que se ocupen todos los cargos
def obtenerSenadoresEnProvincia(escrutinio:list[int]):
    id:int = 0
    first: int = [0,0] #en la posición cero va el valor, en la 1 la posición
    second: int = [0,0]
    while id < len(escrutinio)-1:
        if first[0] < escrutinio[id]:
            second[0] = first[0]
            second[1] = first[1]
            first[0] = escrutinio[id]
            first[1] = id  
        else:
            pass
        
        if second[0] < escrutinio[id] and escrutinio[id] < first[0]:
            second[0] = escrutinio[id]
            second[1] = id
            
        else:
            pass
        id = id + 1
    res = (first[1],second[1])
    return res

#pruebas 
#[123,44523,43,23456734] == (1,0) BIEN
#[10,9,1,1000]  == (0,1) BIEN
#[10,11,9,12,0] == (3,1) BIEN
#[1,17,100,120,105,10000,1000000000000] == (5,3)