from common import characters


""" 
    Función que se encarga de sanitizar la frase recibida.
    Quitamos los tildes
    Cambiamos . por *
    Convertimos las minúsculas a mayúsculas
    Omitimos caracteres que no se incluyen
"""
def sanctify_phrase(phrase):

    # En este punto lo que debemos controlar es que la información sea de tipo string
    if not(isinstance(phrase, str)):
        raise Exception("El valor recibido deber ser una cadena de caracteres")

    # Para remplazar un tilde por un caracter valido
    replacements = { 'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U' }
    sanitized_characters = []

    for i in phrase:
        c = i.upper()
        if c in replacements:
            sanitized_characters.append(replacements[c])
            continue
        
        # La politica actualmente es si no esta y no es un punto, no lo incluimos en el cifrado
        if c not in characters:
            continue

        # Cuando llega acá es un caracter valido y lo agrega
        sanitized_characters.append(c)

    # Arma una frase completa y la devuelve
    return "".join(sanitized_characters)


""" 
    Función que dada una frase, valida que sea de al menos 100 caracteres.
    Si lo es, pasa a encargarse de contar las repeticiones de cada caracter, devuelve 
    cual es el más presente, y si hay varios se queda con el primero que encuentra. 
    También devuelve las posiciones en las que lo encontró y la cantidad de 
    repeticiones. 
"""
def count_appearances(long_phrase, is_a_encripted_phrase = False):


    # Validamos que la variable sea un string
    if not(isinstance(long_phrase, str)):
        raise Exception("El valor recibido deber ser una cadena de caracteres")
    

    # Declaramos las variables que usaremos más adelante
    counters = {}
    positions = {}
    max_value = 0
    max_character = ""


    # Iteramos sobre la frase de forma indexada
    for i in range(0, len(long_phrase)):
        new_value = -2

        # Convertimos a Mayus
        c = long_phrase[i].upper()

        # Revisamos si ya guardamos su aparición
        if c in counters:

            # Si ya fue así, obtenemos el 
            # valor anterior, le sumamos 1 y volvemos a guardarlo
            new_value = counters[c] + 1

            counters[c] = new_value

            # Agregamos la posición 
            positions[c].append(i)

        else:
            # No estaba considerado, guardamos la posición y el valor
            counters[c] = 1
            positions[c] = [i]
        

        # Comparmos, si el nuevo es mayor que el máximo anterior, sustituimos
        # y nos guardamos al caracteres que lo cumple
        if max_value < new_value:
            max_value = new_value
            max_character = c

    # Pasamos a mostrar cada dato        
    print("Caracter con más apariciones", max_character)
    print("Cantidad de apariciones", max_value)
    print("Posiciones de la cadena donde apareció", positions[max_character])
    
