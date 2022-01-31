from datetime import datetime
from time import sleep
import random

class No_asertaste(Exception):
    message: str = ""
    # print(f'{type(message)=}')
    def __init__(self, *args):
        if args:
          self.message = args[0]
        else:
          self.message = "Error. El numero era otro"

    def __str__(self):
        if self.message:
            # return 'MyCustomError, {0} '.format(self.message)
            print('El verdadero valor era: ')

def execution_time(func):
    def wrapper(time_message:str = 'Execution time:', *args, **kwargs):
        init_time = datetime.now()
        return_value = func(*args, **kwargs)
        # func()
        final_time = datetime.now()
        time_elapsed = final_time - init_time
        # print(time_message, time_elapsed.total_seconds())
        return time_elapsed
    return wrapper

SERPIENTE = [
    """
          < * * * * * *




""",
"""
        < * * * * * *




""",
"""
      < * * * * * *




""",
"""
    < * * * * * *




""",
"""
  < * * * * * *




""",
"""
* * * * * *
V



""",
"""
* * * *
*
*
V

""",
"""
* *
*
*
*
* >
""",
"""

*
*
*
* * * >
""",
"""



*
* * * * * >
""",
"""




 * * * * * * >
""",
"""




   * * * * * * >
""",
"""




     * * * * * * >
""",
"""




       * * * * * * >
""",
"""




         * * * * * * >
""",

"""


                       ^ 
                       *
               * * * * *
""",
"""
                       ^ 
                       *
                       *
                       *
                   * * *
""",

"""
                   < * * 
                       *
                       *
                       *
                       *
""",
"""
               < * * * *
                       *
                       *
                       
                       
""",
"""
             < * * * * *
                       *
                       
                       
                       
"""
]


def run():
    timer: int = random.randint(5, 10)
    timer *= 20
    input("Presiona enter para empezar")
    def ciclos():
        for i in range(0, timer):
            #print("Tiempo restante: ", int(timer-i/4), end="")
            print(SERPIENTE[i%20])
            sleep(0.04)
        print("\n\n\n")
    print("\n\n")
    nro_giros = execution_time(ciclos)("Tiempo de ejecucion: ")
    print(nro_giros.total_seconds())
    print(int(nro_giros.total_seconds()) == timer)
    # for i in range(1, 4*random.randint(3,10), 4):
    # for i in range(0, 40):
    #     print(i)

    #     op = int(input("pausa"))

if __name__=="__main__":
    run()


