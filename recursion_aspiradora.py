from tkinter import W

# Funcion para encontrar la lista mas larga. Esta funcion itera sobre el arreglo entregado para sacar el mejor recorrido
# en funcion de la posicion en la que empieza. Y restorna el arreglo mas largo dentro del diccionario que genera.
def longest_list(array):
    # Se generan las variables que se van a utilizar
    # list contiene el arreglo con los niveles de basura
    list = [[] for _ in range(len(array))]
    # pos contiene los indices de la respuesta
    pos = [[] for _ in range(len(array))]
    # Se agrega el primer valor de array en el primer sub arreglo y en pos
    list[0].append(array[0])
    pos[0].append(0)
    # Empieza a recorrer desde 1 por lo que ya agrego el 0.
    for i in range(1, len(array)):
        for j in range(i):
            # Compara con los valores anteriores buscando si es mayor. Esto lo va agregando a arreglos y sobreescribe los arreglos.
            if array[j] >= array[i] and len(list[j]) > len(list[i]):
                list[i] = list[j].copy()
                pos[i] = pos[j].copy()
        # Agrega los valores visitados      
        list[i].append(array[i])
        pos[i].append(i)
    # Busca el arreglo mas largo y guarda su indice en j
    j = 0
    for i in range(len(array)):
        if len(list[j]) < len(list[i]):
            j = i
 
    # Entrega los indices del camino mas largo
    return pos[j]
 
 
if __name__ == '__main__':
    # Importa el arreglo que se va a subir
    file = open(input("Suba la lista de salas: "))
    N_cuartos = file.readline()
    cuartos, basura = [], []
    # Genera dos arreglos, uno con los nombres y otro con los valores de basura
    for i in range(int(N_cuartos)):
        row = file.readline()
        row = row.split(",")
        cuartos.append(row[0])
        basura.append(int(row[1]))
    
    # utiliza la funcion mostrada para hallar la solucion
    pos = longest_list(basura)

    # Crea el archivo txt con la respuesta y agrega los valores
    res = open('result.txt', 'w+')
    res.write("%d \n" % len(pos))
    for i in range(len(pos)):
        res.write("%s, %d\n"% (cuartos[pos[i]],basura[pos[i]]))
        print(cuartos[pos[i]],basura[pos[i]])