#ROWS:
num = [1, 4, 5, 7, 8]
num2 = [1,2,4,6,7,8]
num3 = [0,2,4,5,7]
if 0 or 1 or 2 in num:
    print(num[0])
if 3 or 4 or 5 in num2:
    for i in range(0, len(num2)):
        if num2[i] > 2 and num2[i] < 6:
            print(num2[i])
if 6 or 7 or 8 in num3:
    print(num3[-1])