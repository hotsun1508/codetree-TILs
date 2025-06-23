a,b,c = map(int, input().split())
satisfied = False 

# a 이상 ~ b 이하 
for i in range(a, b+1):
    # c로 나누어 떨어지지 않으면, c의 배수가 없다는 뜻
    if i % c != 0:
        satisfied = True
    # c로 나누어 떨어지는 숫자가 하나라도 있으면 False 
    else: 
        satisfied = False

if satisfied == True:
    print("YES")
else:
    print("NO")

