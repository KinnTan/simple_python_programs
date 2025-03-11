#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

number_list = []
while True:
    numbers = int(input())
    if numbers not in number_list:
        number_list.append(numbers)
        print("Unique")


