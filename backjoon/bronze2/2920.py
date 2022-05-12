inputList = list(map(int, input().split(" ")))
result = "mixed"
aflag = True
dFlag = True

if inputList[0] == 1:
    for i in range(7):
        if inputList[i] +1 != inputList[i+1]:
            aflag = False
    if aflag is True :
        result = "ascending"

if inputList[0] == 8:
    for i in range(7):
        if inputList[i] -1 != inputList[i+1]:
            dFlag = False
    if dFlag is True :
        result = "descending"

print(result)