#code1:
user_input = input("Enter something: ")
try:
    int_input = int(user_input)
    print(f"You entered the integer:", int_input)
    print(f"Type of the input is: {type(int_input)}")
except ValueError:
        try:
            float_input = float(user_input)
            print("you entered:", float_input)
            print(f"Type of the input is: {type(float_input)}")
        except ValueError:
            print("you entered:", user_input)
            print(f"Type of the input is: {type(user_input)}")
    



#code2:
num1_str = input("Enter first number: ")
num2_str = input("Enter second number: ")
num1 = int(num1_str)
num2 = int(num2_str)
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is: {sum_result}")



#code3: swap with temp variable
a = 5
b = 10
temp = a
a = b
b = temp
print(f"After swapping (with temp variable): a = {a}, b = {b}")


#code4: swap without temp variable
a = 5
b = 10
a, b = b, a
print(f"After swapping (without temp variable): a = {a}, b = {b}")