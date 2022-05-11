size = int(input())

name = []
for i in range(size):
    name.append(str(input()))

result = list(name[0])
for i in range(len(result)):
    temp = result[i]
    for y in range(size-1):
        if name[y+1][i] != temp:
            result[i] = '?'
            break

print(''.join(result))
