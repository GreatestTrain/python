def run():
    palabra = input("Escribe una palabra: ")
    palindromo(palabra)

def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    if palabra == palabra[::-1]:
        print("Es un palíndromo.")
    else:
        print("No es un palindromo")

if __name__ =='__main__':
    try:
        run()
    except:
        print("ERROR.")
