#https://www.acmicpc.net/problem/4673

totalNumber = set(range(1,10001))

sequence = set()

for number in totalNumber:
    nextNumber = 0
    for i in range(len(str(number))):
        nextNumber += int(str(number)[i])
    nextNumber += number
    sequence.add(nextNumber)

selfNumbers = totalNumber - sequence
selfNumberList = list(selfNumbers)
selfNumberList.sort()

for selfNumber in selfNumberList:
    print(selfNumber)