number_list = []
while True:
    try:
        number = int(input("Enter a number: "))
        number_list.append(number)

    except ValueError:
        print("invalid number")
        print("the lowest number was", min(number_list))
        break
