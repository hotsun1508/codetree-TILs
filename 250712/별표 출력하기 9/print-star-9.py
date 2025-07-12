n = int(input())

# 공백 개수
    # n-1, n-2, n-3 ...
# 별의 개수
    # 1, 3, 5 ... 2n-1

for i in range(1, n+1):
    for _ in range(n-i):
        print(" ", end=" ")
    
    for _ in range(2*i - 1):
        print("*", end=" ")
    print()


    