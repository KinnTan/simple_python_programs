#Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second Number: "))

if num1 > num2:
    print ("The smaller number is", num2)
else:
    print ("The smaller number is", num1)