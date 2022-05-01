totalSum = 0
for i in range(4):
    totalSum += int(input())

if totalSum < 60:
    hour = 1
    minute = 0
elif totalSum > 3600:
    hour = 59
    minute = 59
else:
    hour = totalSum//60
    minute = totalSum % 60

print(hour)
print(minute)