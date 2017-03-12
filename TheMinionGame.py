def minion_game(string):
    kevinPoints = 0
    stuartPoints = 0
    for i in range(len(string)):
        if string[i] in ('A','E','I','O','U'):
            kevinPoints += len(string)-i
        else:
            stuartPoints += len(string)-i

    if kevinPoints > stuartPoints:
        print("Kevin " + str(kevinPoints))
    elif stuartPoints > kevinPoints:
        print("Stuart " + str(stuartPoints))
    else:
        print("Draw")


if __name__ == '__main__':
    minion_game("BANANA")