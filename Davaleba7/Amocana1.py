

import math

lst = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]

def sum(*arg):
    return int(math.fsum(*arg))

print("სიაში არსებული რიცხვების ჯამი:", sum(lst))
