# Time complexity: O(n)

n = int(input())

friendly_num = 0

for i in range(n+1):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        continue
    
    friendly_num += 1

print(friendly_num)
