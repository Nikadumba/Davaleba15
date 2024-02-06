

num1 = float(input("შეიყვანე პირველი რიცხვი: "))
num2 = float(input("შეიყვანე მეორე რიცხვი: "))
oper = input("შეიყვანე მათემატიკური ოპერატორი: ")

calc_dict = {"+": num1 + num2, "-": num1 - num2, "*": num1 * num2, "/": num1 / num2, "%": num1 % num2, "**": num1 ** num2, "//": num1 // num2}

print("შედეგი:", calc_dict.get(oper))
