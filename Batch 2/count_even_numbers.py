#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

even_count = 0
for i in range(10):
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        even_count += 1
print ("Total even numbers:", even_count)