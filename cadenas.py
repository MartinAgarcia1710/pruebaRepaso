
frase_ingresada = input("Ingrese una frase (máximo 100 caracteres)")
'''
frase = [""] * 100
longitud_real = 0

for i in range(len(frase_ingresada)):
    if i < 100:
        frase[i] = frase_ingresada[i]
        longitud_real += 1

#Punto 2

cantidad_palabras = 0
en_palabra = False

for i in range(longitud_real):
    if frase[i] != " " and not en_palabra:
        cantidad_palabras += 1
        en_palabra = True
    elif frase[i] == " ":
        en_palabra = False

print(f"Cantidad de palabras: {cantidad_palabras}")

#Punto 3

primeras_palabras = [""] * 20
en_palabra = False
indice_letras = 0


for i in range(longitud_real):
    if frase[i] != " " and not en_palabra:
        if indice_letras < 20:
            primeras_palabras[indice_letras] = frase[i]
            indice_letras += 1
        en_palabra = True
    elif frase[i] == " ":
        en_palabra = False

print("Primeras letras de cada palabra: ")

for i in range(indice_letras):
    print(primeras_palabras[i])

#print(primeras_palabras)

#Punto 4
vocales = "aeiouAEIOU"
cantidad_vocales = 0

for i in range(longitud_real):
    for j in range(10):
        if frase[i] == vocales[j]:
            cantidad_vocales += 1

print(f"Cantidad de vocales en la cadena: {cantidad_vocales}")


#Punto 5

longitudes = [0] *20
indice_palabra = 0
en_palabra = False

for i in range(longitud_real):
    if frase[i]  != " ":
        if indice_palabra < 20:
            longitudes[indice_palabra] += 1
        en_palabra = True
    elif en_palabra:
        indice_palabra += 1
        en_palabra = False

print("Longitudes de cada palabra")

for i in range(indice_palabra + 1):
    print(f"Palabra {i + 1}: {longitudes[i]} letras")



'''















