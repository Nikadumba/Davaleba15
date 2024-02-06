

tuple1 = (1,2,3,4,5,6)
tuple2 = (4,5,5,6,6,7)

def tuple_change(tup1, tup2):
    set1 = set(tup1)
    set2 = set(tup2)
    combined_tuple = tuple(set1.union(set2)) 
    dublicated_values = list(set1.intersection(set2))
    print(combined_tuple)
    print(dublicated_values)
    
tuple_change(tuple1, tuple2)

