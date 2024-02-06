

lst = ["cat", "refer", "dog", "noon"] 

palindr = list(filter(lambda a: a == a[::-1], lst))

print(palindr)

