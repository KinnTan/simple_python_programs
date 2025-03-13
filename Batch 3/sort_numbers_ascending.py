number_list = []
while True:
    try:
        number = int(input("Enter a number: "))
        number_list.append(number)

    except ValueError:
        number_list.sort()
        print("Invalid number entered.")
        print("The sorted list from lowest to highest is:")
        print(number_list)
        break