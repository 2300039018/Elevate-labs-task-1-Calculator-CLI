def compute(num1, op, num2):
    """Compute operation based on operator."""
    operations = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2 if num2 != 0 else "Error! Division by zero."
    }
    if op in operations:
        return operations[op]
    else:
        return "Error! Invalid operator. Use +, -, *, or /."

def main():
    """Main function to run the expression-based calculator loop."""
    print("Welcome to the Expression Calculator! (e.g., 5 + 3)")
    
    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            op = input("Enter operator (+, -, *, /): ").strip()
            num2 = float(input("Enter second number: "))
            
            result = compute(num1, op, num2)
            
            if isinstance(result, str):
                print(result)
            else:
                print(f"{num1} {op} {num2} = {result}")
                # Display as int if exact
                if isinstance(result, float) and result.is_integer():
                    print(f"({int(result)})")
            
            continue_choice = input("Another calculation? (y/n): ").lower().strip()
            if continue_choice != 'y':
                print("Goodbye!")
                break
                
        except ValueError:
            print("Invalid number. Please try again.")

if __name__ == "__main__":
    main()
