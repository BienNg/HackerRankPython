n = int(input())
set_n = set(int(x) for x in input().split())
m = int(input())
set_m = set(int(x) for x in input().split())

l = list((set_n.union(set_m)).difference(set_n.intersection(set_m)))
print(l)
l.sort()
print(l)
for x in l:
    print(x)