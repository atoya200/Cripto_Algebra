caracteres = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9,
    "K": 10, "L": 11, "M": 12, "N": 13, "Ñ": 14,
    "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23,
    "X": 24, "Y": 25, "Z": 26, " ": 27, "*": 28
}


def contar_repeticiones_frase(frase):

    if not(isinstance(frase, str)):
        raise Exception("El valor recibido deber ser una cadena de caracteres")
    
    contadores = {}
    posiciones = {}
    valor_maximo = 0
    caracter_maximo = ""

    for i in range(0, len(frase)):
        valor_nuevo = -2
        c = frase[i].upper()
        if c in contadores:
            valor_nuevo = contadores[c] + 1
            contadores[c] = valor_nuevo
            posiciones[c].append(i)
        else:
            contadores[c] = 1
            posiciones[c] = [i]
        
        if valor_maximo < valor_nuevo:
            valor_maximo = valor_nuevo
            caracter_maximo = c
    

    """ print("Caracter maximo", caracter_maximo)
    print("Valor Maximo", valor_maximo)
    print("Contadores", contadores)
    print("Posiciones", posiciones) """
    #return {"contadores": contadores, "posiciones": posiciones, "maximo": valor_maximo, "caracter_maximo": caracter_maximo }
    return {"posiciones": posiciones[caracter_maximo], "maximo": valor_maximo, "caracter_maximo": caracter_maximo }





def santitizar_frase(frase):

    if not(isinstance(frase, str)):
        raise Exception("El valor recibido deber ser una cadena de caracteres")
    
    reemplazos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'
    }

    caracteres_sanitizados = []
    frase_sanitizada = ""

    for i in frase:
        c = i.upper()
        
        if c in reemplazos:
            caracteres_sanitizados.append(reemplazos[c])
            continue

        if c == '.':
            caracteres_sanitizados.append("*")
            continue
        
        """ if c == ",":
            caracteres_sanitizados.append(" ")
            continue """
        
        if c not in caracteres:
            # La politica actualmente es si no esta y no es un punto, no lo incluimos en el cifrado
            continue

        caracteres_sanitizados.append(c)
            
    frase_sanitizada = "".join(caracteres_sanitizados)
    return frase_sanitizada



#frase_larga = "Los desafíos nos enseñan que cada paso cuenta. Con esfuerzo y perseverancia, alcanzaremos nuestras metas. eeeehh"

def contar_apariciones(frase_larga):
    if not(isinstance(frase_larga, str)):
        raise Exception("El valor recibido deber ser una cadena de caracteres")
    
    datos = contar_repeticiones_frase(frase_larga)


    print("Caracter con más apariciones", datos['caracter_maximo'])
    print("Cantidad de apariciones", datos['maximo'])
    print("Posiciones de la cadena donde apareció", datos['posiciones'])