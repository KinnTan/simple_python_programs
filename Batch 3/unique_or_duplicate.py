number_list = []
while True:
    try:
        numbers = int(input())
    except ValueError:
        print("invalid number, exiting...")
        break

    if numbers not in number_list:
        number_list.append(numbers)
        print("Unique")
    elif numbers in number_list:
        print("Duplicate")

