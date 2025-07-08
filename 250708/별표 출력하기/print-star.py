n = int(input())

# 방법 1 
for i in range(1, n+1):  # 1부터 하나씩 증가하는 직각삼각형 
    # print("i :", i)
    for j in range(i):
        # print("j :", j)
        print("*", end=" ")
    print()

for i in range(1, n):  # n부터 하나씩 감소하는 직각삼각형 
    # print("i :", i)
    for j in range(n - i):
        # print("j :", j)
        print("*", end=" ")
    print()


# 방법 2 
# cnt = 1
# # print("cnt :", cnt)

# for i in range(2*n-1):  # 직각삼각형 줄의 개수 (전체 세로 길이)
#     # print("i :", i)
#     for j in range(cnt):  # 한 줄에 출력할 별의 개수 
#         # print("j :", j)
#         print("*", end=" ")
#     print()
    
#     if i < n-1:  # 0부터 시작하니까 n-1보다 작을 때까지는 별의 개수 1씩 증가 
#         cnt += 1
#     else:        # n부터는 별의 개수 1씩 감소 
#         cnt -= 1
    
#     # print(cnt)