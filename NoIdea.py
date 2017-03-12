nm = input().split(" ")
array = input().split(" ")
a = set(input().split(" "))
b = set(input().split(" "))

points = 0

for x in array:
    if x in a:
        points+=1
    elif x in b:
        points -=1

print(points)