Python
import random


# Tool 1: Quick To-Do List
# Lets the user add tasks, view the current list, or clear all tasks using a mutable list.
def run_todo_list():
    tasks = []
    print("\n--- Quick To-Do List ---")
    while True:
        print("\nTo-Do Options: [1] Add Task  [2] View Tasks  [3] Clear Tasks  [4] Back to Menu")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            task = input("Enter task description: ").strip()
            if task:
                tasks.append(task)
                print(f"Added task: '{task}'")
            else:
                print("Task cannot be empty!")
        elif choice == "2":
            if not tasks:
                print("Your to-do list is currently empty.")
            else:
                print("\nYour Current Tasks:")
                for index, item in enumerate(tasks, start=1):
                    print(f"{index}. {item}")
        elif choice == "3":
            tasks.clear()
            print("All tasks have been cleared.")
        elif choice == "4":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid option! Please select a number between 1 and 4.")


# Tool 2: Simple Calculator
# Performs basic arithmetic operations (+, -, *, /) and handles division-by-zero safely using conditionals.
def run_calculator():
    print("\n--- Simple Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid numeric input! Returning to main menu.")
        return

    print("Operations: [+] Add  [-] Subtract  [*] Multiply  [/] Divide")
    op = input("Choose operation (+, -, *, /): ").strip()

    if op == "+":
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif op == "-":
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif op == "*":
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    elif op == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Invalid operation choice!")


# Tool 3: Number Guessing Game
# Generates a secret number between 1 and 20 and uses a while loop to prompt guesses with feedback.
def run_guessing_game():
    print("\n--- Number Guessing Game ---")
    secret = random.randint(1, 20)
    attempts = 5
    print("I'm thinking of a number between 1 and 20. You have 5 attempts!")

    while attempts > 0:
        guess_input = input(f"Enter your guess ({attempts} attempts left): ").strip()
        
        if not guess_input.isdigit():
            print("Please enter a valid whole number!")
            continue

        guess = int(guess_input)
        attempts -= 1

        if guess == secret:
            print(f"Congratulations! You guessed the secret number {secret} correctly!")
            return
        elif guess < secret:
            print("Too low!")
        else:
            print("Too high!")

    print(f"Game over! The secret number was {secret}.")


# Main Program Menu Loop
def main():
    print("==========================================")
    print("    WELCOME TO THE PYTHON UTILITY TOOLKIT ")
    print("==========================================")

    while True:
        print("\nMain Menu:")
        print("1. Quick To-Do List")
        print("2. Simple Calculator")
        print("3. Number Guessing Game")
        print("4. Quit")

        choice = input("\nSelect an option (1-4): ").strip()

        if choice == "1":
            run_todo_list()
        elif choice == "2":
            run_calculator()
        elif choice == "3":
            run_guessing_game()
        elif choice == "4":
            print("\nThank you for using Python Utility Toolkit! Goodbye!")
            break
        else:
            print(f"'{choice}' is not a valid option. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
