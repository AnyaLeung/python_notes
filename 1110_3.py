＃編寫一段程序，交替顯示+ *。總個數等於輸入的整數值，另外，
#當輸入０以下的整數時，什麼也不顯示(?)

num = int(input('enter an int:'))
m = 1

while m <= num:
    print('*', end = "")

    if m % 2 == 0:
        print('+', end = "")

    m += 1

print('\n')
