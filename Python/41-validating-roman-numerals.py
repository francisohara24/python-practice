# Link: https://www.hackerrank.com/challenges/validate-a-roman-number/problem
# Task:
# You are given a string, and you have to validate whether it's a valid Roman numeral.
#  If it is valid, print True. Otherwise, print False. Try to create a regular expression for a valid Roman numeral.
#
# Input Format
# A single line of input containing a string of Roman characters.
#
# Output Format
# Output a single line containing True or False according to the instructions above.
#
# Constraints
# The number will be between 1 and 3999 (both included).
import re

string = input()
regex = "[IVCDX]"  # to be updated

print(bool(re.search(regex, string)))
