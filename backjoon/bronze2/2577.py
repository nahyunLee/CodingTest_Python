a = int(input())
b = int(input())
c = int(input())

num = list(str(a*b*c))
numList = [0,0,0,0,0,0,0,0,0,0]
for i in range(len(num)):
    numList[int(num[i])]+=1

for x in range(len(numList)):
    print(numList[x])

