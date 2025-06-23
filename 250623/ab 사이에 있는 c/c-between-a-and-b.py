a, b, c = map(int, input().split())
satisfied = False

for i in range(a, b+1):
    # a,b 사이에 c의 배수가 있는지 확인 
    if i%c == 0:
        satisfied = True

# 출력 
if satisfied == True:     
    print("YES")
else:
    print("NO")