

# BUILT-IN MODULES
import random
import math

# =========================
# FUNCTIONS
# =========================

def line():
    print("-" * 50)


# Function with parameters and return value
def check_answer(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()


# Function passed as an argument
def execute_function(func, value):
    return func(value)


# Simple function for demonstration
def square_number(num):
    return num * num


# =========================
# OPTION 1: SIMPLE QUIZ
# =========================
def simple_quiz():
    score = 0

    print("\nSIMPLE QUIZ")
    line()

    # QUESTION 1
    answer1 = input(
        "What fruit is green and round like a tennis ball and rhymes with chapel? "
    )

    if check_answer(answer1, "apple"):
        print("Correct!")
        score += 1          # assignment operator
    else:
        print("Wrong! The answer is apple.")

    # QUESTION 2
    answer2 = int(input("How many provinces are in South Africa? "))

    # comparison operator
    if answer2 == 9:
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The answer is 9 provinces.")

    # Nested condition and logical operator
    if score == 2:
        print("Excellent! You got all answers correct.")
    elif score == 1 and score < 2:
        print("Good try! You got 1 correct.")
    else:
        print("You need more practice.")

    print("Final Score:", score)


# =========================
# OPTION 2: DAILY MOTIVATION
# =========================
def motivation_generator():
    print("\nDAILY MOTIVATION GENERATOR")
    line()

    day = input("Enter the day of the week: ").lower()

    motivations = [
        "Monday: A fresh start. Stay focused and keep pushing!",
        "Tuesday: Success comes from hard work and consistency.",
        "Wednesday: You're halfway there. Keep going!",
        "Thursday: Great things take time. Don't give up.",
        "Friday: Finish the week strong and be proud of your progress.",
        "Saturday: Rest, recharge, and prepare for greatness.",
        "Sunday: Believe in yourself and plan for a successful week."
    ]

    days = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday"
    ]

    # for loop with range
    found = False

    for i in range(len(days)):
        if day == days[i]:
            print(motivations[i])
            found = True
            break           # loop control

    if not found:
        print("Invalid day entered.")


# =========================
# OPTION 3: EVEN OR ODD
# =========================
def even_or_odd():
    print("\nEVEN OR ODD CHECKER")
    line()

    # type casting
    number = int(input("Enter a number: "))

    # arithmetic operator
    if number % 2 == 0:
        print(number, "is EVEN")
    else:
        print(number, "is ODD")

    # Using math module
    square_root = math.sqrt(number)
    print("Square root:", round(square_root, 2))

    # Passing function as argument
    squared = execute_function(square_number, number)
    print("Squared number:", squared)


# =========================



# =========================
# MAIN PROGRAM
# =========================

while True:

    line()
    print("1. Simple Quiz")
    print("2. Daily Motivation Generator")
    print("3. Even or Odd Checker")
    print("4. Exit")
    line()

    # User input + type casting
    choice = int(input("Enter number (1-4): "))

    if choice == 1:
        simple_quiz()

    elif choice == 2:
        motivation_generator()

    elif choice == 3:
        even_or_odd()

    elif choice == 4:
        print("Program ended.")
        break

    else:
        print("Invalid choice. Please enter 1-4.")
