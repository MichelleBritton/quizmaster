# Import modules
import json
from colorama import Fore, Back, Style
from tabulate import tabulate
import sys,time

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

def main():
    """
    Run all program functions
    """

typewriter("Welcome to Quiz Master\nAn app to ensure that your pub quiz runs smoothly\n\n")
print("Instructions\n\nTo start, enter the amount each person will pay to take part.\nEnter the team names and how many people are in that team.\nSelect a category and how many questions you would like and then all you need to do is read the questions and provide the answers!\nEnter the scores for each team at the end to show the leaderboard")
main()