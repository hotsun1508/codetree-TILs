# n = list(map(int, input().split("\n"))) # 방법 1: 이렇게는 안됨 
# n = [int(input()) for _ in range(5)] # 방법 2: List comprehension
satisfied = False

# for i in n:  # 방법 2로 할 경우 
for i in [int(input()) for _ in range(5)]: # 방법 3: 바로 for loop에 list comprehension 넣기 
    if i%3 == 0:
        # print(i, end='\n')
        satisfied = True
    else: 
        satisfied = False
        # print(i, end='\n')
        break     # 1개라도 3의 배수가 아니면 break 해야함 
# print(satisfied)

if satisfied == True:
    print(1)
else:
    print(0)

