from analizarFrase import sanctify_phrase, count_appearances
from criptografia1 import encrypt_phrase, desencrypt_phrase
from criptografia2 import encrypt_phrase_as_vector, desencrypt_phrase_as_vector



def main():
        
    long_phrase = "El análisis detallado de los datos permitió descubrir patrones inesperados que no habían sido contemplados previamente."
    sanitized_phrase = sanctify_phrase(long_phrase)
    encrypted_phrase = encrypt_phrase(sanitized_phrase)
    decrypted_phrase = desencrypt_phrase(encrypted_phrase)

    print("Frase original:", long_phrase )
    print("Frase Sanitizada:",  sanitized_phrase)

    # Vamos a ver cual fue el caracter que más aparecio en la original y sus posciones
    print("\nVeamos cual fue el caracter más repetido en la frase original")
    count_appearances(sanitized_phrase)

    print("\nVeamos cual fue el caracter más repetido en la frase encriptada")
    count_appearances(encrypted_phrase)

    print("Frase Encriptada:", encrypted_phrase )
    print("Frase Desnecriptada:", decrypted_phrase)


    # Ahora vamos con el cripto sistema 2
    print("\nVamos ahora a trabajar con el criptosistema2")
    encrypted_phrase2 =  encrypt_phrase_as_vector(sanitized_phrase)
    print("\nFrase encriptada con el criptosistema2:", encrypted_phrase2)
    
    print("\nVeamos cual fue el caracter más repetido en la segunda frase encriptada")
    count_appearances(encrypted_phrase2)

    decrypted_phrase2 = desencrypt_phrase_as_vector(encrypted_phrase2)
    print("\nFrase desencriptada luego de encriptarla con el criptosistema2", decrypted_phrase2)
    count_appearances(decrypted_phrase2)



if __name__ == "__main__":
    main()



