numbers_list = []
unique_numbers_list = []

for i in range(1,11):
    numbers = int(input("Enter a number:"))
    numbers_list.append(numbers)

for numbers in numbers_list:
    if numbers_list.count(numbers) == 1:
        unique_numbers_list.append(numbers)

print("Numbers without duplicates:", unique_numbers_list)