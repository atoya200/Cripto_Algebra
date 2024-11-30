a = 3
b = 21


characters = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9,
    "K": 10, "L": 11, "M": 12, "N": 13, "Ñ": 14,
    "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23,
    "X": 24, "Y": 25, "Z": 26, " ": 27, "*": 28
}

numbers = {
    0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J",
    10: "K", 11: "L", 12: "M", 13: "N", 14: "Ñ",
    15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U", 22: "V", 23: "W",
    24: "X", 25: "Y", 26: "Z", 27: " ", 28: "*"
}


""" 
    Función que toma el caracter y devuelve su número correspondiente
"""
def translate_character(character):
    if isinstance(character, str): 
        return characters[character.upper()]

    raise Exception("El valor recibido debe ser un caracter")

""" 
    Función que toma el número y devuelve un caracter dado
"""
def translate_number(number):
    if isinstance(number, int): 
        return numbers[number]

    raise Exception("El valor recibido debe ser un caracter")