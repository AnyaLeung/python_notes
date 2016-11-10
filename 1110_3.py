num = int(input('enter an int:'))
m = 1

while m <= num:
    print('*', end = "")
    m += 1

    if m % 2 == 0:
        print('+', end = "")
