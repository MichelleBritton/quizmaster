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
        print("\nPlease enter the play amount per person")    
        try:
            amount = float(input("Enter the fee here:\n"))
        except ValueError:
            print("Invalid data, please enter a number")
        else:
            print (f"\nThe fee per person is {POUND}{amount:.2f}\n")
            break
    return amount

class Team:
    """
    Team Class
    """   
    def __init__(self):
        self.name = input("Enter Team Name here: \n")      
        self.size = get_size_from_user()         
    
    def display_teams(self):
        """
        Show the number of people in each team
        """
        print(f"There are {self.size} people in Team {self.name}")
    
def get_size_from_user():
    """
    Get the size of each team from the user and validate the input
    """
    while True:
        try:
            size = int(input("Enter size of Team here (max. 4 players per team): \n"))
            if size > 4 or size == 0:
                print("Please enter a number between 1 and 4")
            else:
                break
        except ValueError:
            print("Invalid data, please enter a number")
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
        add_another_team = input("\nDo you want to add a Team? Y/N \n")     
        if add_another_team.lower() == 'y':            
            continue
        elif add_another_team.lower() == 'n':
            break
        else:
            print("Invalid input. Please type Y or N") 
            add_team()    
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
    print(f"There are {total} people playing\n")
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
    
    print("Please select a category from one of the following options:\n")

    # Extract the Categories and add them to a list and print them out
    for category in data:
        categories.append(category)    
        print(category)

    # Select a category
    print()
    category_selection = input("Please enter a category here: \n")   
    print() 

    quantity = int(input("enter no of questions"))


    # Retrieve the questions for the selected category
    result = data[category_selection]     
    
    # Get the values from the dictionary and append them to the questions list
    values = result.values()
    for value in values:
        questions.append(value)
    
    # Print the questions and answers    
    # for i in questions:        
    #     print("Question: ", i["question"], "\nAnswer: ", i["answer"], "\n")

    
    count = 0
    while count < 5:
        for i in questions:
            print("Question: ", i["question"], "\nAnswer: ", i["answer"], "\n")
            count = count + 1
        
    
    
    
    
    
    

    
def main():
    """
    Run all program functions
    """
    # all_teams = add_team()
    # for team in all_teams:
    #     team.display_teams()
    # winnings(all_teams, play_amount())
    get_questions()
        
  

#typewriter("Welcome to Quiz Master\nAn app to ensure that your pub quiz runs smoothly\n\n")
#print("Instructions\n\nTo start, enter the amount each person will pay to take part.\nEnter the team names and how many people are in that team.\nSelect a category and how many questions you would like and then all you need to do is read the questions and provide the answers!\nEnter the scores for each team at the end to show the leaderboard\n")

main()
