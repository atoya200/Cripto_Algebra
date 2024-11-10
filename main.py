from analizarFrase import santitizar_frase, contar_apariciones
from criptografia1 import encriptar_frase, desencriptar_frase
from criptografia2 import encriptar_frase_as_vector, desencriptar_frase_as_vector

a = 3
b = 21


caracteres = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9,
    "K": 10, "L": 11, "M": 12, "N": 13, "Ñ": 14,
    "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23,
    "X": 24, "Y": 25, "Z": 26, " ": 27, "*": 28
}

numeros = {
    0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J",
    10: "K", 11: "L", 12: "M", 13: "N", 14: "Ñ",
    15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U", 22: "V", 23: "W",
    24: "X", 25: "Y", 26: "Z", 27: " ", 28: "*"
}



def traducir_caracter(caracter):
    if isinstance(caracter, str): 
        return caracteres[caracter.upper()]

    raise Exception("El valor recibido debe ser un caracter")

def main():
        
    frase_larga = "Los desafíos nos enseñan que cjkjhjhjkkjkada paso cuenta.Cooperseverancia,alcanzaremos nuestras metas."
    frase_s = santitizar_frase(frase_larga)
    frase_encript = encriptar_frase(frase_s)
    frase_descrip = desencriptar_frase(frase_encript)

    print("Frase original:", frase_larga )
    print("Frase Sanitizada:",  frase_s)

    # Vamos a ver cual fue el caracter que más aparecio en la original y sus posciones
    print("\nVeamos cual fue el caracter más repetido en la frase original")
    #print(contar_repeticiones_frase(frase_s))
    contar_apariciones(frase_s)

    print("\nVeamos cual fue el caracter más repetido en la frase encriptada")
    #print(contar_repeticiones_frase(frase_encript))
    contar_apariciones(frase_encript)

    print("Frase Encriptada:", frase_encript )
    print("Frase Desnecriptada:", frase_descrip)


    # Ahora vamos con el cripto sistema 2
    print("\nVamos ahora a trabajar con el criptosistema2")
    frase_encriptada2 =  encriptar_frase_as_vector(frase_s)
    print("\nFrase encriptada con el criptosistema2:", frase_encriptada2)
    
    print("\nVeamos cual fue el caracter más repetido en la segunda frase encriptada")
    #print(contar_repeticiones_frase(frase_encriptada2))
    contar_apariciones(frase_encriptada2)

    frase_descrip2 = desencriptar_frase_as_vector(frase_encriptada2)
    print("\nFrase desencriptada luego de encriptarla con el criptosistema2", frase_descrip2)
    contar_apariciones(frase_descrip2)



if __name__ == "__main__":
    main()



