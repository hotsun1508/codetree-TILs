# 시간 복잡도: O(N) -> a를 b번 곱함

# 방법 1
# a, b = map(int, input().split())

# print (a**b)


# 방법 2

a, b = map(int, input().split())
prod = 1

for _ in range(b):
    prod *= a

print(prod)
