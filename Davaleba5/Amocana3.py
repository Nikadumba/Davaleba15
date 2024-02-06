

my_llist = [43, '22', 12, 66, 210, ["hi"]]

# a.
print("210-ის ინდექსია:",my_llist.index(210))

# b. რადგან პირობაში "ბოლო ელემენტში" წერია, append არ გავაკეთე.
my_llist[-1] = ["hi", "hello"]

# c.
my_llist.pop(2)
print(my_llist)

# d. კოპირების მაგივრად შემეძლო my_llist მნიშვნელობა მიმენიჭებინა და შემდეგ ორივე ლისტი გასუფთავდებოდა.
my_llist_2 = my_llist.copy() 
my_llist_2.clear()

print(my_llist)
print(my_llist_2)