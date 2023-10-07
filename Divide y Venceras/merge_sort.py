#Dividir el arreglo en mitades
def merge_sort(arreglo):
    #CASO BASE
    #Verificar que el elemento tiene un solo elemento el arreglo
    if len(arreglo) <= 1:
        return arreglo
    #DIVIDIR
    #Obtener la mitad
    mitad = len(arreglo)//2 #El // es para redondear ya que puede salir decimal
    izq = arreglo[:mitad] #Los : son para indicar que va de x para y, si solo estan los : automaticamente lo toma como 0
    der = arreglo[mitad:]

    #CONQUISTAR
    #Llamada recursiva
    izq = merge_sort(izq)
    der = merge_sort(der)

    #COMBINAR
    #Fusionar las soluciones recursivas
    return merge(izq,der)

def merge(izq,der):
    ordenado = []
    i_izq, i_der = 0, 0
    #Ciclo para comparar elementos
    while i_izq < len(izq) and i_der < len(der):
        if izq[i_izq]<der[i_der]:
            ordenado.append(izq[i_izq])
            i_izq += 1
        else:
            ordenado.append(der[i_der])
            i_der += 1 #Lo que tenga la variable le sumamos un 1 adicional
    #Agregar todos los elementos faltantes, si existen
    ordenado.extend(izq[i_izq:])
    ordenado.extend(der[i_der:])

    return ordenado
#Metodo para ejecutar el programa
if __name__ == '__main__':
    arreglo = [4, 2, 3, 1, 5, 7, 6, 8, 9]
    print("Arreglo desordenado: ", arreglo)
    ordenado = merge_sort(arreglo)
    print("Arreglo ordenado: ", ordenado)