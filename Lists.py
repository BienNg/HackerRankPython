import sys
if __name__ == '__main__':
    N = int(input())
    list = []
    for _ in range(N):
        query = input()
        if(query == "print"):
            print(list)
        else:
            operation = query.split()
            op = operation[0]
            elements = operation[1:]
            op += "(" + ",".join(elements) + ")"
            eval("list."+op)




