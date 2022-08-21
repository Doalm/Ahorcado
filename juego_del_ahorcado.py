import random
import os # para limpiar la pantalla

archivo = open ("data.txt", "r", encoding="utf-8")
archivo = archivo.read()
archivo = archivo.split("\n")
numerado = enumerate(archivo)


def decorado():
    print("------------------------------")
    print("********************************")
    print("Bienvenido al juego del ahorcado")
    print("********************************")
    print("------------------------------")
    return
def aleatorio(archivo):
    palabra_secreta = random.choice(archivo)
    return palabra_secreta

def normal(s):
    remplace = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in remplace:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def limpiar():
    os.system("cls")
    return

def comienza():
    limpiar()
    nueva = aleatorio(archivo)
    nueva = normal(nueva)
    print("Su palabra consta de {} letras".format(len(nueva)))
    adivinar = len(nueva) * "_"
    while nueva != adivinar:
        decorado()
        print(adivinar)
        letra = str(input("Ingrese una letra: ").lower())
        if letra in nueva:
            adivinar = list(adivinar)
            for i, x in enumerate(nueva):
                if x == letra:
                    adivinar[i] = x
            adivinar = "".join(adivinar)
        limpiar()
    print("Ganaste tu palabra era: {}".format(nueva))   

if __name__ == "__main__":
    comienza()
    


