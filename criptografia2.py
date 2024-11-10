from comun import a,b, traducir_caracter, traducir_numero
import numpy as np

matriz_asociada = [[1, 2, 1], [0, 1, -1], [0, 0, 1]]
A = np.array(matriz_asociada)

b = np.array([[1], [2], [3]])


# Calcular la matriz inversa
A_inv = np.linalg.inv(A)

def transformacion_lineal(vector):
    # Control de tamaños

    # T(x) = (x + 2y + z, y-2, z)
    x = vector[0][0]
    y = vector[1][0]
    z = vector[2][0]

    vector_transformado = [[x + 2 * y + z], [y -z],[z]]

    return vector_transformado



def encriptar_terna(terna):

    if not(isinstance(terna, str)) or len(terna) != 3:
        raise Exception("Información invalida")


    x11 = traducir_caracter(terna[0])
    x21 = traducir_caracter(terna[1])
    x31 = traducir_caracter(terna[2])

    transform_lineal = np.array(transformacion_lineal([[x11], [x21], [x31]]))


    resultado_final = (transform_lineal + b) % 29


    # Ahora cada número vamos a obtener su correlación en la tabla
    x = int(resultado_final[0][0])
    y = int(resultado_final[1][0])
    z = int(resultado_final[2][0])


    x = traducir_numero(x)
    y = traducir_numero(y)
    z = traducir_numero(z)


    a_caracteres = [[x], [y], [z]]

    return a_caracteres

    


def encriptar_frase_as_vector(frase):

    if not(isinstance(frase, str)) or len(frase) < 100:
        raise Exception("Entrada invalida")

    
    tamaño = len(frase)
    add = ""
    if(tamaño % 3 == 1):
        add = "  " 
    elif (tamaño % 3 == 2):
        add = " "
    
    frase +=add

    ternas = []
    ternas_encriptadas = []
    for i in range(0, tamaño, 3):

        terna = frase[i:i+3]
        ternas.append(terna)

        # Ya hacemos la encriptación
        terna_encriptada = encriptar_terna(terna)
        ternas_encriptadas.append(terna_encriptada)

    
    return rearmar_frase(ternas_encriptadas)


def rearmar_frase(ternas):

    # Falta comprobar dimensiones
    if ternas == None or len(ternas) == 0:
        raise Exception("Entrada invalida")

    caracteres = []
    for t in ternas:
        caracteres.append(t[0][0])
        caracteres.append(t[1][0])
        caracteres.append(t[2][0])
    
    frase = "".join(caracteres)
    return frase


def desencriptar_terna(terna_encriptada):
    # Control de tamaños

    x = terna_encriptada[0][0]
    y = terna_encriptada[1][0]
    z = terna_encriptada[2][0]

    x = traducir_caracter(x)
    y = traducir_caracter(y)
    z = traducir_caracter(z)

    terna_numerica = np.array([[x], [y], [z]])

    

    # T(x)-1 = A * (T(x) - b 

    tmp = terna_numerica - b
    por_asociada = np.dot(A_inv, tmp)
    terna_desencriptada = por_asociada % 29

    
    x = int(terna_desencriptada[0][0])
    y = int(terna_desencriptada[1][0])
    z = int(terna_desencriptada[2][0])

    x = traducir_numero(x)
    y = traducir_numero(y)
    z = traducir_numero(z)

    vector_desencriptado = [[x], [y], [z]]

    return vector_desencriptado

def desencriptar_frase_as_vector(frase_encriptada):

    if not(isinstance(frase_encriptada, str)) or len(frase_encriptada) < 100:
        raise Exception("Entrada invalida")

    # Primero vemos si es divisible entre 3, si lo es, cortamos cada 3 sin problema
    tamaño = len(frase_encriptada)
    ternas = []
    for i in range(0, tamaño, 3):

        terna = frase_encriptada[i:i+3]
        terna_desencriptada = desencriptar_terna(terna)
        ternas.append(terna_desencriptada)

    return rearmar_frase(ternas)
