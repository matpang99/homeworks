input_ = '''afsafsdfa df
adfasdfa d
sadfdsfsadfsadfsad'''

input = raw_input()

count = 0

for i in range(len(input_)-len(input)):
    if input[0] == input_[i]:
        textCount = 1
        for j in range(1,len(input)):
            if input[j] == input_[i+j]:
                textCount = textCount + 1
                continue
        if textCount == len(input):
            count = count + 1

print count
