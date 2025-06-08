#----------------------------------FUNCIONES----------------------------------------------------------

#Primero agregamos la raiz que es el primer elemento, despues recursivamente vamos agregando a la izquierda 
# o derecha segun corresponda
def agregar_al_arbol(arbol, nodo):
    if arbol == []:
        return [nodo, [], []]
    
    raiz = arbol[0]
    
    if nodo < raiz:
        arbol[1] = agregar_al_arbol(arbol[1], nodo) #arbol [1] representa la izquierda
    else:
        arbol[2] = agregar_al_arbol(arbol[2], nodo) #arbol [2] representa la derecha
    return arbol

#Crea el arbol y por cada nodo de la lista llama a la funcion agregar para que lo agregue donde corresponda
def crear_arbol(nodos):
    arbol = [] #Empezamos con el arbol vacio 
    for nodo in nodos:
        arbol = agregar_al_arbol(arbol, nodo)
    return arbol


#FUNCIONES PARA IMPRIMIR RECORRIDOS
#Imprime primero la raiz, luego el subarbol izquierdo y por ultimo el subarbol derecho. 
def imprimir_preorden(arbol):
     if arbol != []:
        print(arbol[0], end=" ")
        imprimir_preorden(arbol[1])
        imprimir_preorden(arbol[2])

#Imprime primero el subarbol izquierdo, luego la raiz y por ultimo el subarbol derecho
def imprimir_inorden(arbol):
    if arbol != []:
        imprimir_inorden(arbol[1])
        print(arbol[0], end=" ")
        imprimir_inorden(arbol[2])

#Imprimero primero el subarbol izquierdo, luego el subarbol derecho y por ultimo la raiz.
def imprimir_postorden(arbol):
    if arbol != []:
        imprimir_postorden(arbol[1])
        imprimir_postorden(arbol[2])
        print(arbol[0], end=" ")

#FUNCIONES DE PROPIEDADES DE ARBOLES

#Sumamos 1 por cada nodo que se encuentre recursivamente
def peso(arbol):
    if arbol == []:
        return 0
    return 1 + peso(arbol[1]) + peso(arbol[2])

#Sumamos 1 de la raiz, mas la altura maxima encontrada de los subarboles
def altura(arbol):
    if arbol == []:
        return 0
    return 1 + max(altura(arbol[1]), altura(arbol[2]))

def informar_propiedades(arbol):
    print("--- PROPIEDADES DEL ÁRBOL ---")
    print(f"Peso del árbol (cantidad de nodos): {peso(arbol)}")
    print(f"Altura del árbol: {altura(arbol)}")
    print("Orden del árbol: 2 (es un árbol binario)")

#Funcion para buscar un numero en el arbol
def buscar(arbol, numero):
    if arbol == []: #Si el arbol esta vacio devuelve falso
        return False
    if arbol[0] == numero: #Si el numero es igual a la raiz devuelve verdadero
        return True
    elif numero < arbol[0]: #Si es menor a la raiz busca recursivamente en los subarboles izquierdos
        return buscar(arbol[1], numero)
    else:
        return buscar(arbol[2], numero) #Si es mayor a la raiz busca recursivamente en los arboles derechos