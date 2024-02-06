

import random

rand_lst = []

def app_lst(lst):
    for i in range(1000):
        lst.append(str(i + 1) + ": ")
        lst.append(str(random.randint(0, 1000)) + "\n")
    return lst

app_lst(rand_lst)

with open("test1.txt", "w") as file:
    file.writelines(rand_lst)

with open("test1.txt", 'r') as file:
    num_lines = len(file.readlines())
    print("ფაილში შევსებული ხაზების რაოდენობა:", num_lines)

