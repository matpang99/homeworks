num = int(raw_input())
factorial = num
while num > 1:
    factorial = factorial * (num - 1)
    num = num - 1
print factorial
