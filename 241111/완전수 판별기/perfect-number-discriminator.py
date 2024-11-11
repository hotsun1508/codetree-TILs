n = int(input())

sum_val = 0

for i in range(1, n):  # 1부터 시작하지 않으면, i=0인 경우 에러 발생
    if n % i == 0:
        sum_val += i
    
if sum_val == n:
    print ("P")
else:
    print("N")