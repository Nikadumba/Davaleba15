

import functools

lst = [1, 2, 3, 4, 5]

try:
    mult = functools.reduce(lambda a, b: a * b, lst)
    mult = int(mult)
    print(mult)

except ValueError:
    print("სიაში უნდა იყოს მხოლოდ რიცხვები.")


