
# Name: WRITE YOUR FULL NAME
# Group: B
#
# 1. Input: scenarios_B.csv has 14 columns separated by
# semicolons. It contains situations, choices, money
# changes, reputation changes and feedback.
#
# 2. Each day: show a situation, ask for A/B/C,
# update the gauges and save the move.
#
# 3. Output: final result, title, best and worst move.
# results.csv saves name, budget, reputation, title, date.
#
# 4. Problems: invalid choice (ask again),
# negative gauge (stop), missing CSV (show error).
#
# Extra feature: Streak bonus.
# Three positive reputation changes give 500 EUR.

import csv
import random
import os
from datetime import datetime

FILE = "scenarios_B.csv"
RESULTS = "results.csv"


# Add three original situations to the CSV
def add_my_scenarios():
    new_scenarios = [
        [31, "A famous singer orders 100 croissants.",
         "Give a discount", -500, 15, "The singer loves it!",
         "Charge full price", 1000, 0, "Good business.",
         "Cancel the order", 0, -15, "Fans are angry."],

        [32, "A drone delivers croissants to the wrong house.",
         "Offer a refund", -200, 10, "Customer is happy.",
         "Ignore the complaint", 0, -20, "Bad reviews appear.",
         "Send a replacement", -100, 15, "Great service!"],

        [33, "A popular blogger visits your bakery.",
         "Offer free samples", -300, 20, "Great publicity!",
         "Ask for a paid review", -1000, 15, "More followers!",
         "Ignore the blogger", 0, -10, "Opportunity lost."]
    ]

    with open(FILE, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))

    existing = set()
    for row in rows[1:]:
        first = ",".join(row).split(";")[0].strip()
        if first.isdigit():
            existing.add(int(first))

    with open(FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        for scenario in new_scenarios:
            if scenario[0] not in existing:
                writer.writerow(scenario)


# Read the Group B scenario file
def load_scenarios():
    scenarios = []

    with open(FILE, newline="", encoding="utf-8-sig") as f:
        for row in list(csv.reader(f))[1:]:
            # Repair the extra comma formatting
            line = ",".join(row).rstrip(",")
            data = next(csv.reader([line], delimiter=";"))

            if len(data) != 14:
                continue

            options = {}
            for letter, index in [("A", 2), ("B", 6), ("C", 10)]:
                options[letter] = (
                    data[index],
                    int(data[index + 1]),
                    int(data[index + 2]),
                    data[index + 3]
                )

            scenarios.append((data[1], options))

    return scenarios


# Keep asking until the choice is valid
def get_choice():
    while True:
        choice = input("Your choice (A, B or C): ").strip().upper()
        if choice in ("A", "B", "C"):
            return choice
        print("Please type A, B or C.")


# Update budget and reputation
def apply_choice(budget, reputation, option):
    text, money, buzz, feedback = option
    budget += money
    reputation = min(100, reputation + buzz)
    return budget, reputation


# Calculate the player's final title
def get_title(budget, reputation):
    score = reputation + budget // 200

    if score < 95:
        return "Eternal Intern"
    elif score < 120:
        return "Growth Hacker"
    elif score < 140:
        return "CMO Material"
    else:
        return "Viral Legend"


# Save one result after each game
def save_result(name, budget, reputation, title):
    new_file = not os.path.exists(RESULTS)

    with open(RESULTS, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if new_file or os.path.getsize(RESULTS) == 0:
            writer.writerow(
                ["name", "budget", "reputation", "title", "date"]
            )

        writer.writerow([
            name, budget, reputation, title,
            datetime.now().strftime("%Y-%m-%d")
        ])


# Main game
def play_game():
    print("=== SURVIVE THE QUARTER ===")
    name = input("Enter your name: ").strip() or "Player"

    budget = 10000
    reputation = 50
    history = []
    streak = 0

    scenarios = load_scenarios()
    random.shuffle(scenarios)

    for day, (situation, options) in enumerate(scenarios[:10], 1):
        print("\n--- Day", day, "---")
        print("Budget:", budget, "EUR")
        print("Reputation:", reputation, "/100")
        print("\n", situation)

        for letter, option in options.items():
            print(letter + ":", option[0])

        choice = get_choice()
        option = options[choice]

        text, money, buzz, feedback = option
        budget, reputation = apply_choice(
            budget, reputation, option
        )

        print("\n", feedback)
        print("Budget change:", money)
        print("Reputation change:", buzz)

        history.append((buzz, day, text))

        # Extra feature: streak bonus
        if buzz > 0:
            streak += 1
        else:
            streak = 0

        if streak == 3:
            budget += 500
            print("Streak bonus! +500 EUR")
            streak = 0

        if budget <= 0 or reputation <= 0:
            print("\nGAME OVER! You are fired.")
            if budget <= 0:
                print("Reason: Budget reached zero.")
            if reputation <= 0:
                print("Reason: Reputation reached zero.")
            title = "Fired"
            break

    else:
        score = reputation + budget // 200
        title = get_title(budget, reputation)
        print("\nQuarter survived!")
        print("Final score:", score)
        print(name + ", your title:", title)

    print("\nFinal budget:", budget, "EUR")
    print("Final reputation:", reputation)

    if history:
        best = max(history)
        worst = min(history)

        print("Best move: Day", best[1], best[2], best[0])
        print("Worst move: Day", worst[1], worst[2], worst[0])

    save_result(name, budget, reputation, title)
    print("\nSaved in results.csv")


# Start the program
try:
    add_my_scenarios()
    play_game()
except FileNotFoundError:
    print("ERROR: Put scenarios_B.csv in the same folder.")
except (ValueError, IndexError) as error:
    print("CSV data error:", error)
