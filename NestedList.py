if __name__ == '__main__':
    list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        personX = [name, score]
        list.append(personX)

    sorted_list = sorted(list, key=lambda tup: tup[1])

    #Delete worst grade
    worst_grade = sorted_list[0][1]
    while sorted_list[0][1] == worst_grade:
        sorted_list.pop(0)

    second_worst = sorted_list[0][1]
    while sorted_list[len(sorted_list)-1][1] != second_worst:
        del sorted_list[-1]

    sorted_list.sort()
    for i in range(0,len(sorted_list)):
        print(sorted_list[i][0])




