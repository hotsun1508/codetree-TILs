n = int(input())
satisfied = False

# n이라고 넣으면, n-1까지임 
for i in range (2, n):
    # 주어진 정수가 n-1이하의 어떤 정수로 나누어 떨어지는지 확인 
    if n % i == 0: 
        satisfied = True
    
if satisfied == True:
    print("C")
else:
    print("N")
