def conversion(arg1, op):
    tipo_de_cambio = 0
    if op == 1:
        tipo_de_cambio = 0.25
        cadena = "soles peruanos"
    elif op == 2:
        tipo_de_cambio = 0.0013
        cadena = "pesos chilenos"
    elif op == 3:
        tipo_de_cambio = 0.00027
        cadena = "pesos colombianos"
    elif op == 3:
        tipo_de_cambio = 0.044
        cadena = "pesos mexicanos"
    else:
        print("Ingrese una opción válida")
    conversion = round(arg1 * tipo_de_cambio, 2)
    print(f'Los {arg1} {cadena} equivalen a {conversion} dolares')


if __name__ == '__main__':
    try:
        print("Qué moneda desea convertir a dólares.")
        op = int(input('''
            Ingresa el indice de la moneda que quieres convertir a dolar:
                [1] Moneda chilena a Dolar
                [2] Moneda colombiana a Dolar
                [3] Moneda argentida a Dolar
                [4] Moneda mexicana a Dolar
            Selecciona: '''))
        cantidad = int(input("¿Cuanto tienes?: "))
        conversion(cantidad, op)
    except:
        print('* * * * * * E R R O R * * * * * *')
        print('Por favor, Ingresa solo valores numericos')
