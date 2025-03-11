#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

number_list = []
while True:
    try:
        number = int(input("Enter a number: "))
        number_list.append(number)

    except ValueError:
        break
