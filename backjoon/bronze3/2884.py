hour, minute = map(int, input().split())

if hour == 0 and minute < 45:
    hour = 23
    minute = 60 - 45 + minute

else:
    resultMin = minute-45
    if resultMin < 0:
        hour -=1
        minute = 60 + resultMin

    else:
        minute = resultMin

print(hour, minute, sep = " ")





