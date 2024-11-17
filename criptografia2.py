from comun import a,b, traducir_caracter, traducir_numero
import numpy as np

# Transformación Lineal elegida
# T(x) = (x + 2y + z, y-2, z)
# Matriz Asociada a la transformación elegida
A = np.array([[1, 2, 1], [0, 1, -1], [0, 0, 1]])

# Matriz columna auxiliar
b = np.array([[1], [2], [3]])


# Calcular la matriz inversa
A_inv = np.linalg.inv(A)

""" 
    Función que nos sirve para realizar la transformación lineal elegida
"""
def transformacion_lineal(vector):
    # Control de tamaños
    if vector is None or not isinstance(vector, np.ndarray):
        raise Exception("Debe ser un vector")

    if vector.shape != (3, 1):
        raise Exception("Debe ser un vector columna de tres elementos")
         

    # Separamos nuestros x, y, z
    x = vector[0][0]
    y = vector[1][0]
    z = vector[2][0]

    # Le aplicamos la transformación lineal 
    # T(x) = (x + 2y + z, y-2, z)
    # y guardamos su resultado
    vector_transformado = np.array([[x + 2 * y + z], [y -z],[z]])

    return vector_transformado


""" 
    Toma tres caracteres, genera la terna y la encripta basandose en la función
    elegida para este criptsistema
"""
def encriptar_terna(terna):

    # Revisamos que venga una terna de 3 caracteres
    if not(isinstance(terna, str)) or len(terna) != 3:
        raise Exception("Información invalida")

    # Tomamos los caracteres para x11 o x, x21 o y, y para x31 o z
    x11 = traducir_caracter(terna[0])
    x21 = traducir_caracter(terna[1])
    x31 = traducir_caracter(terna[2])

    # Les aplicamos la transformación lineal
    transform_lineal = transformacion_lineal(np.array([[x11], [x21], [x31]]))

    # Le sumamos el vector columna b
    resultado_final = (transform_lineal + b) % 29


    # Ahora cada número vamos a obtener su correlación en la tabla
    x = int(resultado_final[0][0])
    y = int(resultado_final[1][0])
    z = int(resultado_final[2][0])

    # Traducimos de número a letra
    x = traducir_numero(x)
    y = traducir_numero(y)
    z = traducir_numero(z)

    # Armamos una  nueva matriz de 1x3 como la terna encriptada
    terna_encriptada = np.array([[x], [y], [z]])

    return terna_encriptada

    

""" 
    Convierte una frase de 100 caracteres o más en 
    una frase encriptada aplicando el criptosistema 2
"""
def encriptar_frase_as_vector(frase):

    # Si la entrada no es un cadena de caracteres  o si es menor a 100 caracteres
    if not(isinstance(frase, str)) or len(frase) < 100:
        raise Exception("Entrada invalida")

    # Ya nos preparamos de antemano y si el tamaño de la cadena no es 
    # multiplo de 3 significa que hay que adicionar espacios en blanco
    # Si da módulo 1, faltan dos espacios
    # Si da módulo 2, falta un espacio
    tamaño = len(frase)
    add = ""
    if(tamaño % 3 == 1):
        add = "  " 
    elif (tamaño % 3 == 2):
        add = " "
    
    # Agregamos los espacios o nada si es múltiplo
    frase +=add

    ternas_encriptadas = []

    # Pasamos a recorrer la frase, separando de a 3 caracteres
    for i in range(0, tamaño, 3):

        # Tomamos la terna
        terna = frase[i:i+3]

        # Hacemos la encriptación
        terna_encriptada = encriptar_terna(terna)

        # Guardamos el valor encriptado
        ternas_encriptadas.append(terna_encriptada)

    # En vez de devolver las ternas, ya devolvemos la frase encriptada
    return rearmar_frase(ternas_encriptadas)


""" 
    Toma una lista de ternas y va rearmando una frase legible por humanos, encriptada o no, 
    esto dependerá de quien la invoque
"""
def rearmar_frase(ternas):

    """ print(ternas)
    # Comprobamos que no venga nulo o None y que tenga las dimensiones adecuadas
    if ternas is None or not isinstance(ternas, np.ndarray) :
        raise Exception("Debe ser un vector")

    if ternas.shape != (3, 1):
        raise Exception("Debe ser un vector columna de tres elementos") """

    if not isinstance(ternas, list):
        raise ValueError("El objeto debe ser una lista.")
    
    for i, arr in enumerate(ternas):
        if not isinstance(arr, np.ndarray):
            raise ValueError(f"El elemento {i} no es un array de NumPy.")
        
        # Validar que el array tenga 3 filas y 1 columna
        if arr.shape != (3, 1):
            raise ValueError(f"El array en la posición {i} no tiene 3 filas y 1 columna. Forma encontrada: {arr.shape}")
         
    
    caracteres = []
    for t in ternas:
        caracteres.append(t[0][0])
        caracteres.append(t[1][0])
        caracteres.append(t[2][0])
    
    frase = "".join(caracteres)
    return frase


""" 
    Aplica una función de desencriptación para una terna en particular, que llega 
    como un conjunto de tres caracteres, encontrando el valor original
"""
def desencriptar_terna(terna_encriptada):

    # Comprobamos que no venga nulo o None y que tenga las dimensiones adecuadas
    #if terna_encriptada == None or not(terna_encriptada.shape[0] == 3 and terna_encriptada.shape[1] == 1):
    if terna_encriptada == None or len(terna_encriptada) != 3:
        raise Exception("Entrada invalida")

    # Obtenemos cada valor encriptado correspondiente
    x = terna_encriptada[0]
    y = terna_encriptada[1]
    z = terna_encriptada[2]

    # Pasamos de letras a números
    x = traducir_caracter(x)
    y = traducir_caracter(y)
    z = traducir_caracter(z)

    # Armamos la tenra númerica
    terna_numerica = np.array([[x], [y], [z]])

    
    # La función para desencriptar
    # (A^-1 * (x - b)) % 29
    tmp = terna_numerica - b
    por_asociada = np.dot(A_inv, tmp)
    terna_desencriptada = por_asociada % 29

    # Ahora tomamos cada valor
    x = int(terna_desencriptada[0][0])
    y = int(terna_desencriptada[1][0])
    z = int(terna_desencriptada[2][0])

    # Ahora lo convertimos en texto
    x = traducir_numero(x)
    y = traducir_numero(y)
    z = traducir_numero(z)

    terna_desencriptada_letras = np.array([[x], [y], [z]])

    return terna_desencriptada_letras

""" 
    Esta función toma una frase de al menos 100 caracteres y que debe 
    tener un tamaño que sea multiplo de 3, dado que viene encriptada con el sistema 
    anterior. Luego desencripta de a tres caractres, y luego devuelve la frase original
"""
def desencriptar_frase_as_vector(frase_encriptada):

    if not(isinstance(frase_encriptada, str)) or len(frase_encriptada) < 100:
        raise Exception("Entrada invalida")

    # Primero vemos si es divisible entre 3, si lo es, cortamos cada 3 sin problema
    if len(frase_encriptada) % 3 != 0:
        raise Exception("Esta frase no esta encriptada por este algoritmo")
    
    tamaño = len(frase_encriptada)
    ternas = []
    for i in range(0, tamaño, 3):

        # Tomamos una terna de caracteres
        terna = frase_encriptada[i:i+3]

        # Desencriptamos los caractres
        terna_desencriptada = desencriptar_terna(terna)

        # Vamos guardando lo que desencriptamos
        ternas.append(terna_desencriptada)

    return rearmar_frase(ternas)
