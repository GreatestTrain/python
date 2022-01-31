from typing import List
import math

my_list: List[int] = [1, 2, 3, 4, 5]

my_iter = iter(my_list)

while True:
    try:
        print(next(my_iter))
    except StopIteration:
        print("Se acabo la iteracion")
        break

def funcion1(x=1, func = lambda x: x):
    return func(x)

numero = funcion1(15, lambda x: 2*math.sqrt(x) + 3)
print(numero)