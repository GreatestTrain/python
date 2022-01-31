import time

class FiboIter():
    
    def __init__(self, maxValue = None):
        self.maxValue = maxValue
    
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        bool = not self.maxValue or self.counter < self.maxValue
        if bool and self.counter == 0:
            self.counter +=1
            return self.n1
        elif bool and self.counter == 1:
            self.counter += 1
            return self.n2
        elif bool:
            self.aux = self.n1 + self.n2
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux
        else:
            raise StopIteration

if __name__=="__main__":
    fibonacci = iter(FiboIter(15))
    while True:
        try:
            i = next(fibonacci)
            print(i)
            time.sleep(0.25)
        except StopIteration:
            print("Se acabo la iteracion")
            break
