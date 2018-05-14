import random
numberList = []
data2 = ""

for i in range(20):
    numberList.append(random.randint(1, 100))

f = open("sort.txt", "w")
for i in range (19):
    data2 = data2 + "%d, " %numberList[i]
data = "["+ data2 + "%d]" %numberList[19] + "\n"
f.write(data)
f.close()

check2 = 1
while check2 >= 1:
    check = 0
    for i in range(19):
        if numberList[i] > numberList[i+1]:
            a = numberList[i+1]
            b = numberList[i]
            check = check + 1
        else:
            a = numberList[i]
            b = numberList[i+1]
        numberList[i] = a
        numberList[i+1] = b
    check2 = check

data2 = ""
f = open("sort.txt", "a")
for i in range (19):
    data2 = data2 + "%d, " %numberList[i]
data = "["+ data2 + "%d]" %numberList[19] + "\n"
f.write(data)
f.close()
