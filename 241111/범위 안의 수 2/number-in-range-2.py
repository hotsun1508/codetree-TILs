# 문제 이해
    # 0 <= 정수 <= 200 이어야 함
    # 위 조건을 만족하는 정수들의 합과 평균을 구해야 함!

cnt = 0
sum_val = 0

for i in range(10):
    i = int(input())

    if 0 <= i <= 200:
        sum_val += i
        cnt += 1
    
print(sum_val, round(sum_val/cnt, 1))

# print(f"{sum_val} {avg:.1f}") -> python formatting으로도 소수점 표현 가능