

ricxvi1 = float(input("დაწერე პირველი რიცხვი: "))
ricxvi2 = float(input("დაწერე მეორე რიცხვი: "))
operator = input("მიუთითე მათემატიკური ოპერატორი: ")

if operator == "+":
    print(ricxvi1 + ricxvi2)

elif operator == "-":
    print(ricxvi1 - ricxvi2)

elif operator == "*":
    print(ricxvi1 * ricxvi2)

elif operator == "/":
    print(ricxvi1 / ricxvi2)

elif operator == "//":
    print(ricxvi1 // ricxvi2)

elif operator == "%":
    print(ricxvi1 % ricxvi2)

elif operator == "**":
    print(ricxvi1 ** ricxvi2)

else:
    print("მიუთითე სწორი მათემატიკური ოპერატორი.")