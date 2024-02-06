

import random

lst = []

for i in range(10):
    r = random.randint(1, 100)
    lst.append(r)

print(lst)

lst.sort()
print("მინიმალური მნიშვნელობა:", lst[0])
print("მაქსიმალური მნიშვნელობა:", lst[-1])