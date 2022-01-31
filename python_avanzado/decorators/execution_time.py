from datetime import datetime
import random

def execution_time(func):
    def wrapper(time_message:str = 'Execution time:', *args, **kwargs):
        init_time = datetime.now()
        return_value = func(*args, **kwargs)
        # func()
        final_time = datetime.now()
        time_elapsed = final_time - init_time
        print(time_message, time_elapsed.total_seconds())
        return return_value
    return wrapper

def get_name(question: str = "Name: ") -> str:
    name: str = input(question)
    return name

def random_fun():
    print("======== Ejecutando random_fun =======")
    for _ in range(1,100000000):
        pass

def run():
    try:
            op = int(input("Que funcion quieres probar: "))
            if op==1:
                get_name_time = execution_time(get_name)
                student1 = execution_time(get_name)("Tiempo de ejecucion: ", question='Nombre: ')
                print("student1: ", student1)
                student2 = get_name_time("Tiempo de ejecucion: ")
                print("student2: ", student2)
            elif op==2:
                execution_time(random_fun)("Execution time: ")
            elif op==3:
                pass
            else:
                raise ValueError

    except ValueError as ve:
        print('Ingresa un valor en el rango.')
        run()


if __name__=="__main__":
    run()

    
    