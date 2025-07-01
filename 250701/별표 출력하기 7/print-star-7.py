n = int(input())

# 방법 1: 반복문 하나로 해결 
# for i in range(1, n+1):
#     # print("n :", n)
#     print("* " * i)

# 방법 2: 반복문 2개 사용 
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()