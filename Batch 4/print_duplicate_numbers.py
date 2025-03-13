duplicate = []
number_list = []

for i in range(1,11):
    numbers = int(input("Enter a number: "))
    if numbers in number_list:
        if numbers not in duplicate:
            duplicate.append(numbers)
        number_list.append(numbers)
    else:
        number_list.append(numbers)

print("Duplicates:", duplicate)

