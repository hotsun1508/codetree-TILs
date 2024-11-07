# 시간 복잡도: O(n)


a, b = map(int, input().split())

sum_val = 0
count = 0
avg_val = 0

for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        # print("-- i: ", i)
        sum_val += i
        count += 1
        # print("sum_val: ", sum_val, "count :", count)
    # if count != 0:
avg_val = sum_val / count
# print("avg_val: ", avg_val)

print (sum_val, round(avg_val, 1))



# a, b = map(int, input().split(" "))

# num = 0
# count = 0
# for i in range(a, b+1, 1):
#     if i % 5 == 0 or i % 7 == 0:
#         num += i
#         count += 1

# print(num, round(num / count, 1))