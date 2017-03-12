import string

def print_rangoli(size):
    lowercase = string.ascii_lowercase
    for i in range(size-1, -1, -1):
        right = '-'.join(lowercase[i+1 : size])
        left = ''.join(reversed(right))
        print((left +"-"+ lowercase[i] + "-" + right).center(size+3*(size-1), "-"))
    for i in range(1, size):
        right = '-'.join(lowercase[i+1: size])
        left = ''.join(reversed(right))
        print((left +"-"+ lowercase[i] + "-" + right).center(size+3*(size-1), "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)