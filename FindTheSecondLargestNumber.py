if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list = list(arr)
    list.sort()
    max = list[n-1]
    while list[len(list)-1] == max:
        list.remove(max)

    print(list[len(list)-1])