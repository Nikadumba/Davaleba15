

txt1 = str(input("დაწერე პირველი ტექსტი: "))
txt2 = str(input("დაწერე მეორე ტექსტი: "))

def anagram(x, y):
    x = x.lower()
    y = y.lower()
    if (sorted(x) == sorted(y)):
        return "პირველი და მეორე ტექსტები ანაგრამებია."
    else:
        return "პირველი და მეორე ტექტსები ანაგრამები არ არის."
    
print(anagram(txt1, txt2))


