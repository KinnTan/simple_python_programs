#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

numbers_list = []
unique_numbers_list = []

for i in range(1,11):
    numbers = int(input("Enter a number:"))
    numbers_list.append(numbers)

for numbers in numbers_list:
    if numbers_list.count(numbers) == 1:
        unique_numbers_list.append(numbers)

print("Numbers without duplicates:", unique_numbers_list)