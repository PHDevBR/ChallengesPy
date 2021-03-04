print("Insert a number: ", end="")
sentence = input()
ssplit = sentence.split()
for i in ssplit:
    number_transformed = int(ssplit[i])
    if number_transformed == 0:
        v0 += 1
    elif number_transformed == 1:
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
