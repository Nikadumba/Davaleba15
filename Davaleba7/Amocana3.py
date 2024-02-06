

text = str(input("შეიყვანე სტრიქონი: "))

def rev(txt):
    if len(txt) == 1:
        return txt
    else:
        return rev(txt[1:]) + txt[0]
    
print(rev(text))
