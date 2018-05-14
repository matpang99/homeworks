# coding : matpang99
while True:
    print 'input your dan'
    dan = int(raw_input())
    if dan == 0:
        break
    elif 0 < dan < 10:
        for i in range(1, 10):
            print dan, '*', i, '=', dan * i
    else:
        print 'input is too big!'
