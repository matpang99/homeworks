while True:
    guess = 50
    num = 101
    t = 1
    input = int(raw_input())
    if input == 1:
        break
    if input == 0:
        answer = int(raw_input())
        while guess != answer:
            t = t + 1
            if num % 2 == 0:
                if answer < guess:
                    num = num / 2 - 1
                    if num % 2 == 0:
                        guess = guess - (num / 2 + 1)
                        continue
                    if num % 2 == 1:
                        guess = guess - ((num + 1) / 2)
                        continue
                if guess < answer:
                    num = num / 2
                    if num % 2 == 0:
                        guess = guess + (num / 2)
                        continue
                    if num % 2 == 1:
                        guess = guess + ((num + 1) / 2)
                        continue
            if num % 2 == 1:
                num = (num - 1) / 2
                if answer < guess:
                    if num % 2 == 0:
                        guess = guess - (num / 2 + 1)
                        continue
                    if num % 2 == 1:
                        guess = guess - ((num + 1) / 2)
                        continue
                if guess < answer:
                    if num % 2 == 0:
                        guess = guess + (num / 2)
                        continue
                    if num % 2 == 1:
                        guess = guess + ((num + 1) / 2)
                        continue
        else:
            print guess
            print t
