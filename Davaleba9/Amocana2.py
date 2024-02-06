

import random

# Buble Sort
rand_lst = []

def app_lst(lst1):
    for i in range(100):
        lst1.append(random.randint(0, 1000))
    return lst1
    
print(f"Original List: \n{app_lst(rand_lst)}")

def bubbleSort(lst2):    
    length = len(lst2)    
    for i in range(length):        
        swapped = False        
        
        for j in range(length - 1):            
            if lst2[j] > lst2[j + 1]:                
                lst2[j], lst2[j+1] = lst2[j+1], lst2[j]                
                swapped = True        
        
        if swapped == False:            
            break
   
bubbleSort(rand_lst)
print(f"Sorted List: \n{rand_lst}")

# Selection Sort
rand_lst2 = []

def app_lst(lst3):
    for i in range(100):
        lst3.append(random.randint(0, 1000))
    return lst3
    
print(f"Original List N2: \n{app_lst(rand_lst2)}")

def selectionSort(lst4):    
    for i in range(len(lst4)):        
        min_index = i        
        for j in range(i + 1, len(lst4)):            
            if lst4[j] > lst4[min_index]:                
                min_index = j        
                lst4[i], lst4[min_index] = lst4[min_index], lst4[i]

selectionSort(rand_lst2)
print(f"Reversed Sorted List N2: \n{rand_lst2}")


