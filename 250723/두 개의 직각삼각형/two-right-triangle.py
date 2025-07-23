n = int(input())

# (n = 4)
    # 1번줄: 2n (0) => n-0
    # 2번줄: n-1 (2) n-1
    # 3번줄: n-2 (4) n-2
    # 4번줄: n-3 (6) n-3 

for i in range(n):

    for j in range(n-i, 0, -1):
        print("*", end="")
        print("_ :", j)


    for j in range(i):
        print(" "*2, end="")
        # print("_ :", j)


    for j in range(n-i, 0, -1):
        print("*", end="")
        # print("_ :", j)
    
    print()

