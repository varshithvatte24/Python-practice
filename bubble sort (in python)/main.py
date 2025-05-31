user_input = input()
array = list(map(int,user_input.split()))
print(array)

#bubble sort
n = len(array)
for i in range(1,n):
    for j in range(0,n-i-1):
        if(array[j]>array[j+1]):
            temp = array[j+1]
            array[j+1] = array[j]
            array[j] = temp
print("Sorted array ->",array)