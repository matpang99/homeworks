while True:
    guess = 50
    a = 50
    t = 1
    input = int(raw_input())
    if input == 1:
        break
    num = int(raw_input())
    if input == 0:
        while guess != num:
            if guess < num:
                if a % 2 == 1:
                    a = a + 1
                a = a / 2
                guess = guess + a
                t = t + 1
                continue
            elif guess > num:
                if a % 2 == 1:
                    a = a + 1
                a = a / 2
                guess = guess - a
                t = t + 1
                continue
        else:
            print guess
            print t
