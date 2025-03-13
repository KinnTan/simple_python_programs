#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

number_list = []

while True:
    try:
        number = int(input("Enter numbers: "))
    except ValueError:
        break
    number_list.append(number)

print(max(number_list))