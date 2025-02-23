"""
Task
===============
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 
For example, alison heck should be capitalised correctly as Alison Heck.

"""

# Solution
def solve(s):
    splitS = s.split()
    return " ".join(word.capitalize() for word in splitS)

s = input()
print(solve(s))