def merge_the_tools(string, k):
    set1 = set()
    list = []
    for i in range(0,len(string),k):
        word = string[i:i+k]
        for x in word:
            if x not in set1:
                set1.add(x)
                list.append(x)
        print("".join(list))
        list.clear()
        set1.clear()


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)