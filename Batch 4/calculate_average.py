numbers = []
while True:
    try:
        input_number = int(input("Enter a number: "))
        numbers.append(input_number)

    except ValueError:
        if numbers:
            average = sum(numbers)/len(numbers)
            print("The average of the entered numbers is:", average)
        else:
            print("No numbers we're entered. Exiting...")
        break