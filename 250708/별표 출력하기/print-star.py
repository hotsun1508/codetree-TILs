n = int(input())

# 방법 1 
# for i in range(1, n+1):
#     # print("i :", i)
#     for j in range(i):
#         # print("j :", j)
#         print("*", end=" ")
#     print()

# for i in range(1, n): 
#     # print("i :", i)
#     for j in range(n - i):
#         # print("j :", j)
#         print("*", end=" ")
#     print()


# # 방법 2 
# if n%2 == 0:
#     star = n/2
# else:
#     star = int((n+1)/2)

# cnt = 2*n -1 
cnt = 1
# print("cnt :", cnt)

for i in range(2*n-1): 
    # print("i :", i)
    for j in range(cnt):
        # print("j :", j)
        print("*", end=" ")
    print()
    
    if i < n-1:
        cnt += 1
    else:
        cnt -= 1
    
    # print(cnt)