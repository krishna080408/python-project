# Functional Treat – Simple + Functional Menu Program

data = []

def input_data():
    global data
    data = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Data stored successfully!")

def display_summary():
    if not data:
        print("No data available.")
        return
    print("Total items:", len(data))
    print("Minimum:", min(data))
    print("Maximum:", max(data))
    print("Sum:", sum(data))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def calculate_factorial():
    num = int(input("Enter number to find factorial: "))
    print("Factorial of", num, "is", factorial(num))

def filter_data():
    if not data:
        print("No data available.")
        return
    thresh = int(input("Enter threshold value: "))
    result = list(filter(lambda x: x >= thresh, data))
    print("Filtered values:", result)

def sort_data():
    if not data:
        print("No data available.")
        return
    print("1. Ascending\n2. Descending")
    opt = input("Choose option: ")
    if opt == '1':
        print("Sorted Ascending:", sorted(data))
    else:
        print("Sorted Descending:", sorted(data, reverse=True))

def dataset_stats():
    if not data:
        print("No data available.")
        return
    total = sum(data)
    avg = total / len(data)
    print("Min:", min(data))
    print("Max:", max(data))
    print("Sum:", total)
    print("Average:", round(avg, 2))

# Main Menu Loop
while True:
    print("\nMenu:")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data by Threshold")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit Program")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        print("You selected 1")
        input_data()
    elif choice == '2':
        print("You selected 2")
        display_summary()
    elif choice == '3':
        print("You selected 3")
        calculate_factorial()
    elif choice == '4':
        print("You selected 4")
        filter_data()
    elif choice == '5':
        print("You selected 5")
        sort_data()
    elif choice == '6':
        print("You selected 6")
        dataset_stats()
    elif choice == '7':
        print("You selected 7 - Exiting Program. Goodbye!")
        break
    else:
        print("Invalid input. Please enter a number from 1 to 7.")

'''
Menu:
1. Input Data
2. Display Data Summary
3. Calculate Factorial
4. Filter Data by Threshold
5. Sort Data
6. Display Dataset Statistics
7. Exit Program
Enter your choice (1-7): 1
You selected 1
Enter numbers separated by space: 20 40 50 70 90
Data stored successfully!

Menu:
1. Input Data
2. Display Data Summary
3. Calculate Factorial
4. Filter Data by Threshold
5. Sort Data
6. Display Dataset Statistics
7. Exit Program
Enter your choice (1-7): 2
You selected 2
Total items: 5
Minimum: 20
Maximum: 90
Sum: 270

Menu:
1. Input Data
2. Display Data Summary
3. Calculate Factorial
4. Filter Data by Threshold
5. Sort Data
6. Display Dataset Statistics
7. Exit Program
Enter your choice (1-7): 3
You selected 3
Enter number to find factorial: 20
Factorial of 20 is 2432902008176640000

Menu:
1. Input Data
2. Display Data Summary
3. Calculate Factorial
4. Filter Data by Threshold
5. Sort Data
6. Display Dataset Statistics
7. Exit Program
Enter your choice (1-7): 4
You selected 4
Enter threshold value: 100
Filtered values: []

Menu:
1. Input Data
2. Display Data Summary
3. Calculate Factorial
4. Filter Data by Threshold
5. Sort Data
6. Display Dataset Statistics
7. Exit Program
Enter your choice (1-7): 5
You selected 5
1. Ascending
2. Descending
Choose option: 1
Sorted Ascending: [20, 40, 50, 70, 90]

Menu:
1. Input Data
2. Display Data Summary
3. Calculate Factorial
4. Filter Data by Threshold
5. Sort Data
6. Display Dataset Statistics
7. Exit Program
Enter your choice (1-7): 6
You selected 6
Min: 20
Max: 90
Sum: 270
Average: 54.0

Menu:
1. Input Data
2. Display Data Summary
3. Calculate Factorial
4. Filter Data by Threshold
5. Sort Data
6. Display Dataset Statistics
7. Exit Program
Enter your choice (1-7): 7
You selected 7 - Exiting Program. Goodbye!

'''
