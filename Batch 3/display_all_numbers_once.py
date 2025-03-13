display_list = []
for i in range(1,11):
    numbers = int(input("Enter a number: "))
    if numbers not in display_list:
        display_list.append(numbers)

print(display_list)