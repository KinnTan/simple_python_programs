#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

number_list = []

while True:
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        break
    number_list.append(number)

if number_list:
    print("The highest number entered is:", max(number_list))
else:
    print("No numbers entered")