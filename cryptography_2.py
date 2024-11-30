from common import a,b, translate_character, translate_number
import numpy as np

# Transformación Lineal elegida
# T(x) = (x + 2y + z, y-2, z)
# Matriz Asociada a la transformación elegida
A = np.array([[1, 2, 1], [0, 1, -1], [0, 0, 1]])

# Matriz columna auxiliar
b = np.array([[1], [2], [3]])


# Calcular la matriz inversa
A_reverse = np.linalg.inv(A)

""" 
    Función que nos sirve para realizar la transformación lineal elegida
"""
def linear_transformation(vector):
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
    transformed_vector = np.array([[x + 2 * y + z], [y -z],[z]])

    return transformed_vector


""" 
    Toma tres caracteres, genera la terna y la encripta basandose en la función
    elegida para este criptsistema
"""
def encrypt_terna(terna):

    # Revisamos que venga una terna de 3 caracteres
    if not(isinstance(terna, str)) or len(terna) != 3:
        raise Exception("Información invalida")

    # Tomamos los caracteres para x11 o x, x21 o y, y para x31 o z
    x11 = translate_character(terna[0])
    x21 = translate_character(terna[1])
    x31 = translate_character(terna[2])

    # Les aplicamos la transformación lineal
    linear_transform = linear_transformation(np.array([[x11], [x21], [x31]]))

    # Le sumamos el vector columna b
    final_result = (linear_transform + b) % 29


    # Ahora cada número vamos a obtener su correlación en la tabla
    x = int(final_result[0][0])
    y = int(final_result[1][0])
    z = int(final_result[2][0])

    # Traducimos de número a letra
    x = translate_number(x)
    y = translate_number(y)
    z = translate_number(z)

    # Armamos una  nueva matriz de 1x3 como la terna encriptada
    encrypted_terna = np.array([[x], [y], [z]])

    return encrypted_terna

    

""" 
    Convierte una frase de 100 caracteres o más en 
    una frase encriptada aplicando el criptosistema 2
"""
def encrypt_phrase_as_vector(phrase):

    # Si la entrada no es un cadena de caracteres  o si es menor a 100 caracteres
    if not(isinstance(phrase, str)) or len(phrase) < 100:
        raise Exception("Entrada invalida")

    # Ya nos preparamos de antemano y si el tamaño de la cadena no es 
    # multiplo de 3 significa que hay que adicionar espacios en blanco
    # Si da módulo 1, faltan dos espacios
    # Si da módulo 2, falta un espacio
    phrase_size = len(phrase)
    add = ""
    if(phrase_size % 3 == 1):
        add = "  " 
    elif (phrase_size % 3 == 2):
        add = " "
    
    # Agregamos los espacios o nada si es múltiplo
    phrase +=add

    encrypted_ternas = []

    # Pasamos a recorrer la frase, separando de a 3 caracteres
    for i in range(0, phrase_size, 3):

        # Tomamos la terna
        terna = phrase[i:i+3]

        # Hacemos la encriptación
        encrypted_terna = encrypt_terna(terna)

        # Guardamos el valor encriptado
        encrypted_ternas.append(encrypted_terna)

    # En vez de devolver las ternas, ya devolvemos la frase encriptada
    return rearm_phrase(encrypted_ternas)


""" 
    Toma una lista de ternas y va rearmando una frase legible por humanos, encriptada o no, 
    esto dependerá de quien la invoque
"""
def rearm_phrase(ternas):

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
         
    
    characters = []
    for t in ternas:
        characters.append(t[0][0])
        characters.append(t[1][0])
        characters.append(t[2][0])
    
    return "".join(characters)


""" 
    Aplica una función de desencriptación para una terna en particular, que llega 
    como un conjunto de tres caracteres, encontrando el valor original
"""
def decrypt_terna(encrypted_terna):

    # Comprobamos que no venga nulo o None y que tenga las dimensiones adecuadas
    if encrypted_terna == None or len(encrypted_terna) != 3:
        raise Exception("Entrada invalida")

    # Obtenemos cada valor encriptado correspondiente
    x = encrypted_terna[0]
    y = encrypted_terna[1]
    z = encrypted_terna[2]

    # Pasamos de letras a números
    x = translate_character(x)
    y = translate_character(y)
    z = translate_character(z)

    # Armamos la tenra númerica
    triple_numeric = np.array([[x], [y], [z]])

    
    # La función para desencriptar
    # (A^-1 * (x - b)) % 29
    tmp = triple_numeric - b
    tmp_result = np.dot(A_reverse, tmp)
    terna_decrypted = tmp_result % 29

    # Ahora tomamos cada valor
    x = int(terna_decrypted[0][0])
    y = int(terna_decrypted[1][0])
    z = int(terna_decrypted[2][0])

    # Ahora lo convertimos en texto
    x = translate_number(x)
    y = translate_number(y)
    z = translate_number(z)

    terna_decrypted_letters = np.array([[x], [y], [z]])

    return terna_decrypted_letters

""" 
    Esta función toma una frase de al menos 100 caracteres y que debe 
    tener un tamaño que sea multiplo de 3, dado que viene encriptada con el sistema 
    anterior. Luego desencripta de a tres caractres, y luego devuelve la frase original
"""
def desencrypt_phrase_as_vector(encrypted_phrase):

    if not(isinstance(encrypted_phrase, str)) or len(encrypted_phrase) < 100:
        raise Exception("Entrada invalida")

    # Primero vemos si es divisible entre 3, si lo es, cortamos cada 3 sin problema
    if len(encrypted_phrase) % 3 != 0:
        raise Exception("Esta frase no esta encriptada por este algoritmo")
    
    encrypted_phrase_size = len(encrypted_phrase)
    ternas = []
    for i in range(0, encrypted_phrase_size, 3):

        # Tomamos una terna de caracteres
        terna = encrypted_phrase[i:i+3]

        # Desencriptamos los caractres
        terna_decrypted = decrypt_terna(terna)

        # Vamos guardando lo que desencriptamos
        ternas.append(terna_decrypted)

    return rearm_phrase(ternas)
