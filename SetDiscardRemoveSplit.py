n = int(input())
s = set(map(int, input().split()))
commands = int(input())
for _ in range(commands):
    str = input()
    if str == "pop":
        eval("s.pop()")
    else:
        q = str.split(" ")
        line = q[0] + '(' + q[1] + ')'
        eval("s."+line)

print(sum(s))
