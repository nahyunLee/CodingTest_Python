import math
diagonal, width, height = map(int, input().split())


real = math.sqrt(diagonal**2/(width**2 + height**2))

realWidth = width * real
realHeight = width * real

print(str(math.floor(width * real)), str(math.floor(height * real)), sep=" ")
