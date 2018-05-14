input = open("input.txt", "r")
inputList = input.read().split("\n")
inputList1 = []
inputList2 = []

for i in range(10):
    inputList1.append(inputList[i])
    inputList2.append(inputList[i+11])
    inputList1[i] = inputList1[i].split()
    inputList2[i] = inputList2[i].split()

a = list(range(10))
b = list(range(10))
c = list(range(10))

sumList = [a,a,a,a,a,a,a,a,a,a]
subtractList = [b,b,b,b,b,b,b,b,b,b]
matrixList = [c,c,c,c,c,c,c,c,c,c]

for a in range(10): #sumList and subtractList
    for b in range(10):
        sumList[a][b] = int(inputList1[a][b]) + int(inputList2[a][b])
        subtractList[a][b] = int(inputList1[a][b]) - int(inputList2[a][b])

multiplySum = 0
for x in range(10): #matrixList
    for k in range(10):
        multiplySum = multiplySum + int(inputList1[x][y]) * int(inputList[k][z])
        matrixList[]


input.close()

output = open("output.txt", "w+")
data = ''
for i in range(10):
    data = data + str(sumList[i]) + "\n"
data = data + "\n"
for i in range(10):
    data = data + str(subtractList[i]) + "\n"
output.write(data)
output.close()
