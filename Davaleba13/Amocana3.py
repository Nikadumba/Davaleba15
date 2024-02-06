

with open("test3.1.txt", "w") as file1:
    lst1 = ["1\n", "2\n", "3\n"]
    file1.writelines(lst1)

with open("test3.2.txt", "w") as file2:
    lst2 = ["4\n", "5\n", "6"]
    file2.writelines(lst2)

txt_files = ["test3.1.txt", "test3.2.txt"]
with open("test3.3.txt", "w") as file3:
    for i in txt_files:
        with open(i) as file4:
            for y in file4:
                file3.write(y)

with open("test3.3.txt", "r") as file5:
    read_file = file5.read()
    print(read_file)