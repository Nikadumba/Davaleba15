

Total_sum = 0

while True:
    
    number = str(input("შეიყვანე რიცხვი: "))

    if number == "sum":
        print("შეყვანილი დადებითი რიცხვების ჯამი:", Total_sum)
        break

    if float(number) > 0:
        Total_sum += float(number)









