# Import modules
import json
from colorama import Fore, Back, Style
from tabulate import tabulate
import sys,time

POUND = chr(163)

def typewriter(message):
    """
    Create typewriter effect
    Credit: https://learnlearn.uk/python/python-typewriter-code
    """
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        
        if char !=  "\n":
            time.sleep(0.1)
        else:
            time.sleep(1)

def play_amount():
    """
    Get play amount from user so that the total winnings can be calculated.
    Raises a ValueError if a number is not entered
    """
    while True:
        print("Please enter the play amount per person")        
    
        try:
            amount = float(input("Enter the fee here:\n"))
        except ValueError:
            print("Invalid data, please enter a number")
        else:
            print (f"The fee per person is {POUND}{amount:.2f}")
            break

    return amount

class Team:
    """
    Team Class
    """
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
def add_team():
    """
    Add Team name and size
    """
    print("")
    name = input("Enter Team Name here: \n") 
    size = input("Enter size of Team here: \n")

def main():
    """
    Run all program functions
    """
    play_amount()

typewriter("Welcome to Quiz Master\nAn app to ensure that your pub quiz runs smoothly\n\n")
print("Instructions\n\nTo start, enter the amount each person will pay to take part.\nEnter the team names and how many people are in that team.\nSelect a category and how many questions you would like and then all you need to do is read the questions and provide the answers!\nEnter the scores for each team at the end to show the leaderboard\n")

main()