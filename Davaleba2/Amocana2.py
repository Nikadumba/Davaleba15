

text = input("შეიყვანე სასურველი ტექსტი: ")
check1 = "small"
check2 = "tall"
check3 = "middle"


if check1 in text:
    print(f"{check1} მოიძებნა ტექსტში.")

elif check2 in text:
    print(f"{check2} მოიძებნა ტექსტში.")

elif check3 in text:
    print(f"{check3} მოიძებნა ტექსტში.")

else:
    print("ტექსტში არ მოიძებნა სიტყვები: small, tall ან middle.")
