# Time Complexity: O(n)
    # In the worst case, the loop runs for all n input values, 
    # and each iteration involves  O(1) operations (condition check, summation, and increment).

O(n \times O(1)) = O(n)


sum_age, cnt = 0, 0

while(True):
    age = int(input())

    if age < 20 or age >= 30:
        break
    
    sum_age += age 
    cnt += 1

if cnt > 0:
    # print(round(sum_age/cnt, 2))
    print(f"{sum_age/cnt:.2f}")
