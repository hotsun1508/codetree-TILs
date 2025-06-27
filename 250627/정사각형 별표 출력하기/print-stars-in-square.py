n = int(input())

for i in range(n): 
    for j in range(n):
        print("*", end="") # 같은 줄일 때는 붙여주고
    print() # 다른 줄일 때는 한 줄 띄어줌 