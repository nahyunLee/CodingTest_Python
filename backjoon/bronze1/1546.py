size = int(input())
score = list(map(int, input().split()))
maxScore = max(score)
sumInt = 0

for i in range(size):
    sumInt += score[i]/maxScore*100

print(sumInt/size)

