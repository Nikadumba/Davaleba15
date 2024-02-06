
# დაწერეთ ლამბდა ფუნქცია, რომელიც დააბრუნებს სამის ჯერად რიცხვებს, ამის შემდეგ დაწერეთ ფუნქცია, 
# რომელსაც ატრიბუტებად გადაეწოდება ლისტი და ლამბდა ფუნქცია, ხაზობრივი ძიების და 
# ლამბდა ფუნქციის დახმარებით შეავსეთ ახალი ლისტი(ინდექსებით) და დააბრუნეთ მოცემული ლისტი.
# (ფუნქციამ უნდა დააბრუნოს ლისტი, რომელშიც შენახული იქნება სამის ჯერადი რიცხვების ინდექსები)

# გამარჯობა ნიკოლოზ, მოკლედ მაგ დავალებაში უნდა დაწერო ფუნქცია, ამ ფუნქციას გადაეცემა ორი ატრიბუტი, 
# ერთი ლისტი და მეორე ლამბდა ფუნქცია, უნდა დაატრიალო იტერაცია ამ ლისტში და შემდეგ if ხომ დაგჭირდება რომ შეამოწმო სამზე იყოფა თუ არა, 
# მაგრამ ამ იფში უნდა გამოიძახო გადმოცემული ლამბდა ფუნქცია და ატრიბუტად გადააწოდო ის რიცხვი რომელზეც იმყოფები იტერაციის დროს, 
# ლამბდამ შესაბამისად უნდა დააბრუნოს True ან False, თუ დააბრუნა True მაშინ შესაბამისი ინდექსი დაამატე ახალ ლისტში


lst1 = [1, 4, 3, 23, 9, 17, 16, 18, 0, 5, 7, 21]
lst2 = []
mult_three = list(filter(lambda a: a % 3 == 0, lst1))

print(mult_three)


# for func in mult_three:
#     print(func())

# def check_list(checked_list, lambda_func):
#     for y in range(len(checked_list)):
#         if checked_list[y] / 3 == 1:
#             lst2.append(checked_list[y])


# def check_list(checked_list, lambda_func):
#     for y in range(len(checked_list)):
#         if checked_list[y] % 3 == 0 and checked_list[y] > 0:
#             return lst2.append(checked_list.index(checked_list[y]))
#             return checked_list.index(checked_list[y])
#             # lst2.append(checked_list[y])


# for y in range(len(lst1)):
    
#     if lst1[y] in mult_three[]:
#         lst2.append(lst1[y])
    
#     else:
#         break
        
             
        
# check_list(lst1, mult_three)
# print(lst2)


    


