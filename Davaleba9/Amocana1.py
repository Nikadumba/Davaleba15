

import random

rand_lst = []

def app_lst(lst):
    for i in range(100):
        lst.append(random.randint(0, 1000))
    return lst
    
print(f"Original List: \n{app_lst(rand_lst)}")

rand_lst1 = sorted(rand_lst)
print(f"Sorted List: \n{rand_lst1}")

rand_lst2 = sorted(rand_lst, reverse=True)
print(f"Reversed Sorted List: \n{rand_lst2}")

rand_lst.sort()
print(f"Sorted List: \n{rand_lst}")

rand_lst.sort(reverse=True)
print(f"Reversed Sorted List: \n{rand_lst}")
