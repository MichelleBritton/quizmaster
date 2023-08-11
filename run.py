# Import modules
import json
import random
from colorama import Fore, Back, Style
from tabulate import tabulate
import sys
import time

POUND = chr(163)


def typewriter(message):
    """
    Create typewriter effect
    Credit: https://learnlearn.uk/python/python-typewriter-code
    """
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != "\n":
            time.sleep(0.1)
        else:
            time.sleep(1)


def play_amount():
    """
    Get play amount from user so that the total winnings can be calculated.
    Raises a ValueError if a number is not entered
    """
    while True:
        print(Fore.WHITE + "\nPlease enter the fee per person")
        try:
            amount = float(input(Fore.GREEN + "Enter the fee here:\n"))
        except ValueError:
            print(Fore.RED + "\nInvalid data, please enter a number")
        else:
            print(Fore.WHITE + f"\nThe fee per person is {POUND}{amount:.2f}"
                  "\n")
            break
    return amount


class IterTeam(type):
    """
    Use iterator method so we can loop through the Team instances
    """
    def __iter__(cls):
        return iter(cls._allTeams)


class Team(metaclass=IterTeam):
    """
    Team Class
    """
    _allTeams = []

    def __init__(self):
        self._allTeams.append(self)
        self.name = validate_name()
        self.size = get_size_from_user()

    def display_teams(self):
        """
        Show the number of people in each team
        """
        print(Fore.WHITE + f"There are {self.size} people in Team {self.name}")


def validate_name():
    """
    Validate user input for Team Name
    """
    while True:
        try:
            name = input(Fore.GREEN + "Enter Team Name here: \n")
            if len(name.strip()) == 0:
                print(Fore.RED + "Please enter the team name")
            elif len(name) > 30:
                print(Fore.RED + "Team name should be less than 30 characters")
            else:
                break
        except ValueError:
            print(Fore.RED + "Invalid data, please enter the team name")
        else:
            continue
    return name


def get_size_from_user():
    """
    Get the size of each team from the user and validate the input
    """
    while True:
        try:
            size = int(input(Fore.GREEN + "Enter size of Team here (max. 4 "
                             "players per team): \n"))
            if size > 4 or size == 0:
                print(Fore.RED + "Please enter a number between 1 and 4")
            else:
                break
        except ValueError:
            print(Fore.RED + "Invalid data, please enter a number")
        else:
            continue
    return size


def add_team():
    """
    Prompt to ask if you want to add another team and validate the input
    Add an instance of the Team class to the teams list
    """
    teams = []
    while True:
        teams.append(Team())
        while True:
            add_another_team = input(Fore.GREEN + "\nAdd another Team? Y/N \n")
            if add_another_team.lower() == 'y':
                break
            elif add_another_team.lower() == 'n':
                return teams
            else:
                print(Fore.RED + "Invalid input. Please type Y or N")
    return teams


def winnings(data, cost):
    """
    Calculate the winnings pot.
    Loop through the class objects and add the size of the teams up.
    Multiply the total size by the play amount to calculate the winnings.
    """
    total = 0
    for obj in data:
        total += obj.size
    print(Fore.WHITE + f"There are {total} people playing\n")
    pot = total * cost
    print(f"The total winnings for this game is {POUND}{pot:.2f}")


def get_questions():
    """
    Retrieves questions based on user input
    """
    categories = []
    questions = []

    # Open JSON file
    with open("quiz.json") as json_file:
        data = json.load(json_file)

    print("\nTo retrieve the questions, add a category\n")
    while True:
        add_cat = input(Fore.GREEN + "Add a category? Y/N \n")
        if add_cat.lower() == 'y':
            print(Fore.WHITE + "Please enter a number to select a category "
                  "from the following options:\n")

            # Extract the Categories and add them to a list and print them out
            cat_count = 1
            for category in data:
                print(cat_count, category)
                cat_count += 1

            # Select a category and the amount of questions for that category
            while True:
                try:
                    cat_select = int(input(Fore.GREEN + "\nEnter a number:\n"))
                    if cat_select == 1:
                        cat_select = "Food and Drink"
                    elif cat_select == 2:
                        cat_select = "General Knowledge"
                    elif cat_select == 3:
                        cat_select = "Movie Trivia"
                    elif cat_select == 4:
                        cat_select = "Geography"
                    elif cat_select == 5:
                        cat_select = "Sports"
                    elif cat_select == 6:
                        cat_select = "Animals"
                    elif cat_select == 7:
                        cat_select = "Politics"
                    elif cat_select == 8:
                        cat_select = "Quick Fire Questions"
                    else:
                        print(Fore.RED + "Please type a number between 1 & 8")
                        continue
                except ValueError:
                    print(Fore.RED + "Invalid data, please enter a number")
                else:
                    break

            # Validate quantity input
            while True:
                try:
                    quantity = int(input(Fore.GREEN + "How many "
                                         "questions?: \n"))
                    if quantity < 1 or quantity > 20:
                        print(Fore.RED + "Please enter a number between 1 and "
                              "20")
                    else:
                        break
                except ValueError:
                    print(Fore.RED + "Invalid data, please enter a number")

            # Retrieve a number of randomised questions for the selected
            # category and convert dictionary into a list
            result = list(data[cat_select].items())
            temp_questions = random.sample(result, quantity)
            questions.extend(temp_questions)

            continue
        elif add_cat.lower() == 'n':
            break
        else:
            print(Fore.RED + "Invalid input. Please type Y or N")

    # Iterate over the values in dictionary to create a new list for each value
    final_questions = []
    for q in questions:
        final_questions.append([x for x in q[1].values()])

    # Iterate over list of final questions to print out in a user friendly way
    q_count = 1
    for f in final_questions:
        print(Fore.CYAN + f"\nQuestion {q_count}: ", f[0])
        q_count += 1

    return final_questions


def show_answers(data):
    """
    Ask the user if they are ready to show the answers by pressing Y.
    If anything but Y is pressed showing the question again.
    """
    results = input(Fore.GREEN + "\nReady to share the answers? Type Y \n")
    print(Fore.WHITE + "Score for each question is one point")
    if results.lower() == 'y':
        q_count = 1
        for f in data:
            print(Fore.CYAN + f"\nQuestion {q_count}: ", f[0])
            print(Fore.MAGENTA + f"Answer {q_count}: ", f[1])
            q_count += 1
    else:
        show_answers(data)


def add_scores(data):
    """
    Add scores for each team
    """
    keys = []
    values = []

    print()
    # Iterate through each class instance
    for team in Team:
        # Add the team name to the keys list
        keys.append(team.name)
        # Request score and add it to the values list
        while True:
            try:
                score = int(input(Fore.GREEN + "Enter the score for Team "
                            f"{team.name}:\n"))
                if score > len(data):
                    print(Fore.RED + "Score cannot be higher than the number of questions")
                elif score > 0:
                    break
                else:
                    print(Fore.RED + "Please type a number greater than 0")
            except ValueError:
                print(Fore.RED + "Invalid data, please enter a number")
        values.append(score)

    # Create a dictionary from both lists
    # Credit:
    # https://www.geeksforgeeks.org/python-convert-two-lists-into-a-dictionary/
    scores = dict(zip(keys, values))
    return scores


def show_leaderboard(scores):
    """
    Show the leadboard and declare a winner
    """
    headers = ["Team Name", "Score"]
    print("\n", Fore.CYAN + tabulate(scores.items(), headers=headers))

    # Find the highest score
    top_score = max(scores.values())

    # Find the teams with the maximum scores
    winning_teams = [team for team, score in scores.items()
                     if score == top_score]

    if len(winning_teams) == 1:
        # Display the winner
        winner = winning_teams[0]
        print(f"\nThe winning team is {winner}!")
    else:
        # Declare a draw and show winning teams
        print(f"\nIt's a draw. The teams with the highest score are: ")
        for team in winning_teams:
            print(f"{team}")


def welcome_message():
    """
    Display welcome message and instructions
    """
    typewriter(Fore.WHITE + "Welcome to Quiz Master\nAn app to ensure that "
               "your pub quiz runs smoothly\n\n")
    print("Instructions\n\nTo start, enter the team names and how many people "
          "are in that team.\nEnter the amount each person will pay to take "
          "part. \nSelect a category and how many questions you would like "
          "and\nAll you need to do is read the questions and provide the "
          "answers!\nEnter the scores for each team at the end to show the "
          "leaderboard\n")


def main():
    """
    Run all program functions
    """
    welcome_message()
    all_teams = add_team()
    for team in all_teams:
        team.display_teams()
    winnings(all_teams, play_amount())
    data = get_questions()
    show_answers(data)
    scores = add_scores(data)
    show_leaderboard(scores)


if __name__ == "__main__":
    main()
