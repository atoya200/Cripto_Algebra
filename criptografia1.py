from comun import a, b, traducir_caracter, traducir_numero
import math

def encriptar_caracter(caracter):

    x = traducir_caracter(caracter)

    if not(isinstance(x, int)) or not(x >= 0 and x  < 29) : 
        raise Exception("Dato recibido invalido, debe ser un número entre 0 y 28")

    
    indice = (a*x + b) % 29 

    return traducir_numero(indice)



def encriptar_frase(frase):
    if len(frase) < 100:
        raise Exception("El largo de la frase debe ser mayor o igual a 100 caracteres")
    
    caracteres_frase_encriptada = []
    for c in frase:
        encriptado = encriptar_caracter(c)
        caracteres_frase_encriptada.append(encriptado)
    
    frase_encriptada = "".join(caracteres_frase_encriptada)
    return frase_encriptada


def desencriptar_frase(frase):

    caracteres_descifrados = []

    for c in frase:
        c_descr = desencriptar_caracter(c)
        caracteres_descifrados.append(c_descr)

    return "".join(caracteres_descifrados)

def desencriptar_caracter(caracter):

    y = traducir_caracter(caracter)

    a_techo = math.ceil(29 / a)


    x = (a_techo * (y - b) ) % 29
    c = traducir_numero(x)
    return c

