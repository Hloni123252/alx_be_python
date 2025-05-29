# pattern_drawing.py

# Ask the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to handle the rows
while row < size:
    # Use a for loop to print asterisks on the same line
    for _ in range(size):
        print("*", end="")
    # Move to the next line after each row
    print()
    row += 1