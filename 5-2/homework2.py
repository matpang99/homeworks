import random

def sorting(list):
    check2 = 1
    while check2 >= 1:
        check = 0
        for i in range(19):
            if list[i] > list[i+1]:
                a = list[i+1]
                b = list[i]
                check = check + 1
            else:
                a = list[i]
                b = list[i+1]
            list[i] = a
            list[i+1] = b
        check2 = check
    return list

def main():
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

    numberList = sorting(numberList)

    data2 = ""
    f = open("sort.txt", "a")
    for i in range (19):
        data2 = data2 + "%d, " %numberList[i]
    data = "["+ data2 + "%d]" %numberList[19] + "\n"
    f.write(data)
    f.close()

main()
