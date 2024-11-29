from comun import caracteres

""" 
    Función que se encarga de sanitizar la frase recibida.
    Quitamos los tildes
    Cambiamos . por *
    Convertimos las minúsculas a mayúsculas
    Omitimos caracteres que no se incluyen
"""
def santitizar_frase(frase):

    # En este punto lo que debemos controlar es que la información sea de tipo string
    if not(isinstance(frase, str)):
        raise Exception("El valor recibido deber ser una cadena de caracteres")
    
    # Para remplazar un tilde por un caracter valido
    reemplazos = { 'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U' }

    caracteres_sanitizados = []

    for i in frase:
        c = i.upper()
        
        if c in reemplazos:
            caracteres_sanitizados.append(reemplazos[c])
            continue

        if c == '.':
            caracteres_sanitizados.append("*")
            continue
        
        # La politica actualmente es si no esta y no es un punto, no lo incluimos en el cifrado
        if c not in caracteres:
            continue
        
        # Cuando llega acá es un caracter valido y lo agrega
        caracteres_sanitizados.append(c)
            
    # Arma una frase completa y la devuelve
    frase_sanitizada = "".join(caracteres_sanitizados)
    return frase_sanitizada



""" 
    Función que dada una frase, valida que sea de al menos 100 caracteres.
    Si lo es, pasa a encargarse de contar las repeticiones de cada caracter, devuelve 
    cual es el más presente, y si hay varios se queda con el primero que encuentra. 
    También devuelve las posiciones en las que lo encontró y la cantidad de 
    repeticiones. 
"""
def contar_apariciones(frase_larga):

    # Validamos que la variable sea un string
    if not(isinstance(frase_larga, str)):
        raise Exception("El valor recibido deber ser una cadena de caracteres")
    
    # Hacemos impresiones de los datos de interes
    contadores = {}
    posiciones = {}
    valor_maximo = 0
    caracter_maximo = ""

    # Iteramos sobre la frase de forma indexada
    for i in range(0, len(frase_larga)):
        valor_nuevo = -2

        # Convertimos a Mayus
        c = frase_larga[i].upper()
        
        if(c == " " or c == "*"):
            continue

        # Revisamos si ya guardamos su aparición
        if c in contadores:

            # Si ya fue así, obtenemos el 
            # valor anterior, le sumamos 1 y volvemos a guardarlo
            valor_nuevo = contadores[c] + 1
            contadores[c] = valor_nuevo

            # Agregamos la posición 
            posiciones[c].append(i)
        else:
            # No estaba considerado, guardamos la posición y el valor
            contadores[c] = 1
            posiciones[c] = [i]
        
        # Comparmos, si el nuevo es mayor que el máximo anterior, sustituimos
        # y nos guardamos al caracteres que lo cumple
        if valor_maximo < valor_nuevo:
            valor_maximo = valor_nuevo
            caracter_maximo = c

    # Pasamos a mostrar cada dato        
    print("Caracter con más apariciones", caracter_maximo)
    print("Cantidad de apariciones", valor_maximo)
    print("Posiciones de la cadena donde apareció", posiciones[caracter_maximo])