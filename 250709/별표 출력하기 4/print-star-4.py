n = int(input())
cnt = 1

for i in range(1, 2*n):
    # print("i :", i)
    for j in range(n-cnt+1):
        # print("j :", j)
        print("*", end=" ")
    print()

    # print("before cnt :", cnt)
    if i < n:
        cnt += 1
    else:
        cnt -= 1
    
    # print("after cnt :", cnt)