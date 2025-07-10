n = int(input())
cnt = 1

for i in range(1, 2*n):
    print("i :", i)
    for j in range(cnt):
        print("*", end="")
    print()
    print()
    
    if i < n: 
        cnt += 1
    else:
        cnt -= 1 

