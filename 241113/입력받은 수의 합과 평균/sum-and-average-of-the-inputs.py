# 시간 복잡도: O(n)


n = int(input())
# cnt = 0
sumval = 0

for i in range(n):
    i = int(input())

    sumval += i
    # cnt += 1

# print(sumval, round(sumval/cnt, 1))
print(f"{sumval} {sumval/n:.1f}")