import time

class Tabulator:
    def __init__(self, minValue = 0, maxValue = None, func = lambda x : x+3):
        self.minValue = minValue
        self.maxValue = maxValue
        self.func = func
        
    def __iter__(self):
        self.counter = self.minValue
        return self
    
    def __next__(self):
        bool = not self.maxValue or self.counter <= self.maxValue
        if bool:
            y = self.func(self.counter)
            self.counter+=1
            return y
        else:
            raise StopIteration

def run():
    func1 = lambda x: 2*x**2+5*x-7
    i = 0
    tab = Tabulator(i, 5, func1)

    for elemento in tab:
        print(elemento)

    tab = iter(tab)
    print("""
╒══════ Tabulador ══════╕
│    x      │      y    │
├┄┄┄┄┄┄┄┄┄┄┄┼┄┄┄┄┄┄┄┄┄┄┄┤
""", end="")
                        
    while True:
        try:
            print("│", i, "\r\t    │", next(tab),"\r\t\t\t│")
            time.sleep(0.03)
            i+=1
        except StopIteration:
            print("╘═══════════╧═══════════╛")
            print("Se acabo la iteracion")
            
            break
run()