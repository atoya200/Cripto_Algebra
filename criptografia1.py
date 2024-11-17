from comun import a, b, traducir_caracter, traducir_numero
import math

def encriptar_caracter(caracter):

    # Validamos que la entrada sea un caracter
    if not(isinstance(caracter, str)):
        raise Exception("Dato invalido, debe ser un caracter")
 

    x = traducir_caracter(caracter)

    # Validamos que la letra tenga un valor correspondiente
    if not(isinstance(x, int)) or not(x >= 0 and x  < 29) : 
        raise Exception("Dato invalido, debe ser un número entre 0 y 28")

    
    indice = (a*x + b) % 29 

    return traducir_numero(indice)



def encriptar_frase(frase):
    if not(isinstance(frase, str)) or len(frase) < 100:
        raise Exception("El largo de la frase debe ser mayor o igual a 100 caracteres")
    
    caracteres_frase_encriptada = []
    for c in frase:
        encriptado = encriptar_caracter(c)
        caracteres_frase_encriptada.append(encriptado)
    
    frase_encriptada = "".join(caracteres_frase_encriptada)
    return frase_encriptada


def desencriptar_caracter(caracter):

    if(not(isinstance(caracter, str))):
        raise Exception("El dato recibido debe ser una cadena de caracteres")
    
    # Nos da la letra correspondiente al número
    y = traducir_caracter(caracter)

    # Hace un redondeo hacia abajo
    a_techo = math.ceil(29 / a)

    x = (a_techo * (y - b) ) % 29
    c = traducir_numero(x)
    return c

def desencriptar_frase(frase):

    if(not(isinstance(frase, str))):
        raise Exception("El dato recibido debe ser una cadena de caracteres")

    # Lista para guardar los caracteres desencriptados
    caracteres_descifrados = []

    for c in frase:
        c_descr = desencriptar_caracter(c)
        caracteres_descifrados.append(c_descr)

    # Unimos los caracteres y armamos la frase
    return "".join(caracteres_descifrados)


