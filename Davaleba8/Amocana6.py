

lst = ['hello', 'world', 'coding']
ending = "ing"

try:
    ending = list(filter(lambda a: a.endswith(ending), lst))
    print(ending)

except AttributeError:
     print("სია უნდა შეიცავდეს მხოლოდ სტრიქონებს.")


