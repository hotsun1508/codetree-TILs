n = int(input())

for i in range(n): #
    # print(_)
    for _ in range(n-i, 0, -1): # 하나씩 줄어들면서 반복 
        print("*", end=" ")
        # print(_)
    print()