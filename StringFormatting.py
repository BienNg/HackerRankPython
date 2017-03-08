def print_formatted(number):
    binarylength = len('{}'.format(bin(number)))
    for i in range(1,number+1):
        print(str(i), end='')
        print(oct(i).replace('0o','').rjust(binarylength), end='')
        print(hex(i).upper().replace('0X','').rjust(binarylength), end='')
        print(str(bin(i)).replace('0b','').rjust(binarylength), end='')
        print("")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)