from common import a, b, translate_character, translate_number
import math

def encrypt_character(character):

    # Validamos que la entrada sea un caracter
    if not(isinstance(character, str)):
        raise Exception("Dato invalido, debe ser un caracter")
 

    x = translate_character(character)

    # Validamos que la letra tenga un valor correspondiente
    if not(isinstance(x, int)) or not(x >= 0 and x  < 29) : 
        raise Exception("Dato invalido, debe ser un número entre 0 y 28")

    # Convertimos el valor para obtener la correspondencia original del caracter
    index = (a*x + b) % 29 

    # Devolvemos el valor correspondiente
    return translate_number(index)



def encrypt_phrase(phrase):
    if not(isinstance(phrase, str)) or len(phrase) < 100:
        raise Exception("El largo de la frase debe ser mayor o igual a 100 caracteres")
    
    characters_encrypted_phrase = []
    for c in phrase:
        encrypted_character = encrypt_character(c)
        characters_encrypted_phrase.append(encrypted_character)
    
    # Devolvemos la frase encriptada
    return  "".join(characters_encrypted_phrase)


def desencrypt_character(character):

    if(not(isinstance(character, str))):
        raise Exception("El dato recibido debe ser una cadena de caracteres")
    
    # Nos da la letra correspondiente al número
    y = translate_character(character)

    # Hace un redondeo hacia abajo
    a_roof = math.ceil(29 / a)

    x = (a_roof * (y - b) ) % 29
    c = translate_number(x)
    return c

def desencrypt_phrase(phrase):

    if(not(isinstance(phrase, str))):
        raise Exception("El dato recibido debe ser una cadena de caracteres")

    # Lista para guardar los caracteres desencriptados
    decrypted_characters = []

    for c in phrase:
        decrypted_character = desencrypt_character(c)
        decrypted_characters.append(decrypted_character)

    # Unimos los caracteres y armamos la frase desencriptada
    return "".join(decrypted_characters)


