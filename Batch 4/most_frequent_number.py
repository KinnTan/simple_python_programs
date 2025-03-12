#Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most numbe

number_counter = {}

while True:
    try:
        number = int(input("Enter numbers: "))
    except ValueError:
        break

    if number in number_counter:
        number_counter[number] += 1
    else:
        number_counter[number] = 1

print(number_counter)

