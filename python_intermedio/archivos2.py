﻿def read():
    numbers = []
    with open("./archivos/numeros.txt", "r") as f: 
        for line in f:
            numbers.append(line)
    print(numbers)


def write():
    names = ["Facundo", "Gregorio", "Marta", "Susana", "Jose"]
    with open("./archivos/names.txt", "w") as f:
        for name in names: 
            f.write(name)
            f.write("\n")


def run():
    read()


if __name__ == '__main__':
    run()