'''



'''

texto = input("Introduza un texto")

contadorVogais = 0
contadorConsoantes = 0

#Algoritmo
for letra in texto:
    if letra.lower() in "aieou":
        contadorVogais = contadorVogais + 1
    elif letra == '':
        pass
    else:
        contadorConsoantes = contadorConsoantes + 1

    print(f"Vogais -> {contadorVogais}")
    print(f"Consoantes -> {contadorConsoantes}")
