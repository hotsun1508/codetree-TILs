# Time Complexity: O(n)

sum_age, cnt = 0, 0

while(True):
    age = int(input())
    # print("age :", age)

    if age < 20 or age >= 30:
        break
    
    sum_age += age 
    cnt += 1
    # print("sum_age", sum_age)
    # print("cnt", cnt)

if cnt > 0:
    # print(round(sum_age/cnt, 2))
    print(f"{sum_age/cnt:.2f}")
