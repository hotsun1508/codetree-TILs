# 방법 1
a, b = map(int, input().split())

sum_val = 0

if a < b: 
    for i in range(a, b+1):
        if i % 5 == 0:
            sum_val += i
else: 
    for i in range(b, a+1):
        if i % 5 == 0:
            sum_val += i

print(sum_val)


# 방법 2
# a, b = map(int, input().split())

# if a > b:
#     a, b = b, a

# sum = 0
# for i in range(a, b+1):
#     if i % 5 == 0:
#         sum += i

# print(sum)