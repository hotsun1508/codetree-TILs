input_list = ['a','b','c','d','e','f','g','h','i','j']
three = 0
five = 0

for num in input_list: 
    num = int(input())
    if num%3==0:
        three += 1
    if num%5 == 0:
        five += 1

print(three, five)

# cnt3=0
# cnt5=0

# for i in range(10):
#     n=int(input())
#     if n%3==0:
#         cnt3+=1
#     if n%5==0:
#         cnt5+=1

# print(cnt3,cnt5)