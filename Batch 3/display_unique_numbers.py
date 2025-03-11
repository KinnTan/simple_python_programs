#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

numbers_list = []

for i in range(1,11):
    numbers = int(input())
    numbers_list.append(numbers)

print(numbers_list)