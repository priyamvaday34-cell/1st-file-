#code 1: Check if a number is even or odd
num = int(input("Enter a number: "))
rem = num % 2
if (rem == 0):
    print("Even")
else:
    print("Odd")

    #code 2: Find largest of three numbers method 1
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: ")) 
    if ((num1 >= num2) and (num1 >= num3)):
        print("The largest number is:", num1)
    elif ((num2 >= num1) and (num2 >= num3)):
        print("The largest number is:", num2)
    else:
        print("The largest number is:", num3)

#Find largest of three numbers method 2
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))        
num3 = float(input("Enter third number: "))
largest = max(num1, num2, num3)
print("The largest number is:", largest)

