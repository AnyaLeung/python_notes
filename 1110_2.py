a = int(input('begin num:'))
b = int(input('end num:'))
inv = int(input('interval:'))

while a <= b:
    print('%dcm     %.2fkg' % (a, (a - 80) * 0.7))
    a += inv
