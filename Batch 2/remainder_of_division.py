#Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second Number: "))

remainder = num1 % num2
print("The remainder when", num1, "is divided by", num2, "is", remainder)