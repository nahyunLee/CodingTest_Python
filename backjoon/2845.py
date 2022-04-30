# people, area = input().split()
# totalPeople = int(people) * int(area)
#
# list = []
# a,b,c,d,e = input().split()
# list.append(int(a))
# list.append(int(b))
# list.append(int(c))
# list.append(int(d))
# list.append(int(e))
#
# result = ""
# for i in range(5):
#     result += str(list[i] - totalPeople)
#     result += " "
#
# print(result)

a,b = map(int, input().split())
people = list(map(int, input().split()))
party = a*b
for i in people:
    print(i - party , end=" ")