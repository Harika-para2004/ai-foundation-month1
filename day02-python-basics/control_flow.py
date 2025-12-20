for i in range (1,11):
    if i % 2 == 0:
        print(i, "is an even number")
    else :
        print(i, "is an odd number")

for i in range(1, 12):
    if i % 3 == 0:
        print(i, "is divisible by 3")

for i in range(1,11):
    if i == 4:
        break
    if i % 2 == 0 and i % 3 == 0:
        print(i, "is divisible by both 2 and 3")