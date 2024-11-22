# Time Complexity: O(1) -> 루프 안에서 각 반복의 비용은 고정되어 있음
    # 이유
        # - 입력을 받는 데  O(1) 
	    # - 조건 확인  O(1) 
	    # -	출력  O(1) 


while True: 
    n = int(input())
    if n == 0:
        break
    
    print(n)
