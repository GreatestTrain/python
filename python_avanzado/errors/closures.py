from typing import Callable

def makeRepeaterOf(number: int) -> Callable[[str], str]:

    def repeater(string: str) -> str:
        assert type(string) == str, "Solo puedes utilizar cadenas"
        return string*number

    return repeater

repeat5 = makeRepeaterOf(5)
repeat10 = makeRepeaterOf(10)
print(repeat5("hola"))

