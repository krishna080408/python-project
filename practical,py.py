
print("Welcome to the pattern Generator and number Analyzer!")
print("")
print("Select an option.")
print("1. Right-angled Triangle")
print("2. Pyramid")
print("3. Left-angled Triangle")
print("4. Analyze a range of Numbers")
print("")

Pattern = int(input("Enter your pattern: "))

if Pattern == 1:
    rows = int(input("Enter the number of rows for the pattern: "))
    print("Pattern:")
    for i in range(1, rows + 1):
        print("*" * i)
else:
    print("Invalid choice.")

Welcome to the pattern Generator and number Analyzer!

Select an option.
1. Right-angled Triangle
2. Pyramid
3. Left-angled Triangle
4. Analyze a range of Numbers

Enter your pattern: 1
Enter the number of rows for the pattern: 5
Pattern:
*
**
***
****
*****



print("Welcome to the Pattern Generator and Number Analyzer!\n")

print("Select an option:")
print("1. Right-angled Triangle")
print("2. Pyramid")
print("3. Left-angled Triangle")
print("4. Analyze a Range of Numbers")

choice = int(input("Enter your choice: "))

if choice == 1:
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    total = 0
    print()
    for num in range(start, end + 1):
        if num % 2 == 0:
            print("Number", num, "is Even")
        else:
            print("Number", num, "is Odd")
        total += num
    print("Sum of all numbers from", start, "to", end, "is:", total)

Welcome to the Pattern Generator and Number Analyzer!

Select an option:
1. Right-angled Triangle
2. Pyramid
3. Left-angled Triangle
4. Analyze a Range of Numbers
Enter your choice: 1
Enter the start of the range: 1
Enter the end of the range: 50

Number 1 is Odd
Number 2 is Even
Number 3 is Odd
Number 4 is Even
Number 5 is Odd
Number 6 is Even
Number 7 is Odd
Number 8 is Even
Number 9 is Odd
Number 10 is Even
Number 11 is Odd
Number 12 is Even
Number 13 is Odd
Number 14 is Even
Number 15 is Odd
Number 16 is Even
Number 17 is Odd
Number 18 is Even
Number 19 is Odd
Number 20 is Even
Number 21 is Odd
Number 22 is Even
Number 23 is Odd
Number 24 is Even
Number 25 is Odd
Number 26 is Even
Number 27 is Odd
Number 28 is Even
Number 29 is Odd
Number 30 is Even
Number 31 is Odd
Number 32 is Even
Number 33 is Odd
Number 34 is Even
Number 35 is Odd
Number 36 is Even
Number 37 is Odd
Number 38 is Even
Number 39 is Odd
Number 40 is Even
Number 41 is Odd
Number 42 is Even
Number 43 is Odd
Number 44 is Even
Number 45 is Odd
Number 46 is Even
Number 47 is Odd
Number 48 is Even
Number 49 is Odd
Number 50 is Even
Sum of all numbers from 1 to 50 is: 1275
    
