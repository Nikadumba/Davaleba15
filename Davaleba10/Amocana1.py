
# ვირუსი მაქვს და მეორე დავალებისთვის ვერ ავამუშავე ტვინი, ბოდიში :)

import random

rand_lst = []

def app_lst(lst):
    for i in range(100):
        lst.append(random.randint(0, 100))
    return lst
    

def linear_search(search_list, x):
    for i in range(len(search_list)):
        if search_list[i] == x:
            return i
             
    return -1

num1 = int(input("შეიყვანე მოსაძებნი რიცხვი 0-დან 100-ის ჩათვლით: "))    
print(f"Original List: \n{app_lst(rand_lst)}")
print(linear_search(rand_lst, num1))

sorted_lst = sorted(rand_lst)


def binary_search(search_list2, y):
    low = 0
    high = len(search_list2) - 1
    mid = 0

    while low <= high:
        mid = (low + high ) // 2

        if search_list2[mid] < y:
            low = mid + 1
        elif search_list2[mid] > y:
            high = mid - 1
        else:
            return mid
        
    return -1

num2 = int(input("შეიყვანე კიდევ ერთი რიცხვი 0-დან 100-ის ჩათვლით: "))    
print(sorted_lst)
print(binary_search(sorted_lst, num2))
