#code1: calculator for grades
def calculate_grade(marks):
    if (marks >= 90):
        return 'A+'
    elif (marks >= 80):
        return 'A'
    elif (marks >= 70):
        return 'B'
    elif (marks >= 60):
        return 'B+'
    elif (marks >= 50):
        return 'C'
    elif (marks >= 40):
        return 'D'
    else:
        return 'F'  
marks = float(input("Enter your marks: "))
if marks < 0 or marks > 100:
    print("Invalid marks entered.")
else:
     grade = calculate_grade(marks)
     print("Your grade is:", grade)

#code2: calculate for electricity bill
def calculate_electricity_bill(units):
          if (units <= 100):
            return units * 1.5
          elif (units <= 200):
            return 100 * 1.5 + (units - 100) * 2.5
          elif(units <= 300):
           return  100 * 1.5 + 100 * 2.5 + (units - 200) * 4
          else:
            return 100 * 1.5 + 100 * 2.5 + 100 * 4 + (units - 300) * 6
units = float(input("Enter the number of electricity units consumed: "))
if (units < 0):
     print("Invalid input.")
else:
    bill = calculate_electricity_bill(units)
    print(f"Your electricity bill is: {bill}")


#code3: Factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Enter a number to find its factorial: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is: {result}")


    #2nd method
    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result