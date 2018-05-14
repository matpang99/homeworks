count = 0

input_ = '''hello world
hello world hello'''.split()

input = raw_input().lower()

for i in range(len(input_)):
    if input_[i] == input:
        count = count + 1

print count
