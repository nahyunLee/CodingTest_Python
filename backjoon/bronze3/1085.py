x, y, w, h = map(int, input().split())
print(min(w, y, w-x, h-y))
