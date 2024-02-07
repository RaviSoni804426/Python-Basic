n = int(input("Enter the value of n: "))

for i in range(1, n+1):
    # Print characters from 'A' to the current row number
    for j in range(1, i+1):
        char = chr(ord('A') + j - 1)  # Convert number to corresponding character
        print(char, end="")
    print()  # Move to the next line after each row
