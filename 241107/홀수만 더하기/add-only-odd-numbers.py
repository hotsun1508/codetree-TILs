# 시간 복잡도: O(n)


n = int(input())
sum_val = 0

for i in range(n):
    i = int(input())

    if i % 2 == 1 and i % 3 == 0:
        sum_val += i


print(sum_val)