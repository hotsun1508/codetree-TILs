n = int(input())

division = n
i = 1

while True: 
    division /= i
    
    if division <= 1:
        print(i)
        break
    
    i += 1