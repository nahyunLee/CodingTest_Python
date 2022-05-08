inputList = []

for i in range(5):
    inputList.append(int(input()))

burger = min(inputList[0], inputList[1], inputList[2])
drink = min(inputList[3], inputList[4])

print(burger + drink - 50)