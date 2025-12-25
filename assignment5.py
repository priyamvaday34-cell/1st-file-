#code1: reverse string
def reverse_string(s):
    return s[::-1]
user_input = input("Enter a string to reverse: ")
reversed_str = reverse_string(user_input)
print(f"Reversed string: {reversed_str}")



#code2:count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
user_input = input("Enter a string to count vowels: ")
vowel_count = count_vowels(user_input)
print(f"Number of vowels: {vowel_count}")



#code3: find max and min in a list
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
maximum = max(numbers)
minimum = min(numbers)
print(f"Maximum number in the list: {maximum}")
print(f"Minimum number in the list: {minimum}")



#code4: create tuple and demonstrate immutability
my_tuple = (1, 2, "three", 4.5)
print(f" originalTuple: {my_tuple}")
try:
    my_tuple[1] = 99
except TypeError as e:
    print(f"Error when trying to modify tuple(demonstrating immutability): {e}")
    new_tuple = my_tuple + (6,)
print(f"Tuple after attempted concatenation: {new_tuple}")



#code5: check palindrome
def is_palindrome(n):
    str_n = str(n)
    return str_n == str_n[::-1]
number = int(input("Enter a number to check if it's a palindrome: "))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
    
    