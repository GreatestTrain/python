from time import sleep

def fibo_gen(max_value: int = None, max_element: int = None) -> int:
    n1, n2= 0, 1
    counter: int = 0
    while True:
        yield n1
        n1, n2 = n2, n1+n2
        counter += 1
        if n1 > max_value or counter > max_element-1:
            break

def run():
    fibonacci = fibo_gen(1000, 10)
    for element in fibonacci:
        print(element)
        sleep(0.25)

run()

