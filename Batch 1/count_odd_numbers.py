odd_counter = 0

for i in range(10):
    number = (int(input("Enter a number: ")))
    if number % 2 != 0:
        odd_counter += 1
print ("Total odd numbers:", odd_counter)