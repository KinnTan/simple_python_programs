#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function

number_list = []
while True:
    try:
        number = int(input("Enter a number: "))
        number_list.append(number)

    except ValueError:
        number_list.sort()
        print("Invalid number entered. The sorted list is:")
        print(number_list)
        break