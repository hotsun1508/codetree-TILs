n = int(input())

division = n
i = 1

while True: 
    division //= i
    # print("division", division)
    # print("i", i)
    
    if division <= 1:
        print(i)
        break
    
    i += 1