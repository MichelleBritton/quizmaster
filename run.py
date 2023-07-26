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

main()