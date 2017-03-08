def swap_case(s):
    string = ""
    for c in range(0,len(s)):
        if s[c].isupper():
            string += s[c].lower()
        else:
            string += s[c].upper()
    return string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)