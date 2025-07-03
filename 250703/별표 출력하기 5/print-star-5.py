n = int(input())

for i in range(n, 0, -1): # 전체 반복 횟수 (행 개수)
    # print(i)
    for j in range(i, 0, -1): # i만큼 별 반복 (열 개수)
        # print("j :", j)
        # print("i :", i)
        print("*"*i, end=" ")  # 한번에 찍히는 별 개수 
    print()

