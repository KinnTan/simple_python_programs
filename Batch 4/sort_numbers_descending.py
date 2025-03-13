#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function

number_list = []
while True:
    try:
        number = int(input("Enter a number: "))
        number_list.append(number)

    except ValueError:
        number_list.sort(reverse=True)
        print("Invalid number entered.")
        print("The sorted list from highest to lowest is:")
        print(number_list)
        break