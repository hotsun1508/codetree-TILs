# Time Complexity: O(1)


while True: 
    width, height, char = input().split()

    print(int(width)*int(height))

    if char == 'C':
        break 


# Method 2. 
# while(True):
#     # Declare variables and receive input
#     inp = input()
#     arr = inp.split()
#     w = int(arr[0])
#     h = int(arr[1])
#     a = arr[2]
        
#     # Print the area of the rectangle. If the character C is entered, terminate.
#     print(w * h)
        
#     if a == 'C':
#         break