size = int(input())
pc = []
people = list(map(int, input().split()))
refuse = 0
flag = False
for i in range(size):
    want = people[i]
    for z in range(len(pc)):
        if want == pc[z]:
            refuse +=1
            flag = True
            break
    if flag is False:
        pc.append(want)
    flag = False

print(refuse)

