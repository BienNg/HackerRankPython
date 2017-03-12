for i in range(2):
    top_s = 'S' * 16
    top_e = 'E' * 16
    top_n = 'N' * 8
    top_n2 = 'N' * 4
    top_d = 'D' * 11
    print(top_s, top_e.rjust(len(top_s)+2), #S, E
          "  " + top_n, " " * (12) + top_n2, #N
          " "+top_d,)

for i in range(4):
    middle_s1 = 'S'*4
    middle_e1 = 'E'*4
    middle_n1 = 'N'*4
    middle_d1 = 'D'*4
    print(middle_s1, middle_e1.rjust(len(top_s)+2), #S, E
          middle_n1.rjust(len(top_s) + 2), " "*i + middle_n1, " " * (11-i) + middle_n1, #N
          " "+middle_d1," " * 4 + " " *i + middle_d1)

for i in range(2):
    middle_s2 = 'S' * 16
    middle_e2 = 'E' * 16
    middle_n2 = 'N' * 4
    middle_d2 = 'D' * 4
    print(middle_s2, middle_e2.rjust(len(top_s)+2), #S, E
        "  "+middle_n2, " "*4+" "*i + middle_n2, " " * (7-i) + middle_n2, #N
          " " + middle_d2, " " * 8  + middle_d1)

for i in range(4):
    middle_s3 = 'S' * 4
    middle_e3 = 'E' * 4
    middle_n3 = 'N' * 4
    print(middle_s3.rjust(len(middle_s2)),"  "+ middle_e3, #S, E
          middle_n3.rjust(len(top_s) + 2), " " * 6 + " " * i + middle_n3, " " * (5-i) + middle_n3, #N
          " " + middle_d1, " " * (7-i) + middle_d1)

for i in range(2):
    bottom_s = 'S' * 16
    bottom_e = 'E' * 16
    bottom_n = 'N' * 4
    print(bottom_s, "  " + bottom_e, #S, E
          "  " + middle_n3, " " * 10 + " " * i + middle_n3, " " * (1-i) + bottom_n, #N
          " " + middle_d1 + "D"*8)

print()
print()

for i in range(2):
    top_n = 'N' * 8
    top_n2 = 'N' * 4
    top_d = 'D' * 11
    top_u = 'U' * 4
    top_e = 'E' * 16
    top_s = 'S' * 16
    print(top_n, " " * (12) + top_n2,
          " " + top_u, " " * 8, top_u, #N
          " "+top_d,
          " "*7+top_e,
          " " + top_s)

for i in range(4):
    middle_s1 = 'S' * 4
    middle_e1 = 'E' * 4
    middle_n1 = 'N' * 4
    middle_d1 = 'D' * 4
    print(middle_n1, " " * i + middle_n1, " " * (11 - i) + middle_n1,
          " " + top_u, " " * 8, top_u, #N
          " "+middle_d1," " * 4 + " " *i + middle_d1,
          " " * (5-i) + middle_e1,
          " " * 13 + middle_s1)

for i in range(2):
    middle_s2 = 'S' * 16
    middle_e2 = 'E' * 16
    middle_n2 = 'N' * 4
    middle_d2 = 'D' * 4
    print(middle_n2, " " * 4 + " " * i + middle_n2, " " * (7 - i) + middle_n2,
          " " + top_u, " " * 8, top_u, #N
          " " + middle_d2, " " * 8  + middle_d1,
          " " + middle_e2,
          " " + top_s)

for i in range(4):
    middle_s3 = 'S' * 4
    middle_e3 = 'E' * 4
    middle_n3 = 'N' * 4
    print(middle_n2, " " * 6 + " " * i + middle_n3, " " * (5 - i) + middle_n3,
          " " + top_u, " " * 8, top_u, #N
          " " + middle_d1, " " * (7-i) + middle_d1,
          " "," " * i + middle_e1,
          " " * 25 + middle_s1)

for i in range(2):
    bottom_s = 'S' * 16
    bottom_e = 'E' * 16
    bottom_n = 'N' * 4
    print(middle_n3, " " * 10 + " " * i + middle_n3, " " * (1 - i) + bottom_n,
              " " + top_u * 4 + "UU", #N
          " " + middle_d1 + "D"*8,
          " " * 6 + bottom_e,
          " " + top_s)