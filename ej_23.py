""" 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
resuelva las siguientes consultas:
a. listado inorden de las criaturas y quienes la derrotaron;
b. se debe permitir cargar una breve descripción sobre cada criatura;
c. mostrar toda la información de la criatura Talos;
d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
e. listar las criaturas derrotadas por Heracles;
f. listar las criaturas que no han sido derrotadas;
g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
o dios que la capturo;
h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
Erimanto indicando que Heracles las atrapó;
i. se debe permitir búsquedas por coincidencia;
j. eliminar al Basilisco y a las Sirenas;
k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
derroto a varias;
l. modifique el nombre de la criatura Ladón por Dragón Ladón;
m. realizar un listado por nivel del árbol;
n. muestre las criaturas capturadas por Heracles. """


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
    inorden_empieza_con,
    derrotado_por_heracles,
    criaturas_no_derrotadas,
    modificar_criaturas_capturadas,
    criaturas_heracles,
    agregar_descripcion,
)

arbol_criaturas = nodoArbol()

criaturas = [
    {'criatura': 'ceto', 'derrotado_por': '', 'capturada': 'heracles'},
    {'criatura': 'tifon', 'derrotado_por': 'zeus', 'capturada': ''},
    {'criatura': 'equidna', 'derrotado_por': 'argos panoptes', 'capturada': ''},
    {'criatura': 'dino', 'derrotado_por': '', 'capturada': ''},
    {'criatura': 'prefedo', 'derrotado_por': '', 'capturada': ''},
    {'criatura': 'enio', 'derrotado_por': '', 'capturada': ''},
    {'criatura': 'escila', 'derrotado_por': '', 'capturada': ''},
    {'criatura': 'caribdis', 'derrotado_por': '', 'capturada': 'heracles'},
    {'criatura': 'euriale', 'derrotado_por': '', 'capturada': ''},
    {'criatura': 'esteno', 'derrotado_por': '', 'capturada': ''},
    {'criatura': 'medusa', 'derrotado_por': 'perseo', 'capturada': ''},
    {'criatura': 'ladon', 'derrotado_por': 'heracles', 'capturada': ''},
    {'criatura': 'aguila del caucaso', 'derrotado_por': '', 'capturada': 'hercules'},
    {'criatura': 'quimera', 'derrotado_por': 'belerofonte', 'capturada': ''},
    {'criatura': 'hidra de lerna', 'derrotado_por': 'heracles', 'capturada': ''},
    {'criatura': 'leon de nemea', 'derrotado_por': 'heracles', 'capturada': 'heracles'},
    {'criatura': 'esfinge', 'derrotado_por': 'edipo', 'capturada': ''},
    {'criatura': 'dragon de la colquida', 'derrotado_por': '', 'capturada': 'hercules'},
    {'criatura': 'cerbero', 'derrotado_por': '', 'capturada': ''},
    {'criatura': 'talos', 'derrotado_por': 'medea', 'capturada': ''},
    {'criatura': 'cerda de cromion', 'derrotado_por': 'teseo', 'capturada': ''},
    {'criatura': 'ortro', 'derrotado_por': 'heracles', 'capturada': ''},
    {'criatura': 'toro de creta', 'derrotado_por': 'teseo', 'capturada': ''},
    {'criatura': 'jabali de calidon', 'derrotado_por': 'atalanta', 'capturada': 'hercules'},
    {'criatura': 'carcinos', 'derrotado_por': '', 'capturada': ''},
    {'criatura': 'gerion', 'derrotado_por': 'heracles', 'capturada': ''},
    {'criatura': 'cloto', 'derrotado_por': '', 'capturada': ''},
    {'criatura': 'laquesis', 'derrotado_por': '', 'capturada': ''},
    {'criatura': 'atropos', 'derrotado_por': '', 'capturada': ''},
    {'criatura': 'minotauro de creta', 'derrotado_por': 'teseo', 'capturada': 'hercules'},
    {'criatura': 'harpias', 'derrotado_por': '', 'capturada': ''},
    {'criatura': 'argos panoptes', 'derrotado_por': 'hermes', 'capturada': ''},
    {'criatura': 'aves del estinfalo', 'derrotado_por': '', 'capturada': ''},
    {'criatura': 'sirenas', 'derrotado_por': '', 'capturada': ''},
    {'criatura': 'piton', 'derrotado_por': 'apolo', 'capturada': ''},
    {'criatura': 'cierva de cerinea', 'derrotado_por': '', 'capturada': ''},
    {'criatura': 'basilisco', 'derrotado_por': '', 'capturada': ''},
    {'criatura': 'jabali de erimanto', 'derrotado_por': '', 'capturada': ''},
]


for criatura in criaturas:
    insertar_nodo(arbol_criaturas,criatura['criatura'],criatura)

# A
inorden_datos(arbol_criaturas)
print()

# B 
x = input('desea agregar descripcion a alguna criatura? (si-no): ')
print()
while x == 'si': 
    buscado = input('ingrese la criatura que desea agregar descripcion: ')
    pos = busqueda(arbol_criaturas,buscado)

    if pos is not None:
        frase= input(f'descripcion que quiere agregarle a {buscado}: ')
        print()
        agregar_descripcion(arbol_criaturas,buscado,frase)
    else:
        print('la criatura no se encontro')
        print('')

    x = input('desea agregar otra descripcion a alguna criatura? (si-no): ')
    print()
    

# C 
x = busqueda(arbol_criaturas,'talos')
print('informacion de la criatura talos')
print(x['datos'])
print()

# D  determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;

# E
print('criaturas derrotadas por heracles')
derrotado_por_heracles(arbol_criaturas)
print()

# F
print('criaturas no derrotadas')
criaturas_no_derrotadas(arbol_criaturas)
print()

# G agregue el campo en el diccionario

# H
modificar_criaturas_capturadas(arbol_criaturas)

# I
clave = input('ingrese lo que quiera buscar: ')
print('resultado de lo que busco')
inorden_empieza_con(arbol_criaturas,clave)
print()

# J
eliminar_nodo(arbol_criaturas,'basilisco')
eliminar_nodo(arbol_criaturas,'las sirenas')

# K
pos = busqueda(arbol_criaturas, 'aves del estinfalo')
if pos is not None:
    pos['datos']['derrotado_por'] == 'varias'

# L
pos = busqueda(arbol_criaturas,'ladon') 

if pos is not None:            
    datos = pos['datos']
    eliminar_nodo(arbol_criaturas,'ladon')
    print('ladon fue modificado')
    datos['criatura'] = 'dragon ladon'
    insertar_nodo(arbol_criaturas,'dragon ladon',datos)
print()

# M
print('barrido por nivel')
por_nivel(arbol_criaturas)
print()

# N
print('criaturas capturadas por hercules')
criaturas_heracles(arbol_criaturas) 
print()

inorden_datos(arbol_criaturas)









