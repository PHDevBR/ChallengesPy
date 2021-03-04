print("Insert a number: ", end="")
sentence = str(input())
ssplit = sentence.split(",")
v1, v2, v3, v4, v5, v6, v7, v8, v9 = 0,0,0,0,0,0,0,0,0
for i in ssplit:
    number_transformed = int(i)
    if number_transformed == 1:
        v1 += 1
    elif number_transformed == 2:
        v2 += 1
    elif number_transformed == 3:
        v3 += 1
    elif number_transformed == 4:
        v4 += 1
    elif number_transformed == 5:
        v5 += 1
    elif number_transformed == 6:
        v6 += 1
    elif number_transformed == 7:
        v7 += 1
    elif number_transformed == 8:
        v8 += 1
    elif number_transformed == 9:
        v9 += 1
if v1 >= 2:
    print("1: ")
    print(1)
if v2 >=2:
    print("2: ")
    print(2 * (v2 - 1) * 2)
if v3 >=2:
    print("3: ")
    print(3 * (v3 - 1) * 3)
if v4 >=2:
    print("4: ")
    print(4 * (v4 - 1) * 4)
if v5 >=2:
    print("5: ")
    print(5 * (v5 - 1) * 5)
if v6 >=2:
    print("6: ")
    print(6 * (v6 - 1) * 6)
if v7 >=2:
    print("7: ")
    print(7 * (v7 - 1) * 7)
if v8 >=2:
    print("8: ")
    print(8 * (v8 - 1) * 8)
if v9 >=2:
    print("9: ")
    print(9 * (v9 - 1) * 9)
