#tener en cuenta
#todos los elems diferentes
#todos son positivos
#hay al menos 3 elementos pero la ultima posicion es el voto en blanco
#algun partido pasa el 3% y siempre hay forma de que se ocupen todos los cargos
def obtenerSenadoresEnProvincia(escrutinio:list[int]):
    id:int = 0
    first: int = 0
    second: int = 0
    while id < len(escrutinio)-1:
        if first < escrutinio[id]:
            second = first
            first = escrutinio[id]    
        
        if second < escrutinio[id] and escrutinio[id] < first:
            second = escrutinio[id]
            
        else:
            pass
        id = id + 1
    res = (first,second)
    return res

#pruebas 
#[123,44523,43,23456734] BIEN
#[10,9,1,1000] BIEN
#[10,11,9,12,0] BIEN
#[1,17,100,120,105,10000,1000000000000]