def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return "Error! Division by zero."
        result /= num
    return result

def perform_operation(choice):
    num_count = int(input("Enter number of values: "))
    numbers = []
    
    for i in range(num_count):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    
    if choice == '1':
        print(f"Sum: {add(numbers)}")
    elif choice == '2':
        print(f"Difference: {subtract(numbers)}")
    elif choice == '3':
        print(f"Product: {multiply(numbers)}")
    elif choice == '4':
        print(f"Quotient: {divide(numbers)}")

def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter choice (1/2/3/4/5): ")
        
        if choice == '5':
            print("Exiting the calculator.")
            break
        elif choice in ['1', '2', '3', '4']:
            perform_operation(choice)
        else:
            print("Invalid input")

calculator()
