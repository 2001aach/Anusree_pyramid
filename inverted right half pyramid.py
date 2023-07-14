# Inverted right half pyramid pattern

n = 7
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(i):
        print('*',end=" ")
    print()