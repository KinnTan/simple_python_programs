#Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most numbe


while True:
    try:
        number = int(input("Enter numbers: "))
    except ValueError:
        break

