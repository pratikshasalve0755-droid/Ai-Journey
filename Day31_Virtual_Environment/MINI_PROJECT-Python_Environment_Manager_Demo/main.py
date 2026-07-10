import os
import sys
from colorama import init , Fore ,  Style , Back
init(autoreset=True)

print("=== Current Python Version ===")
print("\nPython Version :-")
print(sys.version)
print()

print("=== Current Working Directory ===")
print("\nCurrent Working Directory :-")
print(os.getcwd())
print()

print("== The Sentence is in coloured using Colorama ==")
print(Fore.BLACK + Back.WHITE + " * Welcome To Python Environment Manager * ")
print(Style.RESET_ALL)
print()