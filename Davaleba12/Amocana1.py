

question = input("დაწერეთ წინადადება: ").lower().split(' ')

lst = []

for i in question:
    w_count = question.count(i)
    lst.append((i, w_count))

new_dict = dict(lst)

print(new_dict)
