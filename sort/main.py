ui = input()
array = list(map(int, ui.split()))
print(array)
i = sorted(array)
print(i)

#Count Vowels in a String
string = input("Enter a string: ")
vowels = 'aeiouAEIOU'
count = 0
for char in string:
    if char in vowels:
        count += 1
print("Number of vowels:", count)

#Find Missing Number in a Sequence
arr = list(map(int, input("Enter numbers separated by space: ").split()))
n = len(arr) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)
missing_number = expected_sum - actual_sum
print("The missing number is:", missing_number)

#Anagram Checker
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Sort both strings and compare them
if sorted(string1) == sorted(string2):
    print("Anagram")
else:
    print("Not Anagram")
