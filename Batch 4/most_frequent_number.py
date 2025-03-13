number_counter = {}

while True:
    try:
        number = int(input("Enter numbers: "))
    except ValueError:
        break
    if number in number_counter:
        number_counter[number] += 1
    else:
        number_counter[number] = 1
if number_counter:
    most_frequent = max(number_counter, key=number_counter.get)
    print("The number with the most duplicates is:", most_frequent)
else:
    print("No numbers were entered.")

