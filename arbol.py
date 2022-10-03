from cola import Cola


def nodoArbol():
    nodo = {
        'info': None,
        'datos': None,
        'der': None,
        'izq': None,
        'altura': 0,
    }
    return nodo


def copiar_nodo(nodo_datos, nodo_copia):
    if nodo_datos:
        nodo_copia['info'] = nodo_datos['info']
        nodo_copia['der'] = nodo_datos['der']
        nodo_copia['izq'] = nodo_datos['izq']
        if 'datos' in nodo_datos:
            nodo_copia['datos'] = nodo_datos['datos']


def insertar_nodo(arbol, dato, datos=None):
    if arbol['info'] is None:
        arbol['info'] = dato
        arbol['datos'] = datos
    elif dato < arbol['info']:
        if arbol['izq'] is None:
            arbol['izq'] = nodoArbol()
        insertar_nodo(arbol['izq'], dato, datos)
    else:
        if arbol['der'] is None:
            arbol['der'] = nodoArbol()
        insertar_nodo(arbol['der'], dato, datos)
    balancear(arbol)
    actualizar_altura(arbol)


def altura(arbol):
    if arbol is None:
        return -1
    else:
        return arbol['altura']


def actualizar_altura(arbol):
    if arbol is not None:
        alt_izq = altura(arbol['izq'])
        alt_der = altura(arbol['der'])
        arbol['altura'] = (alt_izq if alt_izq > alt_der else alt_der) + 1


def rotar_simple(arbol, control):
    aux = nodoArbol()
    if control:
        copiar_nodo(arbol['izq'], aux)
        arbol['izq'] = None
        if (aux['der'] and not arbol['izq']):
            arbol['izq'] = nodoArbol()
        copiar_nodo(aux['der'], arbol['izq'])
        aux['der'] = nodoArbol()
        copiar_nodo(arbol, aux['der'])
    else:
        copiar_nodo(arbol['der'], aux)
        arbol['der'] = None
        if (aux['izq'] and not arbol['der']):
            arbol['der'] = nodoArbol()
        copiar_nodo(aux['izq'], arbol['der'])
        aux['izq'] = nodoArbol()
        copiar_nodo(arbol, aux['izq'])
    arbol.update(aux)
    actualizar_altura(aux['izq'])
    actualizar_altura(aux['der'])
    actualizar_altura(aux)


def rotar_doble(arbol, control):
    if control:
        rotar_simple(arbol['izq'], False)
        rotar_simple(arbol, True)
    else:
        rotar_simple(arbol['der'], True)
        rotar_simple(arbol, False)


def balancear(arbol):
    if arbol is not None:
        if altura(arbol['izq']) - altura(arbol['der']) == 2:
            if (altura(arbol['izq']['izq']) >= altura(arbol['izq']['der'])):
                rotar_simple(arbol, True)
            else:
                rotar_doble(arbol, True)
        elif altura(arbol['der']) - altura(arbol['izq']) == 2:
            if (altura(arbol['der']['der']) >= altura(arbol['der']['izq'])):
                rotar_simple(arbol, False)
            else:
                rotar_doble(arbol, False)


def arbol_vacio(arbol):
    return arbol['info'] is None


def preorden(arbol):
    if (arbol is not None):
        print(arbol['info'], arbol['altura'],
              arbol['izq']['info'] if arbol['izq'] else None,
              arbol['der']['info'] if arbol['der'] else None)
        preorden(arbol['izq'])
        preorden(arbol['der'])


def contar_heroes(arbol):
    contador = 0
    if (arbol is not None):
        if arbol['villano'] == False:
            contador += 1
        contador += contar_heroes(arbol['izq'])
        contador += contar_heroes(arbol['der'])
    return contador


def inorden(arbol):
    if (arbol is not None):
        inorden(arbol['izq'])
        print(arbol['info'])
        inorden(arbol['der'])


def inorden_datos(arbol):
    if (arbol is not None):
        inorden_datos(arbol['izq'])
        print(arbol['info'], arbol['datos'])
        inorden_datos(arbol['der'])


def postorden(arbol):
    if (arbol is not None):
        postorden(arbol['der'])
        print(arbol['info'])
        postorden(arbol['izq'])


def busqueda(arbol, clave):
    aux = None
    if arbol is not None and arbol['info'] is not None:
        if arbol['info'] == clave:
            aux = arbol
        elif clave < arbol['info']:
            aux = busqueda(arbol['izq'], clave)
        else:
            aux = busqueda(arbol['der'], clave)
    return aux


def remplazar(arbol, anterior=None, primero=None):
    info, datos = None, None
    if arbol['der'] is None:
        info, datos = arbol['info'], arbol['datos']
        if anterior:
            anterior['der'] = arbol['izq']
        else:
            primero['izq'] = arbol['izq']
    else:
        info, datos = remplazar(arbol['der'], anterior=arbol)
    return info, datos


def eliminar_nodo(arbol, clave, previo=None, hijo=None):
    x, datos = None, None
    if arbol['info'] is not None:
        if arbol['izq'] and clave < arbol['info']:
            x, datos = eliminar_nodo(arbol['izq'], clave, arbol, 'izq')
        elif arbol['der'] and clave > arbol['info']:
            x, datos = eliminar_nodo(arbol['der'], clave, arbol, 'der')
        elif arbol['info'] == clave:
            x = arbol['info']
            datos = arbol['datos']
            if arbol['izq'] is None and arbol['der'] is not None:
                copiar_nodo(arbol['der'], arbol)
            elif arbol['der'] is None and arbol['izq'] is not None:
                copiar_nodo(arbol['izq'], arbol)
            elif arbol['izq'] is None and arbol['der'] is None:
                if previo is None:
                    arbol['info'] = None
                    arbol['datos'] = None
                else:
                    previo[hijo] = None
            else:
                info_aux, datos_aux = remplazar(arbol['izq'], primero=arbol)
                arbol['info'] = info_aux
                arbol['datos'] = datos_aux
        actualizar_altura(arbol)
        balancear(arbol)
    return x, datos


def por_nivel(arbol):
    pendientes = Cola()
    pendientes.arribo(arbol)
    while not pendientes.cola_vacia():
        nodo = pendientes.atencion()
        print(nodo['info'], nodo['izq']['info'] if nodo['izq'] else None, nodo['der']['info'] if nodo['der'] else None)
        if nodo['izq']:
            pendientes.arribo(nodo['izq'])
        if nodo['der']:
            pendientes.arribo(nodo['der'])


def cantidad_ocurrencias(arbol, numero):
    cont_ocurrencias = 0
    if (arbol is not None):
        if arbol['info'] == numero:
            cont_ocurrencias += 1
        cont_ocurrencias += cantidad_ocurrencias(arbol['izq'], numero)
        cont_ocurrencias += cantidad_ocurrencias(arbol['der'], numero)
    return cont_ocurrencias


def numeros_pares(arbol):
    pares = 0
    if (arbol is not None):
        if arbol['info'] % 2 == 0:
            pares += 1
        pares += numeros_pares(arbol['izq'])
        pares += numeros_pares(arbol['der'])
    return pares


def numeros_impares(arbol):
    impares = 0
    if (arbol is not None):
        if arbol['info'] % 2 == 0:
            impares += 1
        impares += numeros_impares(arbol['izq'])
        impares += numeros_impares(arbol['der'])
    return impares


def ranking_master(arbol):
    if (arbol is not None):
        ranking_master(arbol['izq'])
        if arbol['datos']['ranking'] == 'master':
            print(arbol['info'])
        ranking_master(arbol['der'])


def sable_verde(arbol):
    if (arbol is not None):
        sable_verde(arbol['izq'])
        if arbol['datos']['color_sable'] == 'verde':
            print(arbol['info'])
        sable_verde(arbol['der'])


def especie_togruta_cerean(arbol):
    if (arbol is not None):
        especie_togruta_cerean(arbol['izq'])
        if (arbol['datos']['maestro'] == 'cerean') or (arbol['datos']['maestro'] == 'togruta'):
            print(arbol['info'])
        especie_togruta_cerean(arbol['der'])


def inorden_contiene_valor(arbol, valor):
    if (arbol is not None):
        inorden_contiene_valor(arbol['izq'], valor)
        if '-' in arbol['info']:
            print(arbol['info'])
        inorden_contiene_valor(arbol['der'], valor)


# ------------------ FUNCIONES EJERCICIO 5 -------------------------------------
def inorden_villano(arbol):
    if (arbol is not None):
        inorden_villano(arbol['izq'])
        if arbol['datos']['villano'] == True:
            print(arbol['info'])
        inorden_villano(arbol['der'])


def inorden_heroes(arbol):
    if (arbol is not None):
        inorden_heroes(arbol['izq'])
        if arbol['datos']['villano'] == False:
            print(arbol['info'])
        inorden_heroes(arbol['der'])


def inorden_empieza_con(arbol, valor):
    if (arbol is not None):
        inorden_empieza_con(arbol['izq'], valor)
        if arbol['info'].startswith(valor):
            print(arbol['info'])
        inorden_empieza_con(arbol['der'], valor)


def postorden_heroes(arbol):
    if (arbol is not None):
        postorden_heroes(arbol['der'])
        if arbol['datos']['villano'] == False:
            print(arbol['info'])
        postorden_heroes(arbol['izq'])


def crear_bosque(arbol, bosque1, bosque2):
    if (arbol is not None):
        crear_bosque(arbol['izq'], bosque1, bosque2)
        if arbol['datos']['villano'] == True:
            insertar_nodo(bosque1, arbol['info'])
        else:
            insertar_nodo(bosque2, arbol['info'])
        crear_bosque(arbol['der'], bosque1, bosque2)

# ------------------------------------------------------------------------------

# ------------------ FUNCIONES EJERCICIO 23 -------------------------------------
def derrotado_por_heracles(arbol):
    if (arbol is not None):
        derrotado_por_heracles(arbol['izq'])
        if arbol['datos']['derrotado_por'] == 'heracles':
            print(arbol['info'])
        derrotado_por_heracles(arbol['der'])


def criaturas_no_derrotadas(arbol):
    if (arbol is not None):
        criaturas_no_derrotadas(arbol['izq'])
        if arbol['datos']['derrotado_por'] == '':
            print(arbol['info'])
        criaturas_no_derrotadas(arbol['der'])


def modificar_criaturas_capturadas(arbol):
    if (arbol is not None):
        modificar_criaturas_capturadas(arbol['izq'])
        if arbol['info'] == 'cerbero':
            arbol['datos']['capturada'] == 'heracles'

        if arbol['info'] == 'toro de creta':
            arbol['datos']['capturada'] == 'heracles'

        if arbol['info'] == 'cierva cerinea':
            arbol['datos']['capturada'] == 'heracles'

        if arbol['info'] == 'jabali de erimanto':
            arbol['datos']['capturada'] == 'heracles'
            
        modificar_criaturas_capturadas(arbol['der'])


def criaturas_heracles(arbol):
    if (arbol is not None):
        criaturas_heracles(arbol['izq'])
        if arbol['datos']['capturada'] == 'heracles':
            print(arbol['info'])
        criaturas_heracles(arbol['der'])


def agregar_descripcion(arbol,clave,clave2):
    if (arbol is not None):
        agregar_descripcion(arbol['izq'], clave, clave2)
        if arbol['info'] == clave:
            if not 'descripcion' in arbol['datos']:
                arbol['datos']['descripcion'] = clave2
        agregar_descripcion(arbol['der'], clave, clave2)
        
# ----------------------------------------------------------------------------------

