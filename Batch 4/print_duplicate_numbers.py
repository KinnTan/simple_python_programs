#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

duplicate = []
number_list = []

for i in range(1,11):
    numbers = int(input())
    if numbers in number_list:
        if numbers not in duplicate:
            duplicate.append(numbers)
        number_list.append(numbers)
    else:
        number_list.append(numbers)

print(duplicate)

