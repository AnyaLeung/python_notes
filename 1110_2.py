#顯示身高和標準體重的對照表，顯示的身高範圍和間隔由輸入控制，標準體重精確到小數點後兩位
a = int(input('begin num:'))
b = int(input('end num:'))
inv = int(input('interval:'))

while a <= b:
    print('%dcm     %.2fkg' % (a, (a - 80) * 0.7))
    a += inv
