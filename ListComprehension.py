if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    #Solution 1
    print([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a+b+c != n])

    #Solution 2
    lexiList = []
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                if(i+j+k != n):
                    list = [i, j, k]
                    lexiList.append(list)

    print(lexiList)