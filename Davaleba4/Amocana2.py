

text = str(input("შეიყვანე ტექსტი: "))
text_encoded = text.encode('ascii')

for i in range(len(text_encoded)):
    print(text_encoded[i])

