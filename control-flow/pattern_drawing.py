# pattern_drawing.py
# A program that draws a square pattern using nested loops

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter for while loop
row = 0

# While loop for each row
while row < size:
    # For loop to print stars in each row
    for col in range(size):
        print("*", end="")
    # Move to the next line after each row
    print()
    row += 1
