# multiplication_table.py

# Prompt the user for input
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")
