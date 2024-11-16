
n = int(input())

product = 1
for i in range(1, 11):
    product *= i
    if product >= n:
        print(i)
        break

