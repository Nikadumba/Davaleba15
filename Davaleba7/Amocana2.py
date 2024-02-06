

number = int(input("შეიყვანე რიცხვი: "))

def sum(num): 
    if len(str(num)) == 1: 
        return num 
    else:
        return int(num % 10) + sum(int(num / 10))  
   
   
print(sum(number))
