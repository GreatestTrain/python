from typing import Callable

def make_division_by(divisor: float) -> Callable[[float], float]:
    def division(divident: float) -> float:
        assert divisor != 0, "Solo puedes ingresar numeros enteros en el dividendo"
        return divident/divisor
    return division

if __name__ == "__main__":
    
    division_by_3 = make_division_by(3)
    print(division_by_3(18)) # The expected output is 6
    division_by_5 = make_division_by(5)
    print(division_by_5(100)) # The expected output is 20
    division_by_18 = make_division_by(18)
    print(division_by_18(54))

    print(make_division_by(3)(18))

