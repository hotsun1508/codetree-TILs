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