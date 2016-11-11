num = int(input('enter an int:'))
m = 1

while m <= num:
    if m % 2 == 0:
        print('*', end = "")

    if m % 2 == 0:
        print('+', end = "")

    m += 1

print('\n')
