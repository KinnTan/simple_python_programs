#Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

display_list = []
for i in range(1,11):
    numbers = int(input("Enter a number: "))
    if numbers not in display_list:
        display_list.append(numbers)

print(display_list)