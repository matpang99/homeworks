# coding : matpang99
while True:
    print 'enter a number'
    number = int(raw_input())
    if number == 0:
        break
    for i in range(1, number + 1):
        print '*' * i
