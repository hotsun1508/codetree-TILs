n = int(input())

# 방법 1 
cnt = 1 

for i in range(1, 2*n):  # 2n개 행만큼 출력 
    # print("i :", i)
    for j in range(n-cnt+1):  # 별의 개수는 입력한 정수 n에서 cnt를 뺌으로써 거꾸로 range(a,b,-1)와 같은 결과 
        # print("j :", j)
        print("*", end=" ")
    print()

    # print("before cnt :", cnt)
    if i < n:  # 행을 기준으로 cnt 증감 방향 바꾸기 
        cnt += 1
    else:
        cnt -= 1
    
    # print("after cnt :", cnt)


# 방법 2
# # 변수 선언 및 입력
# n = int(input())

# # 길이가 n인 직각삼각형을 뒤집어 출력합니다.
# for i in range(n-1, -1, -1):
# 	for _ in range(i+1):
# 		print("*", end=" ")
# 	print()
	
# # 길이가 n-1인 직각삼각형을 출력합니다.
# for i in range(1, n):
# 	for _ in range(i+1):
# 		print("*", end=" ")
# 	print()
