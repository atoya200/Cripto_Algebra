from analyze_phrase import sanctify_phrase, count_appearances
from cryptography_1 import encrypt_phrase, desencrypt_phrase
from cryptography_2 import encrypt_phrase_as_vector, desencrypt_phrase_as_vector



def main():
    long_phrase = "La capacidad para analizar y ajustar parámetros avanzados garantiza la adaptabilidad de las aplicaciones actuales."
    sanitized_phrase = sanctify_phrase(long_phrase)
    encrypted_phrase = encrypt_phrase(sanitized_phrase)
    decrypted_phrase = desencrypt_phrase(encrypted_phrase)

    print("Frase original:", long_phrase )
    print("Frase Sanitizada:",  sanitized_phrase)

    # Vamos a ver cual fue el caracter que más aparecio en la original y sus posciones
    print("\nVeamos cual fue el caracter más repetido en la frase original")
    count_appearances(sanitized_phrase)

    print("\n\nFrase Encriptada por el cripto sistema 1:", encrypted_phrase )
    print("Frase Desnecriptada luego de aplicarle la encriptación del sistema 1:", decrypted_phrase)
    
    print("\nVeamos cual fue el caracter más repetido en la frase encriptada")
    count_appearances(encrypted_phrase)



    # Ahora vamos con el cripto sistema 2
    
    print("\nVamos ahora a trabajar con el criptosistema2")
    encrypted_phrase2 =  encrypt_phrase_as_vector(sanitized_phrase)
    print("\nFrase encriptada con el cripto sistema 2:", encrypted_phrase2)
    
    print("\nVeamos cual fue el caracter más repetido en la segunda frase encriptada")
    count_appearances(encrypted_phrase2)

    decrypted_phrase2 = desencrypt_phrase_as_vector(encrypted_phrase2)
    print("\nFrase desencriptada luego de encriptarla con el criptosistema2", decrypted_phrase2)
    
    print("\nVeamos cual fue el caracter más repetido en la frase desencriptada luego de aplicarle el cripto sistema 2")
    count_appearances(decrypted_phrase2)



if __name__ == "__main__":
    main()



