n = int(input())

# # 방법 1
for i in range(1, n+1):
    print("*"*(i*2-1))
    # print(i)

# 규칙 찾기 
# 1 -> 1 = 1*2 - 1 = 1
# 2 -> 3 = 2*2 - 1 = 3
# 3 -> 5 = 3*2 - 1 = 5
# 4 -> 7 = 4*2 - 1 = 7
# 5 -> 9 = 5*2 - 1 = 9 


# 방법 2
# for i in range(1, 2*n, 2):
#     for j in range(i):
#         print("*", end="")
#     print()