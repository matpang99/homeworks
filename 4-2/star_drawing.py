import random
import time

def func1(Height):
    for i in range(1,Height):
        print '*'*i+' '*((Height*2-1)-i*2)+'*'*i
    print '*'*(Height*2-1)
    return Height*(Height+1)-1

def func2(Height):
    print '*'*(Height*2-1)
    for i in range(1,Height):
        print '*'*(Height-i)+' '*((Height*2-1)-(Height-i)*2)+'*'*(Height-i)
    return Height*(Height+1)-1

def func3(Height):
    print '*'*(Height*2-1)
    for i in range(1,Height):
        print '*'*(Height-i)+' '*((Height*2-1)-(Height-i)*2)+'*'*(Height-i)
    for i in range(2,Height):
        print '*'*i+' '*((Height*2-1)-i*2)+'*'*i
    print '*'*(Height*2-1)
    return 2*Height*(Height+1)-4

def main():
    for i in range(3):
        a = random.randint(1,3)
        h = int(raw_input("Height : "))
        if a == 1:
            print func1(h)
        elif a == 2:
            print func2(h)
        elif a == 3:
            print func3(h)
        time.sleep(1)

main()
