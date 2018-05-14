# coding : matpang99
while True:
    print '1. + 2. - 3. * 4. exit'
    input = int(raw_input())
    if input == 4:
        break
    num1 = int(raw_input())
    num2 = int(raw_input())
    if input == 1:
        print num1, '+', num2, '=', num1 + num2
    elif input == 2:
        print num1, '-', num2, '=', num1 - num2
    elif input == 3:
        print num1, '*', num2, '=', num1 * num2
