# 방법 1: 조건에 OR 사용 -> 하나라도 만족하면 안되니까 

# n = int(input())


# for i in range(n+1):
#     if i % 2 == 0 or i % 10 == 5 or (i % 3 == 0 and i % 9 != 0):
#         continue
#     print(i, end=" ")


# 방법 2: 리스트 append

n = int(input())

whole_num = []
for i in range(n+1):
    if i % 2 == 0 or i % 10 == 5 or (i % 3 == 0 and i % 9 != 0):
        continue
    whole_num.append(i)

for j in whole_num:
    print(j, end=" ")
