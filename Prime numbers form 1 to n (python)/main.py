import math

num = int(input("Enter the number: "))
if num < 1:
    print("Please enter a valid number")
elif num == 1:
    print("1 is not a prime number")
else:
    print("Prime numbers from 1 to", num, "are:")
    for i in range(2, num + 1):
        count = 0 
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                count += 1
                break 
        if count == 0:  
            print(i)
