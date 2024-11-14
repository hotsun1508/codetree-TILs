a = int(input())


for i in range(a+1):
    if (i % 2 == 0 and i % 4 != 0) or ((i // 8) % 2 == 0) or (i % 7 < 4):
        continue
    
    print(i, end=" ")