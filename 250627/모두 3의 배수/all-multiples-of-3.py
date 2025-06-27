n = list(map(int, input().split("\n"))) # 방법 1: map 사용
# input_str = int(input())
# n = [int(input()) for _ in range(input_str)] # 방법 2: List comprehension
satisfied = False

for i in n:
    if i%3 == 0:
        satisfied = True
    else: 
        satisfied = False
        break     # 1개라도 3의 배수가 아니면 break 해야함 
    
if satisfied == True:
    print(1)
else:
    print(0)

