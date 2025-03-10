#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

total = 0
for i in range(10):
    number = (int(input("Enter a Number: ")))
    total = total + number

print("The sum of all the numbers is:", total)


