""" Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
se (MCU), desarrollar un algoritmo que contemple lo siguiente:

a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
leano que indica si es un héroe o un villano, True y False respectivamente;
b. listar los villanos ordenados alfabéticamente;
c. mostrar todos los superhéroes que empiezan con C;
d. determinar cuántos superhéroes hay el árbol;
e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
encontrarlo en el árbol y modificar su nombre;
f. listar los superhéroes ordenados de manera descendente;
g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
los villanos, luego resolver las siguiente tareas:
    I. determinar cuántos nodos tiene cada árbol;
    II. realizar un barrido ordenado alfabéticamente de cada árbol. """


from arbol import (
    nodoArbol,
    insertar_nodo,
    preorden,
    inorden,
    postorden,
    por_nivel,
    busqueda,
    eliminar_nodo,
    inorden_datos,
    inorden_villano,
    inorden_empieza_con,
    inorden_heroes,
    postorden_heroes,
    crear_bosque,
)

arbol_mcu = nodoArbol()
arbol_mcu_villanos = nodoArbol()
arbol_mcu_heroes = nodoArbol()

# A
lista = [
    ['iron man', False],
    ['capiana marvel', False],
    ['thor', False],
    ['dotor strange', False],
    ['thanos', True],
    ['red skull', True],
    ['capitan america', False],
]


for nombre, villano in lista:
    datos = {'villano': villano}
    insertar_nodo(arbol_mcu, nombre, datos)

print('inorden arbol completo')
inorden(arbol_mcu)
print()

# B
print('inorden villanos')
inorden_villano(arbol_mcu)
print()

# C
print('inorden empieza con "C"')
inorden_empieza_con(arbol_mcu, 'c')
print()

# D
print('inorden heroes')
inorden_heroes(arbol_mcu)
print()

# E
clave = input('ingrese parte de lo que desea buscar: ')
inorden_empieza_con(arbol_mcu, clave)
print()
clave = input('ingrese el nombre que quiere modificar: ')
pos = eliminar_nodo(arbol_mcu, clave)

if pos is not None:
    name_nuevo = input('ingrese el nombre correcto: ')
    insertar_nodo(arbol_mcu, name_nuevo)
else:
    print('el nombre no esta en el arbol')
print()

inorden(arbol_mcu)
print()

# F
print('heroes en forma descendente')
postorden_heroes(arbol_mcu)
print()

# G
crear_bosque(arbol_mcu, arbol_mcu_villanos, arbol_mcu_heroes)

print('arbol villanos')
inorden(arbol_mcu_villanos)
print()

print('arbol heroes')
inorden(arbol_mcu_heroes)
print()
