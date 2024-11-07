# 시간 복잡도: O(n)


a, b = map(int, input().split())

sum_val = 0
count = 0
avg_val = 0

for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        sum_val += i
        count += 1
    if count != 0:
        avg_val = sum_val / count

print (sum_val, round(avg_val, 1))