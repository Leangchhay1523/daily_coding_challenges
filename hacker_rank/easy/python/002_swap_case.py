"""

Task
==============
You are given a string and your task is to swap cases. 
In other words, convert all lowercase letters to uppercase letters and vice versa.

Example:
- Www.HackerRank.com → wWW.hACKERrANK.COM
- Pythonist 2 → pYTHONIST 2  

"""

# Solution
def swap_case(s):
    return " ".join("".join(char.lower() if char.isupper() else char.upper() for char in word) for word in s.split())

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)