#-----------------------------PROGRAMA PRINCIPAL------------------------------------------------------

from Funciones import crear_arbol
from Funciones import imprimir_preorden, imprimir_inorden, imprimir_postorden
from Funciones import informar_propiedades
from Funciones import buscar


print("BIENVENIDOS A ARBOLES BINARIOS DE BUSQUEDA CON PYTHON")
cantidad = int(input("¿Cuantos nodos queres que tenga tu arbol? "))
lista_nodos = []

# Usamos while porque no sabemos cuantas veces se va a ejecutar ya que puede haber repeticion de nodos. 
#Mientras la longitud de la lista arbol sea menor a la cantidad de nodos que debe tener, el arbol sigue pidiendo nodos.
while len(lista_nodos) < cantidad:                                
    nodo = int(input(f"Ingresa el nodo {len(lista_nodos) + 1} de tu árbol: "))
    #if para verificar si ese nodo ya se ingreso
    if nodo in lista_nodos:    
        print("Ese nodo ya existe. Ingresá un valor distinto.")
    else:
        lista_nodos.append(nodo)
print(f"Estos son los nodos de tu arbol: {lista_nodos}")


print("Ahora vamos a crear tu arbol binario de busqueda!")
arbol_creado = crear_arbol(lista_nodos)
print(f"Asi quedo tu arbol creado: {arbol_creado}")

#Preguntamos en que orden de recorrido quiere imprimir su arbol
opcion = int(input(
    "¿Cómo querés que recorra tu árbol?\n"
    "1. Preorden\n"
    "2. Inorden\n"
    "3. Postorden\n"
    "Ingresá el número de la opción seleccionada: "
))

#Verificamos que la opcion elegida sea posible.
while opcion != 1 and opcion != 2 and opcion != 3:
    print("Ingresa una opcion valida: ")
    opcion = int(input())

#Llamamos a la funcion de imprimir que corresponda segun la opcion elegida
if opcion == 1:
    print("El recorrido preorden de tu arbol es el siguiente: ")
    imprimir_preorden(arbol_creado)
elif opcion == 2:
    print("El recorrido inorden de tu arbol es el siguiente: ")
    imprimir_inorden(arbol_creado)
else: 
    print("El recorrido postorden de tu arbol es el siguiente: ")
    imprimir_postorden(arbol_creado)

#Mostramos propiedades del arbol creado
print("") #salto de linea
informar_propiedades(arbol_creado)

#Por ultimo pedimos un numero para buscar en el arbol creado 
numero_a_buscar = int(input("Ingresa un numero para buscar: "))
if buscar(arbol_creado, numero_a_buscar):
    print (f"El numero {numero_a_buscar} si se encuentra en el abol!")
else: 
    print(f"El numero {numero_a_buscar} no se encuentra en el abol!")