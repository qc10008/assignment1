# Program Name: Assignment1.py
# Course: IT3883/Section W01
# Student Name: Quin Costales
# Assignment Number: Assignment #1
# Due Date: 9/5/2025
# Purpose:
#   This program implements a text-based menu with four options:
#   1) Append data to an input buffer
#   2) Clear the input buffer
#   3) Display the input buffer
#   4) Exit the program
# Resources used:
#   - Python official documentation: https://docs.python.org/3/
#   - Help from ChatGPT for structuring menu logic (code written by me)
# ----------------- MAIN PROGRAM -----------------

# input buffer starts empty
inputbuff = ""

# Infinite loop to keep the menu keeps showing
while True:
    # Print menu
    print("\n--- Text Menu ---")
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit program")

    # Prompt user
    Userchoice = input("Enter your choice (1-4): ")

    # choices
    if Userchoice == "1":
        # Append
        newdata = input("Enter text to append: ")
        inputbuff += newdata  # new string
        print("Data appended successfully.")

    elif Userchoice == "2":
        # Clear
        inputbuff = ""
        print("Input buffer cleared.")

    elif Userchoice == "3":
        # current buffer
        if inputbuff:
            print("Current input buffer:", inputbuff)
        else:
            print("Input buffer is empty.")

    elif Userchoice == "4":
        # Exit
        print("Goodbye")
        break

    else:
        # invalid menu choice
        print("Invalid choice, use a number from 1 to 4.")
