from analizarFrase import santitizar_frase, contar_apariciones
from criptografia1 import encriptar_frase, desencriptar_frase
from criptografia2 import encriptar_frase_as_vector, desencriptar_frase_as_vector



def main():
        
    frase_larga = "El análisis detallado de los datos permitió descubrir patrones inesperados que no habían sido contemplados previamente."
    frase_s = santitizar_frase(frase_larga)
    frase_encript = encriptar_frase(frase_s)
    frase_descrip = desencriptar_frase(frase_encript)

    print("Frase original:", frase_larga )
    print("Frase Sanitizada:",  frase_s)

    # Vamos a ver cual fue el caracter que más aparecio en la original y sus posciones
    print("\nVeamos cual fue el caracter más repetido en la frase original")
    contar_apariciones(frase_s)

    print("\nVeamos cual fue el caracter más repetido en la frase encriptada")
    contar_apariciones(frase_encript)

    print("Frase Encriptada:", frase_encript )
    print("Frase Desnecriptada:", frase_descrip)


    # Ahora vamos con el cripto sistema 2
    print("\nVamos ahora a trabajar con el criptosistema2")
    frase_encriptada2 =  encriptar_frase_as_vector(frase_s)
    print("\nFrase encriptada con el criptosistema2:", frase_encriptada2)
    
    print("\nVeamos cual fue el caracter más repetido en la segunda frase encriptada")
    contar_apariciones(frase_encriptada2)

    frase_descrip2 = desencriptar_frase_as_vector(frase_encriptada2)
    print("\nFrase desencriptada luego de encriptarla con el criptosistema2", frase_descrip2)
    contar_apariciones(frase_descrip2)



if __name__ == "__main__":
    main()



