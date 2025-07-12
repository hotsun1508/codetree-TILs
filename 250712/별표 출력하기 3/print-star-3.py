n = int(input())

# n = 5일 때 
# 공백 수 
    # 0, 1, 2, 3, 4
# 별의 개수 
    # 9, 7, 5, 3, 1 


for i in range(n): 
    for j in range(i): # 공백 개수
        print(" ", end=" ")
    
    for j in range(2 * (n-i) - 1): # 별 개수 
        print("*", end=" ")
    print()

