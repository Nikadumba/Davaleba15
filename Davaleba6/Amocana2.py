

txt = str(input("დაწერე სტრიქონი: "))
symb = str(input("დაწერე სიმბოლო: "))

def count_symb(x, y):
    return x.count(y)

print(count_symb(txt, symb))

