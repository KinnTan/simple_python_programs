numbers = []
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

first_number = numbers[0]

for i in range(1, 10):
    results = first_number - numbers[i]
    print("Result of", first_number, "-", numbers[i], "=", results)


