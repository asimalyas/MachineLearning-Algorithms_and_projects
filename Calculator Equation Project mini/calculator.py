# import os

history = []  # List to store calculation history

def calculate():
    
    eq = input("Enter the equation (e.g., 5 + 3 * 2): ")
    try:
        result = eval(eq)  # Evaluate the equation
        record = f"{eq} = {result}"
        print("Result:", result)
        history.append(record)
    except:
        print("Invalid equation!")

def save_to_file():
    with open("calculator_history.txt", "a") as file:
        for item in history:
            file.write(item + "\n")
    print("History saved to 'calculator_history.txt'")
    history.clear()  # Clear after saving to avoid duplicates

def show_history():
    if not history:
        print("No calculations in current session!")
    else:
        print("\n--- History ---")
        for item in history:
            print(item)

# Main menu
while True:
    print("\n=== Calculator Menu ===")
    print("1. Calculate")
    print("2. Show History")
    print("3. Save History to File")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        calculate()
    elif choice == "2":
        show_history()
    elif choice == "3":
        save_to_file()
    elif choice == "4":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")

