

n = int(input("შეიყვანე დადებითი მთელი რიცხვი: "))

def fib(n):
    n1 = 0
    n2 = 1
    if n <= 0:
        print("არასწორი რიცხვი.")

    if n == 1:
        print(n1)

    if n == 2:
        print(n1)
        print(n2)

    if n > 2:
        print(n1)
        for i in range(n - 1):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            print(n3)

fib(n)
    

