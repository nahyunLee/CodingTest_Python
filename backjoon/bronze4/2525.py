hour, minute = map(int, input().split())
time = int(input())

resultHour = hour + time // 60
resultMinute = minute + time % 60

if resultMinute >= 60:
    resultHour += resultMinute // 60
    resultMinute = resultMinute % 60

if resultHour >= 24:
    resultHour -= 24

print(resultHour, resultMinute, sep=' ')