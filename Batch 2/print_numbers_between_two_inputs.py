#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 < num2:
    for i in range(num1 + 1, num2):
        print (i)
if num1 > num2:
    for i in range(num2 + 1, num1):
        print (i)