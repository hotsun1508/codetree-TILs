a, b = map(int, input().split())
satisfied = False

for i in range(a, b+1):
    # 공약수 존재하는지 확인 
    # 8, 10: 
        # 8: 1, 2, 4, 8
        # 10: 1, 2, 5, 10 
        # 공약수: 2 
    if 1920 % i == 0 and 2880 % i == 0:  
        satisfied = True
    

if satisfied == True:
    print(1)
else: 
    print(0)

