# Time Complexity: O(n)
# 포인트: n==1인 조건을 n%2==1 조건 뒤에다가 하면 무한 루프 발생


n = int(input())
count = 0

while True: 
    if n == 1:
        break 
        # print('n: ', n)
        # print('count: ', count)
    elif n % 2 == 0:
        n = n / 2 
        count += 1
        # print('n: ', n)
        # print('count: ', count)
    elif n % 2 == 1:
        n = n * 3 + 1
        count += 1
        # print('n: ', n)
        # print('count: ', count)


print(count)