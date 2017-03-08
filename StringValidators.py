if __name__ == '__main__':
    s = input()

    alphanumeric = False
    alphabetical = False
    digits = False
    lowercase = False
    uppercase = False

    for char in s:
        if str(char).isalnum():
            alphanumeric = True
        if str(char).isalpha():
            alphabetical = True
        if str(char).isdigit():
            digits = True
        if str(char).islower():
            lowercase = True
        if str(char).isupper():
            uppercase = True

    print(alphanumeric)
    print(alphabetical)
    print(digits)
    print(lowercase)
    print(uppercase)