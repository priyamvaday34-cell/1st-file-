'''
#code1(a): word frequency counter
def word_frequency_counter(s):
    words = s.split()
    frequency = {}
    for word in words:
        word = word.lower()
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency
user_input = input("Enter a string to count word frequency: ")
word_freq = word_frequency_counter(user_input)
print("Word Frequency:")
for word, count in word_freq.items():
    print(f"{word}: {count}")


    #code2(a): students marks dictionary
student_marks = {}
n = int(input("Enter number of students: "))
for i in range(n):
    name = input(f"Enter name of student : ")
    marks =[]
    for j in range(3):
         mark = float(input(f"Enter mark {j+1} for {name}: "))
         marks.append(mark)
         student_marks[name] = marks

print("\nStudent Marks:")
for name, marks in student_marks.items():
    print(f"{name}: {marks}")


 #code3(a): find common elements using sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
common_elements = set1.intersection(set2)
print("Common elements:", common_elements)


#code1(b): function to check  prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number to check if it's prime: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
'''

#code2(b): function for factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {num} is {factorial(num)}.")
