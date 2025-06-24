n = int(input())
satisfied = True

for i in range (2, 1001):
    # 소수: 자기 자신이랑 나누어떨어지면서, 다른 숫자들은 나누어 떨어지지 않음 
    # 소수가 아님: 자기 자신외에도 나누어 떨어지는 숫자 존재  
    if i%n != 0 and n%i == 0:
        satisfied = False
         
if satisfied == True:
    print("P") #Prime Number 
else:
    print("C") #Compound Number 