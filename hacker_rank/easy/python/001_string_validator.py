"""
Task
===============
You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, 
alphabetical characters, digits, lowercase and uppercase characters.

Output Format
===============
In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

"""

# Solution
if __name__ == '__main__':
    s = input()
    alphanumCheck = any(char.isalnum() for char in s)
    alphaCheck = any(char.isalpha() for char in s)
    digitCheck = any(char.isdigit() for char in s)
    lowerCheck = any(char.islower() for char in s)
    upperCheck = any(char.isupper() for char in s)
    
    checks = [alphanumCheck, alphaCheck, digitCheck, lowerCheck, upperCheck]
    for ele in checks:
        print(ele)