import os

nombre = input("¿Cual es tu nombre?: ")
nombre = nombre.capitalize()
nombre = nombre.strip()
print("Tu nombre es:" , nombre , end = ".\n" , sep= " ")
# print(len(nombre))
# print(nombre[3])

# for i in range(0, len(nombre), 2):
#     print(nombre[i])

for i in nombre:
    if i.capitalize() == ("A" or "E" or "I" or "O" or "U"):
        continue
    else:
        print(i)
